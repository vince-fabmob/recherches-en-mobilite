"""
Statut : implémentation reproductible indicative d'une méthode établie
Référence : GTFS Schedule Reference, MobilityData ; principes de calcul de temps de parcours
et vitesse planifiés à partir d'horaires et de distances documentées.
Données : GTFS statique — trips.txt, stop_times.txt ; priorité à shape_dist_traveled.
Sortie : vitesse commerciale programmée entre deux arrêts pour chaque voyage retenu.
Hypothèses : distance = différence de shape_dist_traveled lorsque la colonne est complète et croissante ;
le temps couvre l'horaire entre le départ à l'arrêt amont et l'arrivée à l'arrêt aval.
Validation : comparer avec AVL/GPS pour estimer vitesse observée et variabilité.
Limites : ne mesure pas la vitesse réelle ; exclut les voyages sans distance GTFS défendable.
Dernière vérification : 2026-08-14
"""

from __future__ import annotations

import argparse
import zipfile
from datetime import date, datetime
from pathlib import Path

import pandas as pd


def read_gtfs_table(gtfs_path: Path, filename: str, **kwargs) -> pd.DataFrame:
    """Lit un fichier GTFS depuis un dossier ou une archive ZIP."""
    if gtfs_path.is_dir():
        path = gtfs_path / filename
        if not path.exists():
            raise FileNotFoundError(f"Fichier GTFS introuvable : {path}")
        return pd.read_csv(path, **kwargs)
    if gtfs_path.suffix.lower() == ".zip":
        with zipfile.ZipFile(gtfs_path) as archive:
            names = {Path(name).name: name for name in archive.namelist()}
            if filename not in names:
                raise FileNotFoundError(f"{filename} est absent de l'archive {gtfs_path.name}")
            with archive.open(names[filename]) as handle:
                return pd.read_csv(handle, **kwargs)
    raise ValueError("--gtfs doit pointer vers un dossier GTFS ou une archive .zip")


def gtfs_time_to_seconds(value: str) -> int:
    """Convertit HH:MM:SS GTFS en secondes, y compris les heures > 24:00:00."""
    if pd.isna(value) or not str(value).strip():
        raise ValueError("Heure GTFS vide")
    parts = str(value).strip().split(":")
    if len(parts) != 3:
        raise ValueError(f"Heure GTFS invalide : {value}")
    hours, minutes, seconds = map(int, parts)
    if hours < 0 or minutes not in range(60) or seconds not in range(60):
        raise ValueError(f"Heure GTFS invalide : {value}")
    return hours * 3600 + minutes * 60 + seconds


def active_service_ids(gtfs_path: Path, service_date: date) -> set[str]:
    """Retourne les service_id actifs pour une date, selon les calendriers GTFS."""
    ids: set[str] = set()
    weekday = service_date.strftime("%A").lower()
    try:
        calendar = read_gtfs_table(gtfs_path, "calendar.txt", dtype={"service_id": str})
        calendar["start_date"] = pd.to_datetime(calendar["start_date"], format="%Y%m%d").dt.date
        calendar["end_date"] = pd.to_datetime(calendar["end_date"], format="%Y%m%d").dt.date
        active = calendar.loc[
            (calendar["start_date"] <= service_date)
            & (calendar["end_date"] >= service_date)
            & (calendar[weekday] == 1),
            "service_id",
        ]
        ids.update(active.astype(str))
    except FileNotFoundError:
        pass
    try:
        exceptions = read_gtfs_table(gtfs_path, "calendar_dates.txt", dtype={"service_id": str})
        exceptions = exceptions.loc[
            pd.to_datetime(exceptions["date"], format="%Y%m%d").dt.date == service_date
        ]
        ids.difference_update(exceptions.loc[exceptions["exception_type"] == 2, "service_id"].astype(str))
        ids.update(exceptions.loc[exceptions["exception_type"] == 1, "service_id"].astype(str))
    except FileNotFoundError:
        pass
    if not ids:
        raise ValueError(
            f"Aucun service actif trouvé pour {service_date.isoformat()}. "
            "Vérifier les fichiers de calendrier et la date demandée."
        )
    return ids


def programmed_speed(
    gtfs_path: Path,
    service_date: date,
    from_stop_id: str,
    to_stop_id: str,
    direction_id: str | None = None,
    route_id: str | None = None,
) -> pd.DataFrame:
    """Calcule la vitesse programmée par voyage entre deux arrêts, avec shape_dist_traveled."""
    services = active_service_ids(gtfs_path, service_date)
    trips = read_gtfs_table(
        gtfs_path,
        "trips.txt",
        dtype={"trip_id": str, "service_id": str, "route_id": str, "direction_id": str},
    )
    stop_times = read_gtfs_table(
        gtfs_path,
        "stop_times.txt",
        dtype={
            "trip_id": str,
            "stop_id": str,
            "arrival_time": str,
            "departure_time": str,
            "stop_sequence": int,
            "shape_dist_traveled": float,
        },
    )
    if "shape_dist_traveled" not in stop_times.columns:
        raise ValueError(
            "shape_dist_traveled est absent. Ce script exclut volontairement les distances "
            "reconstruites à partir de shapes.txt ; utiliser une version dédiée et documentée."
        )

    trips = trips.loc[trips["service_id"].isin(services)].copy()
    if direction_id is not None:
        trips = trips.loc[trips["direction_id"] == str(direction_id)].copy()
    if route_id is not None:
        trips = trips.loc[trips["route_id"] == str(route_id)].copy()

    selected = stop_times.merge(
        trips[["trip_id", "route_id", "direction_id"]],
        on="trip_id",
        how="inner",
        validate="many_to_one",
    )
    origin = selected.loc[selected["stop_id"] == str(from_stop_id)].copy()
    destination = selected.loc[selected["stop_id"] == str(to_stop_id)].copy()
    origin = origin.rename(
        columns={
            "stop_sequence": "origin_sequence",
            "departure_time": "origin_departure_time",
            "shape_dist_traveled": "origin_distance",
        }
    )
    destination = destination.rename(
        columns={
            "stop_sequence": "destination_sequence",
            "arrival_time": "destination_arrival_time",
            "shape_dist_traveled": "destination_distance",
        }
    )
    origin = origin[
        [
            "trip_id", "route_id", "direction_id", "origin_sequence",
            "origin_departure_time", "origin_distance",
        ]
    ]
    destination = destination[
        ["trip_id", "destination_sequence", "destination_arrival_time", "destination_distance"]
    ]

    result = origin.merge(destination, on="trip_id", how="inner", validate="one_to_one")
    result = result.loc[result["destination_sequence"] > result["origin_sequence"]].copy()
    if result.empty:
        raise ValueError(
            "Aucun voyage ne relie les deux arrêts dans cet ordre. Vérifier les arrêts, la direction et les variantes."
        )

    result["origin_seconds"] = result["origin_departure_time"].map(gtfs_time_to_seconds)
    result["destination_seconds"] = result["destination_arrival_time"].map(gtfs_time_to_seconds)
    result["scheduled_time_minutes"] = (result["destination_seconds"] - result["origin_seconds"]) / 60
    result["distance_native"] = result["destination_distance"] - result["origin_distance"]
    valid = (
        result["scheduled_time_minutes"].gt(0)
        & result["distance_native"].gt(0)
        & result["origin_distance"].notna()
        & result["destination_distance"].notna()
    )
    result = result.loc[valid].copy()
    if result.empty:
        raise ValueError(
            "Aucun voyage valide : vérifier la cohérence croissante de shape_dist_traveled et des heures GTFS."
        )

    result["distance_unit"] = "native_gtfs_unit"
    result["speed_native_unit_per_hour"] = result["distance_native"] / (result["scheduled_time_minutes"] / 60)
    return result[
        [
            "trip_id", "route_id", "direction_id", "origin_sequence", "destination_sequence",
            "origin_departure_time", "destination_arrival_time", "scheduled_time_minutes",
            "distance_native", "distance_unit", "speed_native_unit_per_hour",
        ]
    ].sort_values(["route_id", "trip_id"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calcule des vitesses commerciales programmées entre deux arrêts à partir de shape_dist_traveled."
    )
    parser.add_argument("--gtfs", required=True, type=Path, help="Dossier GTFS ou archive .zip")
    parser.add_argument("--date", required=True, help="Date de service au format AAAA-MM-JJ")
    parser.add_argument("--from-stop-id", required=True, help="Arrêt amont GTFS")
    parser.add_argument("--to-stop-id", required=True, help="Arrêt aval GTFS")
    parser.add_argument("--direction-id", help="Direction GTFS optionnelle")
    parser.add_argument("--route-id", help="Ligne GTFS optionnelle")
    parser.add_argument("--output", type=Path, help="Fichier CSV de sortie optionnel")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        service_date = datetime.strptime(args.date, "%Y-%m-%d").date()
    except ValueError as error:
        raise SystemExit("--date doit respecter le format AAAA-MM-JJ.") from error
    result = programmed_speed(
        gtfs_path=args.gtfs,
        service_date=service_date,
        from_stop_id=args.from_stop_id,
        to_stop_id=args.to_stop_id,
        direction_id=args.direction_id,
        route_id=args.route_id,
    )
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        result.to_csv(args.output, index=False)
    else:
        print(result.to_csv(index=False))


if __name__ == "__main__":
    main()
