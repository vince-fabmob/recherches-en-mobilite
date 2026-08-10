# Registre de Preuve de Covoiturage (RPC) — France

## Source

- **Nom :** Trajets réalisés en covoiturage — Registre de Preuve de Covoiturage (OD-RPC)
- **Territoire :** France
- **Type :** Covoiturage intermédié de courte distance; trajets origine-destination géolocalisés
- **Portail :** https://www.data.gouv.fr/datasets/trajets-realises-en-covoiturage-registre-de-preuve-de-covoiturage
- **Producteur :** Registre de Preuve de Covoiturage / covoiturage.beta.gouv.fr
- **Unité temporelle :** un jeu de données correspond aux trajets réalisés sur un mois
- **Publication :** données ouvertes après traitement de confidentialité (anonymisation, agrégation, etc.)

## Pourquoi cette source est utile

Cette source est particulièrement adaptée à la création de fichiers d'échantillons
pour analyses exploratoires ou avec IA générative. Elle documente des trajets
réalisés, à une échelle plus fine que des indicateurs agrégés, tout en intégrant
un traitement de confidentialité.

Il ne s'agit toutefois pas de traces GPS continues : chaque enregistrement décrit
un trajet origine-destination, sans polyligne ni série de positions intermédiaires.

## Champs analytiques importants

| Champ | Usage |
|---|---|
| `journey_id` | Identifiant unique d'un couple passager-conducteur; unité pour compter les relations de covoiturage |
| `trip_id` | Identifiant qui regroupe les couples passager-conducteur associés à un même véhicule |
| `journey_start_datetime` / `journey_end_datetime` | Analyse des profils horaires et de la durée |
| Coordonnées origine/destination | Cartographie et analyse des flux OD |
| Commune, EPCI, département | Agrégations territoriales |
| `journey_distance` | Distance déclarée par l'opérateur, en mètres |
| Durée du trajet | Analyse de performance et de plausibilité |
| Nombre de sièges passagers | Taux d'occupation potentiel |
| `has_incentive` | Analyse exploratoire des incitations; champ à interpréter avec prudence |

## Attention à l'unité d'analyse

Une ligne représente un couple passager-conducteur. Un conducteur transportant
deux passagers génère donc deux `journey_id`, mais ces observations peuvent être
reliées à un seul `trip_id`. Pour estimer les déplacements de véhicules, agréger
par `trip_id`; pour mesurer les déplacements de passagers ou les appariements,
compter les `journey_id`.

## Protocole d'échantillonnage suggéré

1. Sélectionner une semaine par saison afin de préserver la saisonnalité.
2. Stratifier l'extraction selon le jour (ouvrable ou fin de semaine), la plage
   horaire et des classes de distance.
3. Pour une analyse locale, filtrer par commune, EPCI ou une emprise géographique
   avant l'échantillonnage aléatoire.
4. Produire deux livrables : un échantillon de `journey_id` pour les analyses
   passagers et une table agrégée par `trip_id` pour les analyses véhicule.
5. Créer, pour les LLM, une table OD agrégée avec : territoire de départ,
   territoire d'arrivée, période, nombre de `journey_id`, nombre de `trip_id`,
   distance médiane et durée médiane.

## Limites

- Les données ne couvrent que le covoiturage intermédié, c'est-à-dire réalisé
  via des plateformes partenaires; le covoiturage informel n'y figure pas.
- Les coordonnées et autres données sont traitées afin de prévenir la réidentification.
- Les variables fournies par les opérateurs, notamment les incitations, exigent
  une vérification de complétude avant tout usage causal ou comparatif.

## Liens avec le dépôt

- Catalogue méthodologique : `sources/jeux-traces-mobilite-echantillonnage.md`
- Thème connexe : `sources/mobilite-partagee-tnc-autopartage.md`
- Méthode : `methodes/echantillonnage-donnees-ia-generative.md`
