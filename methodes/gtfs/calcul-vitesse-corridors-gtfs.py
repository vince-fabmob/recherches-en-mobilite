"""
Statut : implémentation reproductible indicative d'une méthode établie.
Référence : GTFS Schedule Reference et GTFS Schedule Best Practices, MobilityData.
Données : GTFS statique + CSV de corridors définis par arrêts-borne.
Sortie : vitesses commerciales programmées par voyage et agrégées par corridor.
Méthode : temps GTFS ; distance curviligne le long de shapes.txt dans un SCR métrique.
Validation : AVL/GPS ou GTFS-Realtime pour toute mesure de vitesse observée.
Limites : le résultat est planifié ; la qualité dépend des horaires, formes et arrêts GTFS.
Dernière vérification : 2026-08-14
"""

from __future__ import annotations
import argparse
import zipfile
from datetime import date, datetime
from pathlib import Path
import pandas as pd
from pyproj import Transformer
from shapely.geometry import LineString, Point


def read_table(source: Path, filename: str, **kwargs) -> pd.DataFrame:
    if source.is_dir():
        return pd.read_csv(source / filename, **kwargs)
    with zipfile.ZipFile(source) as archive:
        names = {Path(name).name: name for name in archive.namelist()}
        if filename not in names:
            raise FileNotFoundError(filename)
        with archive.open(names[filename]) as handle:
            return pd.read_csv(handle, **kwargs)


def seconds(value: str) -> int:
    hours, minutes, secs = map(int, str(value).split(':'))
    if hours < 0 or minutes not in range(60) or secs not in range(60):
        raise ValueError(f'Heure GTFS invalide : {value}')
    return 3600 * hours + 60 * minutes + secs


def active_services(source: Path, service_date: date) -> set[str]:
    active: set[str] = set()
    weekday = service_date.strftime('%A').lower()
    try:
        calendar = read_table(source, 'calendar.txt', dtype={'service_id': str})
        start = pd.to_datetime(calendar['start_date'], format='%Y%m%d').dt.date
        end = pd.to_datetime(calendar['end_date'], format='%Y%m%d').dt.date
        active.update(calendar.loc[(start <= service_date) & (end >= service_date) & (calendar[weekday] == 1), 'service_id'].astype(str))
    except FileNotFoundError:
        pass
    try:
        exceptions = read_table(source, 'calendar_dates.txt', dtype={'service_id': str})
        day = pd.to_datetime(exceptions['date'], format='%Y%m%d').dt.date == service_date
        exceptions = exceptions.loc[day]
        active.difference_update(exceptions.loc[exceptions['exception_type'] == 2, 'service_id'].astype(str))
        active.update(exceptions.loc[exceptions['exception_type'] == 1, 'service_id'].astype(str))
    except FileNotFoundError:
        pass
    if not active:
        raise ValueError('Aucun service actif : vérifier la date et les calendriers GTFS.')
    return active


def shape_lines(shapes: pd.DataFrame, transformer: Transformer) -> dict[str, LineString]:
    lines = {}
    for shape_id, group in shapes.sort_values(['shape_id', 'shape_pt_sequence']).groupby('shape_id'):
        coordinates = [transformer.transform(lon, lat) for lon, lat in zip(group['shape_pt_lon'], group['shape_pt_lat'])]
        if len(coordinates) >= 2:
            line = LineString(coordinates)
            if line.is_valid and line.length > 0:
                lines[str(shape_id)] = line
    return lines


def corridor_rows(source: Path, service_date: date, corridors_path: Path, epsg: int, max_error: float) -> tuple[pd.DataFrame, pd.DataFrame]:
    services = active_services(source, service_date)
    corridors = pd.read_csv(corridors_path, dtype=str)
    required = {'corridor_id', 'corridor_name', 'from_stop_id', 'to_stop_id'}
    if not required.issubset(corridors.columns):
        raise ValueError(f'Colonnes requises : {sorted(required)}')
    trips = read_table(source, 'trips.txt', dtype=str)
    trips = trips.loc[trips.service_id.isin(services) & trips.shape_id.notna()].copy()
    times = read_table(source, 'stop_times.txt', dtype={'trip_id': str, 'stop_id': str, 'arrival_time': str, 'departure_time': str, 'stop_sequence': int})
    stops = read_table(source, 'stops.txt', dtype={'stop_id': str})
    shapes = read_table(source, 'shapes.txt', dtype={'shape_id': str, 'shape_pt_sequence': int, 'shape_pt_lat': float, 'shape_pt_lon': float})
    transformer = Transformer.from_crs(4326, epsg, always_xy=True)
    lines = shape_lines(shapes, transformer)
    stop_points = {str(row.stop_id): Point(transformer.transform(row.stop_lon, row.stop_lat)) for row in stops.itertuples()}
    joined = times.merge(trips[['trip_id', 'route_id', 'direction_id', 'shape_id']], on='trip_id', how='inner')
    rows, rejected = [], []
    for corridor in corridors.itertuples(index=False):
        origin = joined.loc[joined.stop_id == corridor.from_stop_id]
        destination = joined.loc[joined.stop_id == corridor.to_stop_id]
        merged = origin.merge(destination, on=['trip_id', 'route_id', 'direction_id', 'shape_id'], suffixes=('_from', '_to'))
        for trip in merged.itertuples(index=False):
            base = {'corridor_id': corridor.corridor_id, 'corridor_name': corridor.corridor_name, 'trip_id': trip.trip_id, 'route_id': trip.route_id, 'direction_id': trip.direction_id, 'shape_id': trip.shape_id}
            if trip.stop_sequence_to <= trip.stop_sequence_from:
                rejected.append(base | {'exclusion_reason': 'ordre_arrets_invalide'})
                continue
            try:
                time_minutes = (seconds(trip.arrival_time_to) - seconds(trip.departure_time_from)) / 60
            except (ValueError, TypeError):
                rejected.append(base | {'exclusion_reason': 'heure_invalide'})
                continue
            line, from_point, to_point = lines.get(str(trip.shape_id)), stop_points.get(str(corridor.from_stop_id)), stop_points.get(str(corridor.to_stop_id))
            if line is None or from_point is None or to_point is None:
                rejected.append(base | {'exclusion_reason': 'forme_ou_arret_absent'})
                continue
            from_position, to_position = line.project(from_point), line.project(to_point)
            from_error, to_error = from_point.distance(line), to_point.distance(line)
            distance_m = to_position - from_position
            if time_minutes <= 0 or distance_m <= 0:
                rejected.append(base | {'exclusion_reason': 'temps_ou_distance_non_positif'})
                continue
            if max(from_error, to_error) > max_error:
                rejected.append(base | {'exclusion_reason': 'ecart_arret_forme_excessif'})
                continue
            rows.append(base | {'from_stop_id': corridor.from_stop_id, 'to_stop_id': corridor.to_stop_id, 'scheduled_time_minutes': time_minutes, 'distance_m': distance_m, 'scheduled_speed_kmh': distance_m / 1000 / (time_minutes / 60), 'from_stop_shape_error_m': from_error, 'to_stop_shape_error_m': to_error, 'max_stop_shape_error_m': max(from_error, to_error), 'distance_method': f'shapes.txt / EPSG:{epsg}'})
    return pd.DataFrame(rows), pd.DataFrame(rejected)


def aggregate(rows: pd.DataFrame) -> pd.DataFrame:
    if rows.empty:
        return rows
    keys = ['corridor_id', 'corridor_name', 'route_id', 'direction_id', 'from_stop_id', 'to_stop_id']
    output = rows.groupby(keys, dropna=False).agg(voyages_retenus=('trip_id', 'nunique'), distance_mediane_m=('distance_m', 'median'), temps_median_min=('scheduled_time_minutes', 'median'), vitesse_mediane_kmh=('scheduled_speed_kmh', 'median'), distance_totale_m=('distance_m', 'sum'), temps_total_min=('scheduled_time_minutes', 'sum'), erreur_max_arret_forme_m=('max_stop_shape_error_m', 'max')).reset_index()
    output['vitesse_ponderee_kmh'] = output.distance_totale_m / 1000 / (output.temps_total_min / 60)
    return output.drop(columns=['distance_totale_m', 'temps_total_min'])


def main() -> None:
    parser = argparse.ArgumentParser(description='Calcule les vitesses commerciales programmées par corridor GTFS.')
    parser.add_argument('--gtfs', required=True, type=Path)
    parser.add_argument('--date', required=True)
    parser.add_argument('--corridors', required=True, type=Path)
    parser.add_argument('--output-prefix', required=True, type=Path)
    parser.add_argument('--epsg', type=int, default=32188)
    parser.add_argument('--max-stop-shape-error-m', type=float, default=100)
    args = parser.parse_args()
    service_date = datetime.strptime(args.date, '%Y-%m-%d').date()
    rows, rejected = corridor_rows(args.gtfs, service_date, args.corridors, args.epsg, args.max_stop_shape_error_m)
    args.output_prefix.parent.mkdir(parents=True, exist_ok=True)
    rows.to_csv(f'{args.output_prefix}_voyages.csv', index=False)
    aggregate(rows).to_csv(f'{args.output_prefix}_corridors.csv', index=False)
    rejected.to_csv(f'{args.output_prefix}_exclusions.csv', index=False)


if __name__ == '__main__':
    main()
