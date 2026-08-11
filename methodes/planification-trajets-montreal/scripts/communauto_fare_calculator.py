import json
import math
from pathlib import Path


def load_rates(path=None):
    if path is None:
        path = Path(__file__).resolve().parents[1] / "donnees" / "tarifs-communauto.json"
    with open(path, encoding="utf-8") as source:
        return json.load(source)


def _money(value):
    return round(value + 1e-9, 2)


def _distance_cost(distance_km, included_km, base_rate, threshold_km, reduced_rate):
    if distance_km < 0:
        raise ValueError("distance_km must be non-negative")
    if distance_km <= included_km:
        return 0.0
    billable = distance_km - included_km
    if threshold_km is None or reduced_rate is None or billable <= threshold_km:
        return billable * base_rate
    return threshold_km * base_rate + (billable - threshold_km) * reduced_rate


def _with_taxes(subtotal, taxes):
    return {
        "before_taxes": _money(subtotal),
        "tps": _money(subtotal * taxes["tps"]),
        "tvq": _money(subtotal * taxes["tvq"]),
        "total": _money(subtotal * (1 + taxes["total"])),
    }


def calculate_flex(rates, duration_minutes, distance_km):
    if duration_minutes < 0:
        raise ValueError("duration_minutes must be non-negative")
    flex = rates["flex_base"]
    time_cost = min(
        duration_minutes * flex["minute_rate"],
        math.ceil(duration_minutes / 60) * flex["hourly_cap"],
        math.ceil(duration_minutes / 1440) * flex["daily_cap"],
    )
    distance_cost = _distance_cost(
        distance_km,
        flex["included_distance_km"],
        flex["distance_rate_after_included_km"],
        None,
        None,
    )
    result = _with_taxes(time_cost + distance_cost, rates["taxes"])
    result.update({"mode": "flex", "time_cost": _money(time_cost), "distance_cost": _money(distance_cost)})
    return result


def calculate_station(rates, plan_id, duration_minutes, distance_km, weekend=False):
    if duration_minutes < 0:
        raise ValueError("duration_minutes must be non-negative")
    try:
        station = rates["plans"][plan_id]["station"]
    except KeyError as error:
        raise ValueError(f"unknown plan: {plan_id}") from error
    if duration_minutes > 1440 and station["additional_day_rate"] is None:
        raise ValueError("additional-day station rate is unavailable for this plan")
    hourly_rate = station["hourly_rate"] + (station.get("weekend_hourly_surcharge", 0) if weekend else 0)
    daily_cap = station["first_day_cap"] + (station.get("weekend_daily_surcharge", 0) if weekend else 0)
    time_cost = min(duration_minutes / 60 * hourly_rate, daily_cap)
    distance_cost = _distance_cost(
        distance_km,
        station["included_distance_km"],
        station["distance_rate"],
        station["distance_rate_after_km"],
        station["distance_rate_after_threshold"],
    )
    result = _with_taxes(time_cost + distance_cost, rates["taxes"])
    result.update({"mode": "station", "plan": plan_id, "time_cost": _money(time_cost), "distance_cost": _money(distance_cost)})
    return result


def calculate_best_eligible_rate(rates, plan_id, duration_minutes, distance_km, weekend=False):
    flex = calculate_flex(rates, duration_minutes, distance_km)
    plan = rates["plans"].get(plan_id)
    if plan is None:
        raise ValueError(f"unknown plan: {plan_id}")
    if not plan["flex"]["eligible_for_station_rate_if_lower"]:
        flex["selected_by"] = "flex_only"
        return flex
    station = calculate_station(rates, plan_id, max(duration_minutes, 240), distance_km, weekend)
    selected = min((flex, station), key=lambda item: item["before_taxes"])
    selected = dict(selected)
    selected["selected_by"] = "lowest_eligible_rate"
    selected["alternatives"] = {"flex": flex["before_taxes"], "station_comparison": station["before_taxes"]}
    return selected
