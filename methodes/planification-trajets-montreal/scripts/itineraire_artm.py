"""Construction et validation d’itinéraires à partir du référentiel ARTM."""

from reseau_artm import correspondance_directe, zone_station


def zones_itineraire(segments: list[dict]) -> list[str]:
    """Retourne la séquence de zones et valide les correspondances entre segments."""
    if not segments:
        raise ValueError("Un itinéraire doit contenir au moins un segment.")

    zones: list[str] = []
    previous = None
    for segment in segments:
        required = {"reseau", "origine", "destination"}
        if not required <= segment.keys():
            raise ValueError("Chaque segment doit préciser reseau, origine et destination.")
        if previous and not correspondance_directe(
            previous["destination"], previous["reseau"], segment["origine"], segment["reseau"]
        ):
            raise ValueError(
                f"Correspondance non définie: {previous['destination']} → {segment['origine']}."
            )
        start_zone = zone_station(segment["origine"], segment["reseau"])
        end_zone = zone_station(segment["destination"], segment["reseau"])
        if not zones or zones[-1] != start_zone:
            zones.append(start_zone)
        if zones[-1] != end_zone:
            zones.append(end_zone)
        previous = segment
    return zones


def titre_artm(segments: list[dict]) -> str:
    """Détermine le titre tous-modes minimal à partir des zones parcourues."""
    zones = set(zones_itineraire(segments))
    if zones <= {"A"}:
        return "Tous modes A"
    if zones <= {"A", "B"}:
        return "Tous modes AB"
    if zones <= {"A", "B", "C"}:
        return "Tous modes ABC"
    return "Tous modes ABCD"
