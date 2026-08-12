import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from leo_fare_calculator import calculate_leo_fare, load_leo_rates


RATES = load_leo_rates(Path(__file__).resolve().parents[1] / "donnees" / "tarifs-leo.json")


def test_official_32_minute_example():
    result = calculate_leo_fare(32, distance_km=10, rates=RATES)

    assert result["time_cost"] == 10.36
    assert result["before_taxes"] == 13.84
    assert result["included_km"] == 75


def test_official_two_days_two_hours_two_minutes_example():
    result = calculate_leo_fare(2 * 24 * 60 + 2 * 60 + 2, distance_km=150, rates=RATES)

    assert result["time_cost"] == 142.86
    assert result["before_taxes"] == 146.34
    assert result["included_km"] == 150


def test_downtown_parking_is_added():
    result = calculate_leo_fare(30, parking="downtown_cents", rates=RATES)

    assert result["parking_cost"] == 5.90
    assert result["before_taxes"] == 18.88
