"""Accès au référentiel unifié du réseau ARTM."""

import json
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEAU_PATH = ROOT / "donnees" / "reseau-artm.json"
NETWORK_ALIASES = {"metro": "metro", "métro": "metro", "rem": "rem", "exo": "exo_train", "train": "exo_train"}


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    return value.lower().replace("'", " ").replace("-", " ").replace("–", " ").strip()


def load_reseau(path: Path = RESEAU_PATH) -> dict:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def network_key(reseau: str) -> str:
    key = NETWORK_ALIASES.get(normalize(reseau))
    if not key:
        raise ValueError(f"Réseau inconnu: {reseau}")
    return key


def zone_station(station: str, reseau: str, data: dict | None = None) -> str:
    """Retourne la zone ARTM d'une station sur le réseau indiqué."""
    data = data or load_reseau()
    network = network_key(reseau)
    station_key = normalize(station)
    if network == "metro":
        for name in data["networks"]["metro"]["zone_b_stations"]:
            if normalize(name) == station_key:
                return "B"
        return data["networks"]["metro"]["default_zone"]
    for zone, stations in data["networks"][network].items():
        if any(normalize(name) == station_key for name in stations):
            return zone
    raise ValueError(f"Station inconnue sur le réseau {reseau}: {station}")


def correspondance_directe(depart: str, reseau_depart: str, arrivee: str, reseau_arrivee: str, data: dict | None = None) -> bool:
    """Indique si deux stations sont reliées par une correspondance définie."""
    data = data or load_reseau()
    start = (normalize(depart), network_key(reseau_depart))
    end = (normalize(arrivee), network_key(reseau_arrivee))
    for link in data["correspondances"]:
        source = (normalize(link["from"]["station"]), link["from"]["network"])
        target = (normalize(link["to"]["station"]), link["to"]["network"])
        if (start, end) in ((source, target), (target, source)):
            return True
    return False
