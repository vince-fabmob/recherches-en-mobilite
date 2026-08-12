"""Calculateur des tarifs Leo AutoPartage, avant taxes."""

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RATES_PATH = ROOT / "donnees" / "tarifs-leo.json"


def load_leo_rates(path: Path = RATES_PATH) -> dict:
    with path.open(encoding="utf-8") as source:
        return json.load(source)


def _money(cents: int) -> float:
    return round(cents / 100, 2)


def _best_hour_cost(remaining_minutes: int, rates: dict) -> int:
    if remaining_minutes <= 0:
        return 0
    packages = {int(hours) * 60: cents for hours, cents in rates["time_packages"]["hours"].items()}
    packages[30] = rates["time_packages"]["thirty_minutes_cents"]
    candidates = [
        cents + max(remaining_minutes - minutes, 0) * rates["time_packages"]["minute_rate_cents"]
        for minutes, cents in packages.items()
    ]
    return min(candidates + [remaining_minutes * rates["time_packages"]["minute_rate_cents"]])


def _best_day_cost(duration_minutes: int, rates: dict) -> int:
    remaining = duration_minutes
    cost = 0
    for days, cents in sorted(((int(days), cents) for days, cents in rates["time_packages"]["days"].items()), reverse=True):
        count, remaining = divmod(remaining, days * 24 * 60)
        cost += count * cents
    return cost + _best_hour_cost(remaining, rates)


def calculate_leo_fare(duration_minutes: int, distance_km: float = 0, parking: str = "leo_zone", rates: dict | None = None) -> dict:
    """Retourne un devis Leo avant taxes; refuse un surplus kilométrique non documenté."""
    if duration_minutes < 1:
        raise ValueError("duration_minutes must be at least 1")
    if distance_km < 0:
        raise ValueError("distance_km must be non-negative")
    rates = rates or load_leo_rates()
    if parking not in rates["parking"]:
        raise ValueError(f"Unknown parking option: {parking}")
    included_km = math.ceil(duration_minutes / (24 * 60)) * rates["distance"]["included_km_per_day"]
    excess_km = max(distance_km - included_km, 0)
    excess_rate = rates["distance"]["excess_rate_cents_per_km"]
    if excess_km and excess_rate is None:
        raise ValueError("Leo excess-kilometre rate is not confirmed; quote cannot be completed.")
    time_cents = _best_day_cost(duration_minutes, rates)
    distance_cents = round(excess_km * excess_rate) if excess_km else 0
    access_cents = rates["per_trip_fees"]["access_cents"]
    insurance_cents = rates["per_trip_fees"]["insurance_cents"]
    parking_cents = rates["parking"][parking]
    before_taxes_cents = time_cents + distance_cents + access_cents + insurance_cents + parking_cents
    return {
        "mode": "leo",
        "duration_minutes": duration_minutes,
        "distance_km": distance_km,
        "included_km": included_km,
        "time_cost": _money(time_cents),
        "distance_cost": _money(distance_cents),
        "access_fee": _money(access_cents),
        "insurance_fee": _money(insurance_cents),
        "parking_cost": _money(parking_cents),
        "before_taxes": _money(before_taxes_cents),
        "taxes_included": False
    }
