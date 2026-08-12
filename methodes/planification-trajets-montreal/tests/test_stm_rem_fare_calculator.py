import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from stm_rem_fare_calculator import devis_trajet, lookup_zone, lowest_fare


def test_lookup_zone_resolves_municipality_and_alias():
    assert lookup_zone("Brossard") == "B"
    assert lookup_zone("Deux Montagnes") == "C"


def test_lookup_zone_resolves_stations_by_network():
    assert lookup_zone("Montmorency", reseau="métro") == "B"
    assert lookup_zone("Bonaventure", reseau="métro") == "A"
    assert lookup_zone("Panama", reseau="REM") == "B"
    assert lookup_zone("Saint-Jérôme", reseau="exo") == "C"


def test_lookup_zone_rejects_unknown_rem_station():
    with pytest.raises(ValueError, match="Station inconnue"):
        lookup_zone("Lieu inexistant", reseau="REM")


def test_brossard_to_deux_montagnes_uses_abc_one_trip():
    assert lowest_fare(["B", "A", "C"], trips=1)["cost_cents"] == 700


def test_devis_trajet_returns_display_ready_quote():
    result = devis_trajet("Brossard", "Deux-Montagnes", ["B", "A", "C"])
    assert result["couverture_requise"] == "ABC"
    assert result["titre_recommande"] == "un passage"
    assert result["cout_dollars"] == 7.0
