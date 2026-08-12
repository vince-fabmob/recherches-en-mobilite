"""Calculateur minimal pour les titres Tous modes STM-REM."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FARES_PATH = ROOT / "donnees" / "tarifs-stm-rem.json"


def fare_zone_key(traversed_zones: list[str]) -> str:
    """Retourne la couverture Tous modes minimale pour les zones traversées."""
    zones = set(traversed_zones)
    if not zones or not zones.issubset({"A", "B", "C", "D"}):
        raise ValueError("traversed_zones must contain one or more zones from A to D")
    if "D" in zones:
        return "ABCD"
    if "C" in zones:
        return "ABC"
    if "B" in zones:
        return "AB" if "A" in zones else "AB"
    return "A"


def load_fares(path: Path = FARES_PATH) -> dict:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def lowest_fare(
    traversed_zones: list[str],
    trips: int,
    profile: str = "regular",
    within_24_hours: bool = False,
    fares: dict | None = None,
) -> dict:
    """Sélectionne le titre valide le moins cher pour un déplacement Tous modes."""
    if trips < 1:
        raise ValueError("trips must be at least 1")

    fares = fares or load_fares()
    zone_key = fare_zone_key(traversed_zones)
    products = fares["all_modes"][zone_key]
    candidates = []

    for product_name in ("one_trip", "two_trips", "ten_trips"):
        product = products.get(product_name, {})
        price = product.get(profile)
        capacity = {"one_trip": 1, "two_trips": 2, "ten_trips": 10}[product_name]
        if price is not None and trips % capacity == 0:
            candidates.append({
                "product": product_name,
                "quantity": trips // capacity,
                "cost_cents": price * (trips // capacity),
                "zone_key": zone_key,
            })

    if within_24_hours and profile == "regular" and "24_hours" in products:
        price = products["24_hours"].get("regular")
        if price is not None:
            candidates.append({
                "product": "24_hours",
                "quantity": 1,
                "cost_cents": price,
                "zone_key": zone_key,
            })

    if not candidates:
        raise ValueError("No eligible fare product for this profile and trip count")
    return min(candidates, key=lambda candidate: candidate["cost_cents"])
