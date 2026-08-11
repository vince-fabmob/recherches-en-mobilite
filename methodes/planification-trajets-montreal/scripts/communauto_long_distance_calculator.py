import json
import math
from datetime import datetime
from pathlib import Path


def load_long_distance_rates(path=None):
    if path is None:
        path = Path(__file__).resolve().parents[1] / "donnees" / "tarifs-communauto-longue-distance.json"
    with open(path, encoding="utf-8") as source:
        return json.load(source)


def _money(value):
    return round(value + 1e-9, 2)


def _season(start):
    key = (start.month, start.day)
    return "high" if (6, 15) <= key <= (10, 15) else "low"


def calculate_long_distance(rates, plan_id, start, end, distance_km):
    if isinstance(start, str):
        start = datetime.fromisoformat(start)
    if isinstance(end, str):
        end = datetime.fromisoformat(end)
    if end <= start:
        raise ValueError("end must be after start")
    config = rates["long_distance"]
    if plan_id not in config["eligible_plans"]:
        raise ValueError(f"plan is not eligible for long distance: {plan_id}")
    if distance_km < 0:
        raise ValueError("distance_km must be non-negative")
    season_name = _season(start)
    season = config["seasons"][season_name]
    duration_hours = (end - start).total_seconds() / 3600
    first_day = min(duration_hours, 24)
    time_cost = season["first_day_rate"]
    remaining_hours = max(duration_hours - first_day, 0)
    additional_days = math.ceil(remaining_hours / 24)
    for day in range(additional_days):
        hours = min(max(remaining_hours - day * 24, 0), 24)
        time_cost += min(hours * config["excess_hour_rate"], season["additional_day_rate"])
    full_weeks, remaining_days = divmod(math.ceil(duration_hours / 24), 7)
    weekly_candidate = full_weeks * season["weekly_rate"]
    if remaining_days:
        weekly_candidate += season["first_day_rate"] + max(remaining_days - 1, 0) * season["additional_day_rate"]
    time_cost = min(time_cost, weekly_candidate)
    distance_cost = min(distance_km, season["distance_rate_until_km"]) * season["distance_rate"]
    distance_cost += max(distance_km - season["distance_rate_after_km"], 0) * season["distance_rate_after_threshold"]
    subtotal = time_cost + distance_cost
    taxes = rates["metadata"].get("taxes", {"tps": 0.05, "tvq": 0.09975})
    return {
        "mode": "long_distance",
        "season": season_name,
        "duration_hours": _money(duration_hours),
        "time_cost": _money(time_cost),
        "distance_cost": _money(distance_cost),
        "before_taxes": _money(subtotal),
        "tps": _money(subtotal * taxes["tps"]),
        "tvq": _money(subtotal * taxes["tvq"]),
        "total": _money(subtotal * (1 + taxes["tps"] + taxes["tvq"])),
    }
