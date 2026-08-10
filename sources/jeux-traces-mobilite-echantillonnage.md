# Jeux de traces et trajets — Catalogue pour échantillonnage

Catalogue évolutif de sources publiques (open data) de traces GPS et de trajets
(TNC, vélopartage, taxi, transport collectif) utilisables pour créer des fichiers
d'échantillons destinés à des analyses par IA générative.

> À mettre à jour au fur et à mesure des découvertes. Ajouter une entrée par source,
> en respectant le gabarit ci-dessous. Trier par catégorie.

## Comment ajouter une source

Copier ce gabarit et le remplir en fin de section pertinente :

```
### Nom de la source
- Ville/région :
- Type : (Taxi/TNC, Vélopartage, GTFS, Traces GPS, Micromobilité)
- Format : (CSV, Parquet, JSON, GPX, GTFS)
- Fréquence de mise à jour :
- URL :
- Licence :
- Champs clés :
- Date d'ajout : AAAA-MM-JJ
- Notes :
```

## Taxi / TNC (Transportation Network Companies)

### NYC TLC Trip Records
- Ville/région : New York
- Type : Taxi/TNC
- Format : Parquet
- Fréquence de mise à jour : Mensuelle
- URL : https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- Licence : Ouvert (gouvernement municipal)
- Champs clés : pickup/dropoff datetime, zones TLC, tarif, distance
- Date d'ajout : 2026-08-10
- Notes : Anonymisé par zone TLC, pas de coordonnées lat/lon précises. Format Parquet, lisible efficacement avec pyarrow/duckdb sans tout charger en mémoire.

### Chicago Transportation Network Providers (TNP) — Trips
- Ville/région : Chicago
- Type : Rideshare
- Format : CSV/JSON (API Socrata)
- Fréquence de mise à jour : Trimestrielle
- URL : https://data.cityofchicago.org/
- Licence : Ouvert (gouvernement municipal)
- Champs clés : tract censitaire origine/destination, heure arrondie à 15 min, tarif arrondi
- Date d'ajout : 2026-08-10
- Notes : Pré-agrégé par la ville pour préserver la confidentialité. Voir le dépôt CMAP-REPOS/Chicago-TNC-analysis sur GitHub pour un exemple de script d'extraction via l'API Socrata (télécharge seulement colonnes/plages nécessaires).

## Vélopartage

### BIXI Montréal — Données ouvertes
- Ville/région : Montréal
- Type : Vélopartage
- Format : CSV
- Fréquence de mise à jour : Annuelle (parfois mensuelle)
- URL : https://bixi.com/en/open-data/
- Licence : Ouvert
- Champs clés : station départ/arrivée, durée, type d'usager
- Date d'ajout : 2026-08-10
- Notes : Format a changé en 2022. Voir le projet d'uniformisation de Vincent Goulet (GitLab) pour harmoniser les années.

### Divvy (Chicago) — System Data
- Ville/région : Chicago
- Type : Vélopartage
- Format : CSV
- Fréquence de mise à jour : Mensuelle
- URL : https://divvybikes.com/system-data
- Licence : Ouvert
- Champs clés : station, heure début/fin, type d'usager
- Date d'ajout : 2026-08-10
- Notes :

### Citi Bike (NYC) — System Data
- Ville/région : New York
- Type : Vélopartage
- Format : CSV
- Fréquence de mise à jour : Mensuelle
- URL : https://citibikenyc.com/system-data
- Licence : Ouvert
- Champs clés : station, heure début/fin, latitude/longitude
- Date d'ajout : 2026-08-10
- Notes :

### Vélib' Métropole (Paris) — Open Data
- Ville/région : Paris
- Type : Vélopartage
- Format : CSV / temps réel
- Fréquence de mise à jour : Variable
- URL : https://opendata.paris.fr
- Licence : Ouvert
- Champs clés : stations, disponibilité
- Date d'ajout : 2026-08-10
- Notes :

### TfL Cycle Hire Data (Londres, Santander Cycles)
- Ville/région : Londres
- Type : Vélopartage
- Format : CSV
- Fréquence de mise à jour : Hebdomadaire
- URL : https://cycling.data.tfl.gov.uk/
- Licence : Ouvert (TfL)
- Champs clés : trajets vélos en libre-service
- Date d'ajout : 2026-08-10
- Notes :

## Micromobilité / temps réel

### GBFS — General Bikeshare Feed Specification (catalogue mondial)
- Ville/région : Mondial
- Type : Vélopartage/micromobilité temps réel
- Format : JSON
- Fréquence de mise à jour : Temps réel
- URL : https://github.com/MobilityData/gbfs
- Licence : Standard ouvert (MobilityData)
- Champs clés : position des stations, disponibilité vélos/trottinettes
- Date d'ajout : 2026-08-10
- Notes : Plus de 1000 systèmes référencés dans le monde. Snapshots légers, l'échantillonnage porte surtout sur la fréquence de capture d'un historique.

## Traces GPS génériques

### OpenStreetMap — GPS Traces
- Ville/région : Mondial
- Type : Traces GPS génériques
- Format : GPX
- Fréquence de mise à jour : Continue (contributions usagers)
- URL : https://www.openstreetmap.org/traces
- Licence : ODbL
- Champs clés : traces GPS brutes contribuées par les usagers
- Date d'ajout : 2026-08-10
- Notes :

## Transport en commun

### Transitland / OpenMobilityData
- Ville/région : Mondial
- Type : Transport en commun (GTFS)
- Format : GTFS statique / temps réel
- Fréquence de mise à jour : Variable selon l'agence
- URL : https://www.transit.land/
- Licence : Variable selon l'agence
- Champs clés : horaires, arrêts, itinéraires
- Date d'ajout : 2026-08-10
- Notes :

## Multi-thématique (Montréal)

### Données ouvertes Ville de Montréal
- Ville/région : Montréal
- Type : Multi-thématique mobilité
- Format : CSV/JSON/Shapefile
- Fréquence de mise à jour : Variable
- URL : https://donnees.montreal.ca/
- Licence : Licence ouverte Montréal
- Champs clés : comptages vélo, stationnement, réseau routier
- Date d'ajout : 2026-08-10
- Notes :

## À explorer / non encore documenté

- Répertoires nationaux (Statistique Canada, data.gouv.fr, data.gov)
- Kaggle (versions déjà échantillonnées par la communauté, à valider pour provenance/licence)
