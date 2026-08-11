import json
from pathlib import Path


def load_bixi_rates(path=None):
    if path is None:
        path = Path(__file__).resolve().parents[1] / "donnees" / "tarifs-bixi.json"
    with open(path, encoding="utf-8") as source:
        return json.load(source)


def _money(value):
    return round(value + 1e-9, 2)


def calculate_bixi_fare(rates, membership, bike_type, segments_minutes):
    if membership not in {"member", "one_way"}:
        raise ValueError("membership must be 'member' or 'one_way'")
    if bike_type not in {"regular_bike", "electric_bike"}:
        raise ValueError("bike_type must be 'regular_bike' or 'electric_bike'")
    if not segments_minutes:
        raise ValueError("at least one segment is required")
    if any(minutes < 0 for minutes in segments_minutes):
        raise ValueError("segment duration must be non-negative")

    if membership == "member":
        pricing = rates["member_trip_pricing"][bike_type]
        if bike_type == "regular_bike":
            subtotal = sum(
                max(0, minutes - pricing["included_minutes_per_segment"]) * pricing["overage_rate_per_minute"]
                for minutes in segments_minutes
            )
        else:
            subtotal = sum(minutes * pricing["rate_per_minute"] for minutes in segments_minutes)
    else:
        pricing = rates["one_way_trip_pricing"]
        rate_key = f"{bike_type}_rate_per_minute"
        subtotal = sum(pricing["unlock_fee"] + minutes * pricing[rate_key] for minutes in segments_minutes)

    taxes = rates["taxes"]
    return {
        "mode": "bixi",
        "membership": membership,
        "bike_type": bike_type,
        "segments_minutes": segments_minutes,
        "cost_before_taxes": _money(subtotal),
        "tps": _money(subtotal * taxes["tps"]),
        "tvq": _money(subtotal * taxes["tvq"]),
        "cost_after_taxes": _money(subtotal * (1 + taxes["total"])),
        "confidence": "estimate",
        "verification_needed": ["bike availability at departure", "dock availability at arrival"],
    }
