"""Extraction des zones ARTM à partir d'étapes d'itinéraire indépendantes d'un fournisseur."""

from stm_rem_fare_calculator import devis_trajet, lookup_zone


def extraire_zones_itineraire(etapes: list[dict]) -> dict:
    if not etapes:
        raise ValueError("etapes must contain at least one itinerary step")
    zones_traversees = []
    modes = []
    for index, etape in enumerate(etapes):
        try:
            origine = etape["origine"]
            destination = etape["destination"]
            mode = etape["mode"]
        except KeyError as error:
            raise ValueError(f"Missing itinerary field: {error.args[0]}") from error
        zone_origine = lookup_zone(origine, reseau=mode)
        zone_destination = lookup_zone(destination, reseau=mode)
        if index == 0:
            zones_traversees.append(zone_origine)
        elif zones_traversees[-1] != zone_origine:
            raise ValueError("Itinerary steps must connect through the same ARTM zone")
        if zones_traversees[-1] != zone_destination:
            zones_traversees.append(zone_destination)
        if mode not in modes:
            modes.append(mode)
    return {"origine": etapes[0]["origine"], "destination": etapes[-1]["destination"], "zones_traversees": zones_traversees, "modes": modes}


def devis_depuis_itineraire(etapes: list[dict], deplacements: int = 1, profil: str = "ordinaire", dans_24_heures: bool = False) -> dict:
    itineraire = extraire_zones_itineraire(etapes)
    devis = devis_trajet(origine=itineraire["origine"], destination=itineraire["destination"], zones_traversees=itineraire["zones_traversees"], deplacements=deplacements, profil=profil, dans_24_heures=dans_24_heures)
    return {**devis, "modes": itineraire["modes"]}
