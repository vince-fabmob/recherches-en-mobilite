# Packs de mobilité — Las Vegas, San Francisco et Los Angeles

Ce document contient trois packs prêts à copier dans le dépôt :

```text
methodes/planification-trajets-montreal/donnees/us/
```

Les données structurées distinguent les services à devis dynamique et les services à prix/zone publics. Ne pas remplacer les valeurs `null` ou `verification_required: true` par des données supposées.

---

# 1. Pack Las Vegas

## Arborescence

```text
las-vegas/
├── README.md
├── on_demand_mobility.json
├── vegas_loop.json
├── parking.json
├── ev_charging.json
├── sources.json
└── tests_itineraires.json
```

## `las-vegas/README.md`

```md
# Pack mobilité — Las Vegas

Ce pack indexe les options de mobilité multimodale de Las Vegas.

## Priorités

- Comparer RTC, marche, vélo partagé, VTC, robotaxi, Vay, stationnement et Vegas Loop.
- Distinguer robotaxi sans conducteur, VTC avec chauffeur et véhicule livré par téléopération.
- Pour Vegas Loop, n’utiliser que les stations ouvertes et confirmer les tarifs avant affichage.
- Ne jamais garantir un prix ou une disponibilité d’application.
```

## `las-vegas/on_demand_mobility.json`

```json
{
  "schema_version": "1.0.0",
  "city_id": "las-vegas-nv",
  "timezone": "America/Los_Angeles",
  "last_refreshed": null,
  "providers": [
    {
      "id": "zoox",
      "name": "Zoox",
      "category": "robotaxi",
      "automation_type": "driverless",
      "availability_status": "active",
      "booking": {
        "channel": "mobile_app",
        "api_public": false,
        "quote_type": "in_app_before_booking"
      },
      "service_area": {
        "type": "fixed_locations_or_geofence",
        "geojson_path": null,
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
        "public_formula": null,
        "app_quote_required": true
      },
      "constraints": {
        "origin_must_be_eligible": true,
        "destination_must_be_eligible": true,
        "driver_license_required": false,
        "user_drives_vehicle": false
      },
      "source_url": "https://zoox.com/las-vegas",
      "verified_at": null
    },
    {
      "id": "vay",
      "name": "Vay",
      "category": "short_term_rental",
      "automation_type": "teledriven_delivery",
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
        "model": "per_minute_or_dynamic_quote",
        "currency": "USD",
        "public_formula": null,
        "app_quote_required": true
      },
      "constraints": {
        "driver_license_required": true,
        "user_drives_vehicle": true,
        "delivery_and_pickup_remote_driving": true
      },
      "source_url": "https://vay.io/",
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
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
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
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
        "app_quote_required": true
      },
      "source_url": "https://www.lyft.com/",
      "verified_at": null
    }
  ]
}
```

## `las-vegas/vegas_loop.json`

```json
{
  "schema_version": "1.0.0",
  "id": "vegas-loop",
  "name": "Vegas Loop",
  "operator": "The Boring Company",
  "category": "fixed_station_tunnel_network",
  "city_id": "las-vegas-nv",
  "booking": {
    "channel": "web_or_mobile_ticket",
    "url": "https://www.lvloop.com/tickets",
    "api_public": false
  },
  "stations": [],
  "fares": {
    "model": "route_or_station_pair",
    "currency": "USD",
    "verify_before_display": true,
    "last_verified": null
  },
  "planning_rules": {
    "max_access_walk_m": 700,
    "transfer_penalty_min": 5,
    "require_open_station_at_both_ends": true,
    "do_not_use_planned_stations": true
  },
  "source_url": "https://www.lvcva.com/vegas-loop/"
}
```

## `las-vegas/parking.json`

```json
{
  "schema_version": "1.0.0",
  "city_id": "las-vegas-nv",
  "currency": "USD",
  "last_refreshed": null,
  "parking_facilities": [],
  "facility_schema": {
    "id": "string",
    "name": "string",
    "category": "hotel_casino_garage|garage|lot|airport|convention_center|on_street_zone|other",
    "operator": "string",
    "coordinates": [null, null],
    "capacity": null,
    "access": {
      "public": null,
      "hours": null,
      "hotel_guest_conditions": null,
      "reservation_supported": null
    },
    "pricing": {
      "model": "hourly|daily|event|hotel_guest|dynamic|unknown",
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

## `las-vegas/ev_charging.json`

```json
{
  "city_id": "las-vegas-nv",
  "charging_registry_scope": "national_or_nevada_source_required",
  "station_ids": [],
  "planning_rules": {
    "include_parking_fee_in_total_cost": true,
    "require_connector_compatibility": true,
    "do_not_guarantee_port_availability_without_realtime_source": true
  }
}
```

## `las-vegas/sources.json`

```json
{
  "city_id": "las-vegas-nv",
  "sources": [
    {
      "id": "rtc_southern_nevada",
      "name": "Regional Transportation Commission of Southern Nevada",
      "url": "https://www.rtcsnv.com/ways-to-travel/transit-services/for-developers/",
      "coverage": "Transit data and developer resources",
      "format": "GTFS|GTFS-RT|GIS|varies",
      "realtime": true,
      "verified_at": null
    },
    {
      "id": "zoox_las_vegas",
      "name": "Zoox Las Vegas",
      "url": "https://zoox.com/las-vegas",
      "coverage": "Robotaxi booking and service guidance",
      "format": "web|mobile_app",
      "realtime": false,
      "verified_at": null
    },
    {
      "id": "vay_las_vegas",
      "name": "Vay Las Vegas",
      "url": "https://vay.io/",
      "coverage": "Teleoperated delivery and short-term vehicle rental",
      "format": "web|mobile_app",
      "realtime": false,
      "verified_at": null
    },
    {
      "id": "vegas_loop",
      "name": "Vegas Loop / LVCVA",
      "url": "https://www.lvcva.com/vegas-loop/",
      "coverage": "Stations, tickets and passenger information",
      "format": "web",
      "realtime": false,
      "verified_at": null
    }
  ]
}
```

## `las-vegas/tests_itineraires.json`

```json
{
  "city_id": "las-vegas-nv",
  "scenarios": [
    {
      "id": "airport_to_strip_hotel",
      "requirements": ["bagages", "arrivee_tardive", "prix_total", "pickup_legal"]
    },
    {
      "id": "convention_center_to_strip",
      "requirements": ["vegas_loop", "marche", "rtc", "robotaxi", "ridehail"]
    },
    {
      "id": "multiple_stops_with_vehicle",
      "requirements": ["vay", "stationnement", "recharge", "duree_totale"]
    }
  ]
}
```

---

# 2. Pack San Francisco

## Arborescence

```text
san-francisco/
├── README.md
├── on_demand_mobility.json
├── parking.json
├── curb_rules.json
├── ev_charging.json
├── sources.json
└── tests_itineraires.json
```

## `san-francisco/README.md`

```md
# Pack mobilité — San Francisco

Ce pack indexe les options de mobilité multimodale pour San Francisco et la baie.

## Priorités

- Comparer transport collectif, mobilité active, robotaxi, VTC et automobile en intégrant les contraintes de stationnement.
- Vérifier la couverture Waymo et toute offre Zoox ou Tesla Robotaxi dans l’application avant recommandation.
- Ne pas présenter le stationnement sur rue comme disponible sans donnée temps réel officielle.
- Lier les bornes au socle Californie et ajouter les frais d’accès au garage au coût total.
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
      "constraints": {
        "origin_must_be_eligible": true,
        "destination_must_be_eligible": true,
        "driver_license_required": false,
        "user_drives_vehicle": false
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
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
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
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
        "app_quote_required": true
      },
      "source_url": "https://www.lyft.com/",
      "verified_at": null
    }
  ]
}
```

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

## `san-francisco/ev_charging.json`

```json
{
  "city_id": "san-francisco-ca",
  "charging_registry_path": "../shared/california/ev_charging_network.json",
  "station_ids": [],
  "planning_rules": {
    "include_parking_fee_in_total_cost": true,
    "require_connector_compatibility": true,
    "do_not_guarantee_port_availability_without_realtime_source": true
  }
}
```

## `san-francisco/sources.json`

```json
{
  "city_id": "san-francisco-ca",
  "sources": [
    {
      "id": "datasf",
      "name": "DataSF",
      "url": "https://data.sfgov.org/",
      "coverage": "Transportation, parking, SFMTA lots, garages and related open data",
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

## `san-francisco/tests_itineraires.json`

```json
{
  "city_id": "san-francisco-ca",
  "scenarios": [
    {
      "id": "airport_to_downtown_hotel",
      "requirements": ["bagages", "transit", "robotaxi", "ridehail", "prix_total"]
    },
    {
      "id": "downtown_to_hilly_neighborhood",
      "requirements": ["marche", "denivele", "waymo", "transit", "stationnement"]
    },
    {
      "id": "multiple_stops_with_ev",
      "requirements": ["garage", "recharge", "tarif_stationnement", "duree_totale"]
    }
  ]
}
```

---

# 3. Pack Los Angeles

## Arborescence

```text
los-angeles/
├── README.md
├── on_demand_mobility.json
├── parking.json
├── curb_rules.json
├── ev_charging.json
├── sources.json
└── tests_itineraires.json
```

## `los-angeles/README.md`

```md
# Pack mobilité — Los Angeles

Ce pack indexe les options de mobilité multimodale de Los Angeles.

## Priorités

- Comparer LA Metro, marche, vélo, Waymo, VTC, automobile, stationnement et recharge.
- Traiter stationnement, marche d’accès et congestion comme des composantes du coût porte-à-porte.
- Utiliser les règles de curb pour sélectionner un point de dépose VTC/robotaxi légal.
- Vérifier les géorepérages et les prix de robotaxi/VTC dans les applications avant affichage.
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
      "constraints": {
        "origin_must_be_eligible": true,
        "destination_must_be_eligible": true,
        "driver_license_required": false,
        "user_drives_vehicle": false
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
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
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
        "verification_required": true
      },
      "pricing": {
        "model": "dynamic_quote",
        "currency": "USD",
        "app_quote_required": true
      },
      "source_url": "https://www.lyft.com/",
      "verified_at": null
    }
  ]
}
```

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
    "category": "garage|lot|park_and_ride|on_street_zone|airport|event_parking|other",
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

## `los-angeles/ev_charging.json`

```json
{
  "city_id": "los-angeles-ca",
  "charging_registry_path": "../shared/california/ev_charging_network.json",
  "station_ids": [],
  "planning_rules": {
    "include_parking_fee_in_total_cost": true,
    "require_connector_compatibility": true,
    "do_not_guarantee_port_availability_without_realtime_source": true
  }
}
```

## `los-angeles/sources.json`

```json
{
  "city_id": "los-angeles-ca",
  "sources": [
    {
      "id": "la_open_data",
      "name": "Los Angeles Open Data",
      "url": "https://data.lacity.org/",
      "coverage": "Transportation, parking and other municipal datasets",
      "format": "Socrata API|GIS|varies",
      "realtime": false,
      "verified_at": null
    },
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

## `los-angeles/tests_itineraires.json`

```json
{
  "city_id": "los-angeles-ca",
  "scenarios": [
    {
      "id": "airport_to_hotel",
      "requirements": ["bagages", "transit", "robotaxi", "ridehail", "prix_total"]
    },
    {
      "id": "metro_station_to_final_destination",
      "requirements": ["transit", "last_mile", "waymo", "ridehail", "curb_pickup"]
    },
    {
      "id": "event_or_multiple_stops",
      "requirements": ["stationnement", "recharge", "congestion", "duree_totale"]
    }
  ]
}
```

---

# Installation manuelle

1. Téléverse ou copie chaque bloc JSON dans le fichier portant le même nom, dans son répertoire de ville.
2. Commence par les trois `README.md`, puis les fichiers `on_demand_mobility.json`.
3. Ajoute ensuite stationnement, bornes et règles de curb selon les sources officielles disponibles.
4. Commit suggéré :

```bash
git add methodes/planification-trajets-montreal/donnees/us
git commit -m "feat: add city mobility packs for Las Vegas, San Francisco and Los Angeles"
git push origin main
```

# Sources à vérifier avant ingestion automatisée

- Waymo : https://support.google.com/waymo/answer/9059119
- Zoox Las Vegas : https://zoox.com/las-vegas
- Vay : https://vay.io/
- Vegas Loop : https://www.lvcva.com/vegas-loop/
- RTC Southern Nevada : https://www.rtcsnv.com/ways-to-travel/transit-services/for-developers/
- DataSF : https://data.sfgov.org/
- Los Angeles Open Data : https://data.lacity.org/
- LADOT Code the Curb : https://ladot.lacity.gov/codethecurb
