import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from itineraire_zones import devis_depuis_itineraire, extraire_zones_itineraire


ETAPES_BROSSARD_DEUX_MONTAGNES = [
    {"mode": "REM", "origine": "Brossard", "destination": "Montréal"},
    {"mode": "métro", "origine": "Montréal", "destination": "Montréal"},
    {"mode": "train", "origine": "Montréal", "destination": "Deux-Montagnes"},
]


def test_extraire_zones_itineraire_returns_ordered_zones_and_modes():
    result = extraire_zones_itineraire(ETAPES_BROSSARD_DEUX_MONTAGNES)

    assert result == {
        "origine": "Brossard",
        "destination": "Deux-Montagnes",
        "zones_traversees": ["B", "A", "C"],
        "modes": ["REM", "métro", "train"],
    }


def test_devis_depuis_itineraire_returns_abc_quote():
    result = devis_depuis_itineraire(ETAPES_BROSSARD_DEUX_MONTAGNES)

    assert result["couverture_requise"] == "ABC"
    assert result["titre_recommande"] == "un passage"
    assert result["cout_cents"] == 700
    assert result["cout_dollars"] == 7.0
    assert result["modes"] == ["REM", "métro", "train"]


def test_extraire_zones_itineraire_rejects_disconnected_steps():
    etapes = [
        {"mode": "REM", "origine": "Brossard", "destination": "Montréal"},
        {"mode": "train", "origine": "Laval", "destination": "Deux-Montagnes"},
    ]

    with pytest.raises(ValueError, match="must connect"):
        extraire_zones_itineraire(etapes)
