# Méthodologie de création de fichiers échantillons pour analyses de mobilité et IA générative

## 1. Objet et périmètre

Cette page décrit un protocole reproductible pour réduire des jeux de données
massifs de mobilité en fichiers d'échantillons légers, représentatifs et
interprétables. Les échantillons servent à l'exploration, à la mise au point de
scripts, à la cartographie et à des analyses assistées par IA générative.

Un échantillon ne remplace pas le jeu complet pour une estimation statistique
formelle. Toute inférence sur la population entière exige un plan d'échantillonnage,
des pondérations et une validation adaptés.

Voir `sources/jeux-traces-mobilite-echantillonnage.md` pour le catalogue des
sources et `sources/covoiturage-rpc-france.md` pour un exemple documenté.

## 2. Fiche d'identité du jeu source

Avant tout traitement, consigner dans `metadata.json` ou dans le README :

- Source, URL, producteur, licence et date de téléchargement
- Période couverte, format, nombre de lignes, colonnes et taille du fichier
- Unité d'observation et granularité spatiale/temporelle
- Champs sensibles, règles de confidentialité et limitations connues
- Version du script et somme de contrôle facultative du fichier brut

Conserver le jeu brut en dehors du dépôt GitHub. Le dépôt doit contenir les
scripts, métadonnées et petits échantillons dont la licence et le risque de
réidentification permettent la publication.

## 3. Définir l'unité d'analyse

L'unité d'analyse détermine les filtres, les doublons et les agrégations.

| Source ou cas | Unité possible | Point d'attention |
|---|---|---|
| NYC TLC | Course de taxi ou VTC | Les zones remplacent généralement les coordonnées précises |
| Chicago TNP | Trajet agrégé OD-temps | Les données sont déjà protégées par agrégation/arrondissement |
| BIXI, Divvy, Citi Bike | Trajet ou paire de stations | Distinguer le trajet de l'observation de disponibilité d'une station |
| Registre de Preuve de Covoiturage | `journey_id` ou `trip_id` | Une ligne est un couple passager-conducteur; plusieurs `journey_id` peuvent partager un `trip_id` |
| GBFS | Snapshot de station | L'échantillonnage porte sur la fréquence de capture |

Choisir `journey_id` pour compter des passagers/appairages de covoiturage et
`trip_id` pour analyser des mouvements de véhicules.

## 4. Choisir une stratégie d'échantillonnage

### Temporel stratifié

Prélever une semaine représentative par saison, en conservant les jours ouvrables,
les fins de semaine, les pointes et les périodes hors pointe. Cette méthode
réduit fortement le volume tout en préservant une partie de la saisonnalité.

### Géographique

Filtrer par bounding box, arrondissement, borough, commune, EPCI, zone TLC ou
corridor OD. La sélection géographique doit être explicite dans les métadonnées.

### Aléatoire stratifié

Tirer des observations par strate : période, territoire, classe de distance,
durée, type d'usager ou mode. Fixer une graine aléatoire (`random_seed`) afin
de rendre le résultat reproductible.

### Agrégation préalable

Quand les microdonnées ne sont pas nécessaires, produire une table agrégée,
par exemple `zone_depart`, `zone_arrivee`, `date`, `heure`, `nombre_trajets`,
`distance_mediane`, `duree_mediane`. Cette option est souvent la plus adaptée
aux limites de contexte des modèles génératifs.

## 5. Chaîne de traitement

1. Lire uniquement les colonnes requises; préférer Parquet, DuckDB ou PyArrow
   pour les fichiers volumineux.
2. Filtrer la période et le territoire définis dans le plan d'analyse.
3. Nettoyer les données : valeurs manquantes, durées négatives, distances
   impossibles, doublons et coordonnées invalides.
4. Créer les strates et réaliser l'échantillonnage avec une graine fixe.
5. Agréger ou généraliser les géographies et les temps au besoin.
6. Produire un fichier d'échantillon, des métadonnées et un rapport qualité.
7. Comparer les distributions du jeu brut filtré et de l'échantillon.

## 6. Contrôles de qualité

Documenter au minimum :

- Nombre de lignes avant et après chaque étape
- Taux de valeurs manquantes et de lignes éliminées
- Doublons, identifiants non uniques et valeurs hors domaine
- Distributions avant/après : jour, heure, distance, durée, territoire et mode
- Taille de chaque strate et justification des éventuels déséquilibres

Ne pas retenir un échantillon qui efface une période, un territoire ou une
classe de distance importante pour la question étudiée.

## 7. Confidentialité, éthique et licence

- Respecter la licence et les conditions du portail source.
- Ne pas publier de microdonnées avec coordonnées précises si le risque de
  réidentification demeure significatif.
- Préférer l'agrégation spatiale, l'arrondissement des coordonnées ou la
  suppression des OD rares.
- Distinguer les données observées des variables inférées ou imputées.
- Documenter les biais de couverture : par exemple, le RPC français couvre le
  covoiturage intermédié, pas le covoiturage informel.

## 8. Format de sortie pour IA générative

| Fichier | Rôle |
|---|---|
| `sample.parquet` ou `sample.csv` | Échantillon microdonnées, si autorisé |
| `aggregate.csv` | Table agrégée privilégiée pour l'analyse conversationnelle |
| `metadata.json` | Source, période, filtres, méthode, graine, volume et licence |
| `data_dictionary.md` | Définition des champs, unités et codes |
| `quality_report.md` | Résultats des contrôles avant/après |
| `create_sample.py` | Script exécutable et versionné |

Utiliser CSV pour les petites tables et JSONL pour des observations enrichies.
Pour chaque analyse LLM, fournir un court contexte : objectif, unité d'analyse,
période, territoire, variables, transformations et limites.

Convention suggérée :

```text
<source>_<territoire>_<periode>_<methode>_v<version>.parquet
```

## 9. Exemple : Registre de Preuve de Covoiturage

Pour le RPC français :

1. Choisir des semaines réparties sur les saisons.
2. Stratifier par jour ouvrable/week-end, plage horaire et classe de distance.
3. Filtrer une commune, un EPCI ou une région si l'analyse est territoriale.
4. Créer un échantillon `journey_id` pour les analyses passagers et une table
   dédoublonnée par `trip_id` pour les analyses véhicule.
5. Exporter une table OD agrégée avec volumes, distance médiane et durée médiane.

Voir `sources/covoiturage-rpc-france.md` pour les champs, limites et précautions
propres à cette source.

## 10. Reproductibilité et scripts

Prévoir les scripts suivants :

- `scripts/sample_by_time.py` : filtre et tirage temporel stratifié
- `scripts/sample_by_geo.py` : filtre spatial ou OD
- `scripts/sample_random.py` : tirage aléatoire stratifié avec graine
- `scripts/aggregate_for_llm.py` : agrégation zone-temps ou OD-temps
- `scripts/to_jsonl.py` : conversion CSV/Parquet vers JSONL
- `scripts/validate_sample.py` : contrôles de schéma et distributions

Conserver les paramètres dans un fichier YAML ou JSON : source, période,
territoire, strates, taille cible, graine, champs retenus et règles de
confidentialité. Ainsi, un échantillon peut être régénéré ou audité sans
interprétation manuelle.

## 11. Références utiles

- `sources/jeux-traces-mobilite-echantillonnage.md`
- `sources/covoiturage-rpc-france.md`
- Dépôt `CMAP-REPOS/Chicago-TNC-analysis` : exemple d'extraction ciblée via
  l'API Socrata
- Projet d'uniformisation des données BIXI par Vincent Goulet (GitLab) :
  exemple d'harmonisation multi-années avant échantillonnage
