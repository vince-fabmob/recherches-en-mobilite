import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from reseau_artm import correspondance_directe, zone_station


def test_zones_des_stations():
    assert zone_station("Panama", "REM") == "B"
    assert zone_station("Gare Centrale", "REM") == "A"
    assert zone_station("Bonaventure", "métro") == "A"
    assert zone_station("Montmorency", "métro") == "B"


def test_correspondance_gare_centrale_bonaventure():
    assert correspondance_directe("Gare Centrale", "REM", "Bonaventure", "métro") is True
    assert correspondance_directe("Panama", "REM", "Bonaventure", "métro") is False
