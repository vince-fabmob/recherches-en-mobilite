import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from itineraire_artm import titre_artm, zones_itineraire


def test_panama_gare_centrale_bonaventure_montmorency():
    segments = [
        {"reseau": "REM", "origine": "Panama", "destination": "Gare Centrale"},
        {"reseau": "métro", "origine": "Bonaventure", "destination": "Montmorency"},
    ]

    assert zones_itineraire(segments) == ["B", "A", "B"]
    assert titre_artm(segments) == "Tous modes AB"
