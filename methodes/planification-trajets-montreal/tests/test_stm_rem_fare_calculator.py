import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from stm_rem_fare_calculator import devis_trajet, lookup_zone, lowest_fare


def test_lookup_zone_resolves_municipality_and_alias():
    assert lookup_zone("Brossard") == "B"
    assert lookup_zone("Deux-Montagnes") == "C"
    assert lookup_zone("Deux Montagnes") == "C"


def test_lookup_zone_resolves_station_override():
    assert lookup_zone("Station Brossard") == "B"


def test_lookup_zone_rejects_unknown_place():
    with pytest.raises(ValueError, match="Unknown ARTM place"):
        lookup_zone("Lieu inexistant")


def test_brossard_to_deux_montagnes_uses_abc_one_trip():
    result = lowest_fare(["B", "A", "C"], trips=1)

    assert result == {
        "product": "one_trip",
        "quantity": 1,
        "cost_cents": 700,
        "zone_key": "ABC",
    }


def test_brossard_to_montreal_return_uses_ab_two_trips():
    result = lowest_fare(["B", "A"], trips=2)

    assert result == {
        "product": "two_trips",
        "quantity": 1,
        "cost_cents": 975,
        "zone_key": "AB",
    }


def test_four_zone_a_trips_in_24_hours_selects_day_pass():
    result = lowest_fare(["A"], trips=4, within_24_hours=True)

    assert result == {
        "product": "24_hours",
        "quantity": 1,
        "cost_cents": 1125,
        "zone_key": "A",
    }


def test_reduced_profile_does_not_select_regular_day_pass():
    result = lowest_fare(["A"], trips=4, profile="reduced_6_17", within_24_hours=True)

    assert result == {
        "product": "two_trips",
        "quantity": 2,
        "cost_cents": 1000,
        "zone_key": "A",
    }


def test_devis_trajet_returns_display_ready_quote():
    result = devis_trajet(
        origine="Brossard",
        destination="Deux-Montagnes",
        zones_traversees=["B", "A", "C"],
    )

    assert result == {
        "origine": "Brossard",
        "destination": "Deux-Montagnes",
        "zone_origine": "B",
        "zone_destination": "C",
        "zones_traversees": ["B", "A", "C"],
        "couverture_requise": "ABC",
        "titre_recommande": "un passage",
        "quantite": 1,
        "cout_cents": 700,
        "cout_dollars": 7.0,
    }
