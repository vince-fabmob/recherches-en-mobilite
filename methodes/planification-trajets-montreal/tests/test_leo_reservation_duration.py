from datetime import datetime

LEO_UNLOCK_FEE = 1.49
LEO_INSURANCE_FEE = 1.99
LEO_TWO_DAY_RATE = 118.00
LEO_TWO_DAY_INCLUDED_KM = 150
LEO_EXTRA_KM_RATE = 0.32


def reservation_hours(start: datetime, end: datetime) -> float:
    return (end - start).total_seconds() / 3600


def leo_two_day_total_before_tax(km: float) -> float:
    extra_km = max(0, km - LEO_TWO_DAY_INCLUDED_KM)
    return round(
        LEO_UNLOCK_FEE
        + LEO_INSURANCE_FEE
        + LEO_TWO_DAY_RATE
        + extra_km * LEO_EXTRA_KM_RATE,
        2,
    )


def test_rawdon_weekend_duration_is_46_hours_not_54_hours():
    start = datetime(2026, 8, 14, 14, 0)
    end = datetime(2026, 8, 16, 12, 0)

    assert reservation_hours(start, end) == 46
    assert reservation_hours(start, end) < 48


def test_rawdon_weekend_two_day_leo_quote_matches_official_calculator():
    assert leo_two_day_total_before_tax(160) == 124.68
