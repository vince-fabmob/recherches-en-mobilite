# Pack de données mobilité — Californie

Ce pack initialise les données de recharge, stationnement, règles de bordure (« curb ») et mobilité à la demande pour le planificateur.

## Emplacement cible dans le dépôt

```text
methodes/planification-trajets-montreal/donnees/us/
```

## Arborescence

```text
us/
├── README.md
├── california/
│   ├── ev_charging_network.json
│   └── ev_charging_sources.json
├── san-francisco/
│   ├── parking.json
│   ├── curb_rules.json
│   ├── on_demand_mobility.json
│   └── sources.json
└── los-angeles/
    ├── parking.json
    ├── curb_rules.json
    ├── on_demand_mobility.json
    └── sources.json
```

---

## `README.md`

```md
# Données de mobilité — États-Unis

Cette structure complète le planificateur multimodal avec des données de mobilité à la demande, stationnement, curb et recharge.

## Organisation

- `california/ev_charging_network.json` : registre normalisé des bornes de recharge; les stations sont partagées entre villes pour éviter la duplication.
- `san-francisco/parking.json` et `los-angeles/parking.json` : garages, lots, P+R et zones de stationnement.
- `*/curb_rules.json` : règles localisées pour stationnement, chargement, arrêts et dépose VTC/robotaxi.
- `*/on_demand_mobility.json` : fournisseurs robotaxi et VTC, avec statut, modèle de réservation et exigences de validation.
- `*/sources.json` : provenance, format, conditions d'accès et date de vérification.

## Principes de données

1. Ne pas générer de tarif, disponibilité ou géorepérage non publié. Employer `null`, `unknown` ou `verification_required: true`.
2. Distinguer `driverless`, `safety_driver`, `teledriven_delivery` et `human_driver`.
3. Conserver les prix de stationnement distincts des prix de recharge.
4. Joindre une borne à un stationnement par `station_ids`, sans dupliquer sa fiche technique.
5. Pour les prix de type devis dynamique, afficher `app_quote_required: true`.
6. Toute donnée exploitable doit avoir une URL de source et `verified_at`.

## Calcul de coût

`cout_total = cout_stationnement + cout_recharge + frais_occupation + cout_detour`

La disponibilité du stationnement sur rue ne doit jamais être présentée comme garantie en l'absence de donnée temps réel officielle.
```

---

## `california/ev_charging_network.json`

```json
{
  "schema_version": "1.0.0",
  "region_id": "california",
  "name": "California EV charging network",
  "currency": "USD",
  "last_refreshed": null,
  "stations": [],
  "station_schema": {
    "id": "provider_station_id",
    "name": "string",
    "coordinates": {
      "longitude": null,
      "latitude": null
    },
    "address": {
      "city": "string",
      "state": "CA",
      "postal_code": "string"
    },
    "operator": "string",
    "network": "string",
    "access": {
      "public": null,
      "hours": null,
      "parking_restrictions": null
    },
    "chargers": [
      {
        "connector": "NACS|CCS1|J1772|CHAdeMO|other",
        "power_kw": null,
        "current_type": "AC|DC|unknown",
        "ports_total": null,
        "ports_available": null,
        "status": "available|occupied|out_of_service|unknown"
      }
    ],
    "pricing": {
      "model": "per_kwh|per_minute|session|dynamic_quote|unknown",
      "price_usd_per_kwh": null,
      "price_usd_per_min": null,
      "idle_fee_usd_per_min": null,
      "app_quote_required": true
    },
    "data_quality": {
      "source_type": "official_api|official_web|public_registry|third_party",
      "realtime": false,
      "verified_at": null,
      "source_url": null
    }
  }
}
```

## `california/ev_charging_sources.json`

```json
{
  "schema_version": "1.0.0",
  "region_id": "california",
  "sources": [
    {
      "id": "california_energy_commission",
      "name": "California Energy Commission / California Open Data",
      "coverage": "California public and planned EV charging datasets",
      "url": "https://data.ca.gov/",
      "format": "ArcGIS|CSV|GeoJSON|varies",
      "realtime": false,
      "authentication_required": false,
      "verified_at": null,
      "notes": "Inspect the current dataset and licence before automated ingestion."
    },
    {
      "id": "alternative_fuel_stations",
      "name": "Alternative Fuel Stations registry",
      "coverage": "United States EV charging stations",
      "url": "https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/",
      "format": "API",
      "realtime": false,
      "authentication_required": true,
      "verified_at": null,
      "notes": "API key and terms of use must be reviewed before ingestion."
    }
  ]
}
```

---

## `san-francisco/parking.json`

```json
{
  "schema_version": "1.0.0",
  "city_id": "san-francisco-ca",
  "currency": "USD",
  "last_refreshed": null,
  "parking_facilities": [],
  "facility_schema": {
    "id": "string",
    "name": "string",
    "category": "garage|lot|park_and_ride|on_street_zone|other",
    "operator": "string",
    "coordinates": [null, null],
    "capacity": null,
    "access": {
      "public": null,
      "hours": null,
      "reservation_supported": null
    },
    "pricing": {
      "model": "hourly|daily|event|metered|dynamic|unknown",
      "rates": [],
      "quote_required": false,
      "verified_at": null
    },
    "availability": {
      "spaces_available": null,
      "realtime": false,
      "observed_at": null
    },
    "ev_charging": {
      "station_ids": [],
      "parking_payment_required": null
    },
    "source": {
      "url": null,
      "verified_at": null,
      "confidence": "official|third_party|unknown"
    }
  }
}
```

## `san-francisco/curb_rules.json`

```json
{
  "schema_version": "1.0.0",
  "city_id": "san-francisco-ca",
  "last_refreshed": null,
  "rules": [],
  "rule_schema": {
    "id": "string",
    "geometry": {
      "type": "LineString|Point|Polygon",
      "coordinates": []
    },
    "use": "parking|loading|pickup_dropoff|transit|bike|accessible|no_stopping|other",
    "vehicle_classes": [],
    "days_of_week": [],
    "start_time": null,
    "end_time": null,
    "max_stay_minutes": null,
    "permit_required": null,
    "fee": {
      "amount_usd": null,
      "unit": "hour|session|unknown"
    },
    "enforcement_notes": null,
    "source_url": null,
    "verified_at": null,
    "confidence": "official|third_party|unknown"
  }
}
```

## `san-francisco/on_demand_mobility.json`

```json
{
  "schema_version": "1.0.0",
  "city_id": "san-francisco-ca",
  "timezone": "America/Los_Angeles",
  "last_refreshed": null,
  "providers": [
    {
      "id": "waymo",
      "name": "Waymo",
      "category": "robotaxi",
      "automation_type": "driverless",
      "availability_status": "active",
      "booking": {
        "channel": "mobile_app",
        "api_public": false,
        "quote_type": "in_app_before_booking"
      },
      "service_area": {
        "type": "geofence_polygon",
        "geojson_path": null,
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
        "public_formula": null,
        "app_quote_required": true
      },
      "source_url": "https://support.google.com/waymo/answer/9059119",
      "verified_at": null
    },
    {
      "id": "zoox",
      "name": "Zoox",
      "category": "robotaxi",
      "automation_type": "driverless",
      "availability_status": "verify_access_or_waitlist",
      "booking": {
        "channel": "mobile_app",
        "api_public": false,
        "quote_type": "in_app_before_booking"
      },
      "service_area": {
        "type": "geofence_or_fixed_locations",
        "geojson_path": null,
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
        "public_formula": null,
        "app_quote_required": true
      },
      "source_url": "https://zoox.com/",
      "verified_at": null
    },
    {
      "id": "tesla_robotaxi",
      "name": "Tesla Robotaxi",
      "category": "robotaxi",
      "automation_type": "verify_supervision_status",
      "availability_status": "verify_in_app_and_official_source",
      "booking": {
        "channel": "mobile_app",
        "api_public": false,
        "quote_type": "in_app_before_booking"
      },
      "service_area": {
        "type": "unknown",
        "geojson_path": null,
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
        "public_formula": null,
        "app_quote_required": true
      },
      "source_url": "https://www.tesla.com/robotaxi",
      "verified_at": null
    },
    {
      "id": "uber",
      "name": "Uber",
      "category": "ridehail",
      "automation_type": "human_driver_or_partner_autonomous_service",
      "availability_status": "active",
      "booking": {
        "channel": "mobile_app",
        "api_public": false,
        "quote_type": "in_app_before_booking"
      },
      "service_area": {
        "type": "metro_service_area",
        "geojson_path": null,
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
        "public_formula": null,
        "app_quote_required": true
      },
      "source_url": "https://www.uber.com/",
      "verified_at": null
    },
    {
      "id": "lyft",
      "name": "Lyft",
      "category": "ridehail",
      "automation_type": "human_driver_or_partner_autonomous_service",
      "availability_status": "active",
      "booking": {
        "channel": "mobile_app",
        "api_public": false,
        "quote_type": "in_app_before_booking"
      },
      "service_area": {
        "type": "metro_service_area",
        "geojson_path": null,
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
        "public_formula": null,
        "app_quote_required": true
      },
      "source_url": "https://www.lyft.com/",
      "verified_at": null
    }
  ]
}
```

## `san-francisco/sources.json`

```json
{
  "city_id": "san-francisco-ca",
  "sources": [
    {
      "id": "datasf_parking",
      "name": "DataSF parking datasets",
      "url": "https://data.sfgov.org/",
      "coverage": "SFMTA garages, lots, meters and related parking datasets",
      "format": "Socrata API|CSV|JSON|GeoJSON",
      "realtime": false,
      "verified_at": null
    },
    {
      "id": "waymo_service_area",
      "name": "Waymo service areas",
      "url": "https://support.google.com/waymo/answer/9059119",
      "coverage": "Public service-area guidance",
      "format": "web",
      "realtime": false,
      "verified_at": null
    }
  ]
}
```

---

## `los-angeles/parking.json`

```json
{
  "schema_version": "1.0.0",
  "city_id": "los-angeles-ca",
  "currency": "USD",
  "last_refreshed": null,
  "parking_facilities": [],
  "facility_schema": {
    "id": "string",
    "name": "string",
    "category": "garage|lot|park_and_ride|on_street_zone|other",
    "operator": "string",
    "coordinates": [null, null],
    "capacity": null,
    "access": {
      "public": null,
      "hours": null,
      "reservation_supported": null
    },
    "pricing": {
      "model": "hourly|daily|event|metered|dynamic|unknown",
      "rates": [],
      "quote_required": false,
      "verified_at": null
    },
    "availability": {
      "spaces_available": null,
      "realtime": false,
      "observed_at": null
    },
    "ev_charging": {
      "station_ids": [],
      "parking_payment_required": null
    },
    "source": {
      "url": null,
      "verified_at": null,
      "confidence": "official|third_party|unknown"
    }
  }
}
```

## `los-angeles/curb_rules.json`

```json
{
  "schema_version": "1.0.0",
  "city_id": "los-angeles-ca",
  "last_refreshed": null,
  "rules": [],
  "rule_schema": {
    "id": "string",
    "geometry": {
      "type": "LineString|Point|Polygon",
      "coordinates": []
    },
    "use": "parking|loading|pickup_dropoff|transit|bike|accessible|no_stopping|other",
    "vehicle_classes": [],
    "days_of_week": [],
    "start_time": null,
    "end_time": null,
    "max_stay_minutes": null,
    "permit_required": null,
    "fee": {
      "amount_usd": null,
      "unit": "hour|session|unknown"
    },
    "enforcement_notes": null,
    "source_url": null,
    "verified_at": null,
    "confidence": "official|third_party|unknown"
  }
}
```

## `los-angeles/on_demand_mobility.json`

```json
{
  "schema_version": "1.0.0",
  "city_id": "los-angeles-ca",
  "timezone": "America/Los_Angeles",
  "last_refreshed": null,
  "providers": [
    {
      "id": "waymo",
      "name": "Waymo",
      "category": "robotaxi",
      "automation_type": "driverless",
      "availability_status": "active",
      "booking": {
        "channel": "mobile_app",
        "api_public": false,
        "quote_type": "in_app_before_booking"
      },
      "service_area": {
        "type": "geofence_polygon",
        "geojson_path": null,
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
        "public_formula": null,
        "app_quote_required": true
      },
      "source_url": "https://support.google.com/waymo/answer/9059119",
      "verified_at": null
    },
    {
      "id": "tesla_robotaxi",
      "name": "Tesla Robotaxi",
      "category": "robotaxi",
      "automation_type": "verify_supervision_status",
      "availability_status": "verify_in_app_and_official_source",
      "booking": {
        "channel": "mobile_app",
        "api_public": false,
        "quote_type": "in_app_before_booking"
      },
      "service_area": {
        "type": "unknown",
        "geojson_path": null,
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
        "public_formula": null,
        "app_quote_required": true
      },
      "source_url": "https://www.tesla.com/robotaxi",
      "verified_at": null
    },
    {
      "id": "uber",
      "name": "Uber",
      "category": "ridehail",
      "automation_type": "human_driver_or_partner_autonomous_service",
      "availability_status": "active",
      "booking": {
        "channel": "mobile_app",
        "api_public": false,
        "quote_type": "in_app_before_booking"
      },
      "service_area": {
        "type": "metro_service_area",
        "geojson_path": null,
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
        "public_formula": null,
        "app_quote_required": true
      },
      "source_url": "https://www.uber.com/",
      "verified_at": null
    },
    {
      "id": "lyft",
      "name": "Lyft",
      "category": "ridehail",
      "automation_type": "human_driver_or_partner_autonomous_service",
      "availability_status": "active",
      "booking": {
        "channel": "mobile_app",
        "api_public": false,
        "quote_type": "in_app_before_booking"
      },
      "service_area": {
        "type": "metro_service_area",
        "geojson_path": null,
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
        "public_formula": null,
        "app_quote_required": true
      },
      "source_url": "https://www.lyft.com/",
      "verified_at": null
    }
  ]
}
```

## `los-angeles/sources.json`

```json
{
  "city_id": "los-angeles-ca",
  "sources": [
    {
      "id": "ladot_code_the_curb",
      "name": "LADOT Code the Curb",
      "url": "https://ladot.lacity.gov/codethecurb",
      "coverage": "Digital curb and regulatory inventory initiative",
      "format": "web|GIS|verify",
      "realtime": false,
      "verified_at": null
    },
    {
      "id": "la_open_data",
      "name": "Los Angeles Open Data and GeoHub",
      "url": "https://data.lacity.org/",
      "coverage": "City open-data datasets including transportation and parking-related sources",
      "format": "Socrata API|GIS|varies",
      "realtime": false,
      "verified_at": null
    },
    {
      "id": "waymo_service_area",
      "name": "Waymo service areas",
      "url": "https://support.google.com/waymo/answer/9059119",
      "coverage": "Public service-area guidance",
      "format": "web",
      "realtime": false,
      "verified_at": null
    }
  ]
}
```

---

## Installation manuelle avec Git

Depuis un clone local du dépôt :

```bash
cd recherches-en-mobilite
mkdir -p methodes/planification-trajets-montreal/donnees/us/{california,san-francisco,los-angeles}
```

Crée chaque fichier ci-dessus à son emplacement, puis :

```bash
git add methodes/planification-trajets-montreal/donnees/us
git commit -m "feat: add California EV charging and city parking data schemas"
git push origin main
```

## Liens de départ

- Dépôt : https://github.com/vince-fabmob/recherches-en-mobilite
- Dossier planificateur : https://github.com/vince-fabmob/recherches-en-mobilite/tree/main/methodes/planification-trajets-montreal
- California Open Data : https://data.ca.gov/
- DataSF : https://data.sfgov.org/
- Los Angeles Open Data : https://data.lacity.org/
- LADOT Code the Curb : https://ladot.lacity.gov/codethecurb
