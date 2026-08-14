"""
Statut : implémentation reproductible indicative d'une méthode établie
Référence : General Transit Feed Specification Reference, MobilityData ;
Transit Capacity and Quality of Service Manual (TCQSM), Transportation Research Board.
Données : GTFS statique — trips.txt, stop_times.txt, calendar.txt et/ou calendar_dates.txt.
Sortie : nombre de voyages programmés par heure à un arrêt donné, par direction optionnelle.
Hypothèses : un passage est compté selon departure_time si disponible, sinon arrival_time ;
une fenêtre horaire est [HH:00:00, HH+1:00:00[ ; les résultats décrivent l'offre planifiée.
Validation : comparer avec AVL/GPS ou GTFS-Realtime pour mesurer l'exploitation réelle.
Limites : ne mesure pas retards, annulations, charge, capacité, régularité effective ni détournements.
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
    if minutes not in range(60) or seconds not in range(60) or hours < 0:
        raise ValueError(f"Heure GTFS invalide : {value}")
    return hours * 3600 + minutes * 60 + seconds


def active_service_ids(gtfs_path: Path, service_date: date) -> set[str]:
    """Retourne les service_id actifs à une date selon calendar et calendar_dates."""
    ids: set[str] = set()
    weekday = service_date.strftime("%A").lower()

    try:
        calendar = read_gtfs_table(gtfs_path, "calendar.txt", dtype={"service_id": str})
        calendar["start_date"] = pd.to_datetime(calendar["start_date"], format="%Y%m%d").dt.date
        calendar["end_date"] = pd.to_datetime(calendar["end_date"], format="%Y%m%d").dt.date
        valid = calendar.loc[
            (calendar["start_date"] <= service_date)
            & (calendar["end_date"] >= service_date)
            & (calendar[weekday] == 1),
            "service_id",
        ]
        ids.update(valid.astype(str))
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
            "Vérifier calendar.txt, calendar_dates.txt et la date demandée."
        )
    return ids


def hourly_scheduled_trips(
    gtfs_path: Path,
    service_date: date,
    stop_id: str,
    start_hour: int,
    end_hour: int,
    direction_id: str | None = None,
) -> pd.DataFrame:
    """Compte les voyages programmés par heure pour un arrêt et une date de service."""
    if not 0 <= start_hour < end_hour <= 48:
        raise ValueError("Les heures doivent respecter 0 <= start < end <= 48.")

    services = active_service_ids(gtfs_path, service_date)
    trips = read_gtfs_table(
        gtfs_path,
        "trips.txt",
        dtype={"trip_id": str, "service_id": str, "direction_id": str, "route_id": str},
    )
    stop_times = read_gtfs_table(
        gtfs_path,
        "stop_times.txt",
        dtype={"trip_id": str, "stop_id": str, "arrival_time": str, "departure_time": str},
    )

    trips = trips.loc[trips["service_id"].isin(services)].copy()
    if direction_id is not None:
        trips = trips.loc[trips["direction_id"] == str(direction_id)].copy()

    passages = stop_times.loc[stop_times["stop_id"] == str(stop_id)].copy()
    passages = passages.merge(
        trips[["trip_id", "route_id", "service_id", "direction_id"]],
        on="trip_id",
        how="inner",
        validate="many_to_one",
    )
    if passages.empty:
        raise ValueError("Aucun passage trouvé : vérifier stop_id, date de service et direction_id.")

    passages["event_time"] = passages["departure_time"].where(
        passages["departure_time"].notna() & (passages["departure_time"].str.strip() != ""),
        passages["arrival_time"],
    )
    passages["seconds"] = passages["event_time"].map(gtfs_time_to_seconds)
    passages["hour"] = passages["seconds"] // 3600

    selected = passages.loc[(passages["hour"] >= start_hour) & (passages["hour"] < end_hour)].copy()
    grouped = (
        selected.groupby(["hour", "route_id"], dropna=False)["trip_id"]
        .nunique()
        .rename("voyages_programmes")
        .reset_index()
    )

    all_hours = pd.DataFrame({"hour": range(start_hour, end_hour)})
    totals = (
        selected.groupby("hour")["trip_id"]
        .nunique()
        .rename("voyages_programmes_total")
        .reset_index()
    )
    totals = all_hours.merge(totals, on="hour", how="left").fillna({"voyages_programmes_total": 0})
    totals["voyages_programmes_total"] = totals["voyages_programmes_total"].astype(int)

    return grouped.merge(totals, on="hour", how="right").sort_values(["hour", "route_id"], na_position="last")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compte les voyages programmés par heure à un arrêt GTFS pour une date de service."
    )
    parser.add_argument("--gtfs", required=True, type=Path, help="Dossier GTFS ou archive .zip")
    parser.add_argument("--date", required=True, help="Date de service au format AAAA-MM-JJ")
    parser.add_argument("--stop-id", required=True, help="Identifiant GTFS de l’arrêt")
    parser.add_argument("--start-hour", type=int, default=0, help="Première heure incluse (défaut : 0)")
    parser.add_argument("--end-hour", type=int, default=30, help="Première heure exclue (défaut : 30)")
    parser.add_argument("--direction-id", help="Direction GTFS optionnelle")
    parser.add_argument("--output", type=Path, help="Fichier CSV de sortie optionnel")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        service_date = datetime.strptime(args.date, "%Y-%m-%d").date()
    except ValueError as error:
        raise SystemExit("--date doit respecter le format AAAA-MM-JJ.") from error

    result = hourly_scheduled_trips(
        gtfs_path=args.gtfs,
        service_date=service_date,
        stop_id=args.stop_id,
        start_hour=args.start_hour,
        end_hour=args.end_hour,
        direction_id=args.direction_id,
    )

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        result.to_csv(args.output, index=False)
    else:
        print(result.to_csv(index=False))


if __name__ == "__main__":
    main()
