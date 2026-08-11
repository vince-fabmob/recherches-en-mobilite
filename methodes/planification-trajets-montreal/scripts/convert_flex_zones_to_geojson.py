import json
import sys
from datetime import datetime, timezone
from pathlib import Path

source = Path(sys.argv[1])
target = Path(sys.argv[2])
with source.open(encoding="utf-8") as fh:
    payload = json.load(fh)

features = []
for zone in payload["zones"]:
    coordinates = zone["coordinates"]
    if coordinates[0] != coordinates[-1]:
        coordinates.append(coordinates[0])
    features.append({
        "type": "Feature",
        "properties": {key: zone.get(key) for key in ["zone_id", "name", "description", "type", "ride_allowed", "parking_allowed", "centroid"]},
        "geometry": {"type": "Polygon", "coordinates": [coordinates]}
    })

geojson = {"type": "FeatureCollection", "name": "communauto_flex_zones", "generated_at": datetime.now(timezone.utc).isoformat(), "features": features}
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(geojson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
