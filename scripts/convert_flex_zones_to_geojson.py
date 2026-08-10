import json
from datetime import datetime, timezone
from pathlib import Path

source = Path("data/communauto_flex_zones.json")
target = Path("data/communauto_flex_zones.geojson")

with source.open(encoding="utf-8") as fh:
    payload = json.load(fh)

features = []
for zone in payload["zones"]:
    coordinates = zone["coordinates"]
    if coordinates[0] != coordinates[-1]:
        coordinates.append(coordinates[0])
    features.append({
        "type": "Feature",
        "properties": {
            "zone_id": zone["zone_id"],
            "name": zone["name"],
            "description": zone.get("description"),
            "type": zone.get("type", "service_area"),
            "ride_allowed": zone.get("ride_allowed", True),
            "parking_allowed": zone.get("parking_allowed", True),
            "centroid": zone.get("centroid"),
            "source": payload.get("metadata", {}).get("source_originale"),
            "source_last_updated_epoch": payload.get("metadata", {}).get("last_updated_epoch")
        },
        "geometry": {"type": "Polygon", "coordinates": [coordinates]}
    })

geojson = {
    "type": "FeatureCollection",
    "name": "communauto_flex_zones",
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "features": features
}

target.parent.mkdir(parents=True, exist_ok=True)
with target.open("w", encoding="utf-8") as fh:
    json.dump(geojson, fh, ensure_ascii=False, indent=2)
    fh.write("\n")
