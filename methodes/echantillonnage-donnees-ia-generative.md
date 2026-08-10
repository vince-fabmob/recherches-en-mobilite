# Méthodologie d'échantillonnage pour analyses par IA générative

Objectif : réduire des jeux de données massifs (NYC TLC, Chicago TNP, BIXI, etc.)
en fichiers d'échantillons exploitables dans des outils d'IA générative (contexte
limité), tout en conservant une représentativité statistique suffisante.

Voir `sources/jeux-traces-mobilite-echantillonnage.md` pour le catalogue des sources
brutes utilisables.

## Stratégies d'échantillonnage

### 1. Échantillonnage temporel stratifié
Prendre une semaine représentative par saison plutôt que l'année complète.
Réduit la taille de plus de 90 % tout en préservant la variabilité saisonnière
(ex: hiver vs été pour le vélopartage).

### 2. Échantillonnage géographique
Filtrer par bounding box, arrondissement ou borough pour des analyses locales
ciblées sans charger l'ensemble du territoire couvert.

### 3. Sous-échantillonnage aléatoire
Utiliser `pandas.sample()` ou un filtrage `pyarrow` sur fichier Parquet pour
tester rapidement un pipeline avant de le lancer sur le jeu complet.

### 4. Agrégation préalable
Regrouper par heure/zone avant export (ex: nombre de trajets par tranche horaire
et par zone) plutôt que de conserver chaque ligne brute — souvent suffisant pour
une analyse par IA générative et beaucoup plus léger en tokens.

## Bonnes pratiques

- Privilégier les formats Parquet quand disponibles (lecture partielle possible
  sans tout charger en mémoire, ex: NYC TLC).
- Pour les données déjà agrégées à la source (ex: Chicago TNP par tract
  censitaire), documenter le niveau d'agrégation plutôt que de le refaire.
- Convertir les échantillons finaux en JSONL avec un en-tête décrivant le schéma,
  pour faciliter l'interprétation par un LLM.
- Utiliser `duckdb` pour interroger directement des fichiers Parquet/CSV
  volumineux sans les charger entièrement.

## Scripts de référence à développer

- `scripts/sample_by_time.py` — échantillonnage temporel
- `scripts/sample_by_geo.py` — échantillonnage géographique (bounding box)
- `scripts/sample_random.py` — échantillonnage aléatoire stratifié
- `scripts/to_jsonl.py` — conversion CSV/Parquet vers JSONL pour IA générative

## Exemples externes à consulter

- Dépôt GitHub `CMAP-REPOS/Chicago-TNC-analysis` : script d'extraction ciblée via
  l'API Socrata de Chicago (limite le volume dès l'extraction).
- Projet d'uniformisation des données BIXI par Vincent Goulet (GitLab) : bon
  exemple d'harmonisation de formats multi-années avant échantillonnage.
