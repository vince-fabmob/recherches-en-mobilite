# Valorisation des données GTFS et capacité des services d’autobus

## Statut du document

**Document méthodologique évolutif.** Cette page distingue les méthodes établies, leurs implémentations reproductibles et les propositions méthodologiques à tester. Elle ne constitue ni une norme officielle ni un avis professionnel. Toute application décisionnelle ou publication doit vérifier la version la plus récente des sources primaires, les définitions locales, la validité du jeu GTFS et les hypothèses retenues.

Les résultats provenant uniquement d’un GTFS statique décrivent une **offre planifiée**. Ils ne constituent pas une observation de l’exploitation réelle.

## Objet

Ce guide organise l’usage analytique des données GTFS statiques pour documenter :

- les départs et passages programmés par heure ;
- les intervalles programmés ;
- les temps de parcours et la vitesse commerciale programmée ;
- la capacité d’offre théorique ;
- l’articulation entre l’offre planifiée et l’évaluation d’une voie réservée.

Il précise aussi les limites du GTFS et sépare les calculs établis des hypothèses de travail qui nécessitent une validation.

## Principe de séparation

| Niveau | Rôle | Statut |
|---|---|---|
| Méthodes établies | Concepts, procédures et seuils provenant de manuels institutionnels ou d’articles évalués par les pairs | Références à consulter dans leur version à jour |
| Implémentations reproductibles | Scripts qui appliquent une méthode documentée à un GTFS donné | Code indicatif, versionné et testable |
| Propositions méthodologiques | Indicateurs, scénarios ou approximations développés pour l’espace | Hypothèses non validées à confronter aux données observées |

## Ce que mesure un GTFS statique

| Indicateur | GTFS statique seul | Qualification requise | Donnée complémentaire utile |
|---|---:|---|---|
| Départs programmés par heure à un arrêt | Oui | Offre planifiée | Vérification des calendriers et exceptions |
| Passages programmés par heure sur un segment | Oui, avec une règle explicite de franchissement | Offre planifiée | Contrôle des variantes, directions et courses partielles |
| Intervalle entre passages | Oui | Intervalle programmé | AVL ou GTFS-Realtime pour la régularité effective |
| Temps de parcours | Oui | Temps programmé | AVL ou GTFS-Realtime pour le temps observé |
| Vitesse commerciale | Oui si distance et horaire sont disponibles | Vitesse commerciale programmée | AVL/GPS pour la vitesse commerciale observée et sa variabilité |
| Capacité d’offre | Partiellement | Estimation théorique | Modèle de véhicule et capacité nominale documentés |
| Débit-personnes | Non | Non inférable sans hypothèse de charge | APC, billettique, comptages ou enquête |
| Capacité d’une voie réservée | Non | Évaluation d’infrastructure distincte | Temps d’arrêt, géométrie, feux, aires d’arrêt et observation terrain |

### Règle de vocabulaire

Utiliser **vitesse commerciale programmée** lorsque le calcul repose uniquement sur des horaires GTFS. Réserver **vitesse commerciale observée** aux données de parcours réellement effectués (AVL, GPS ou GTFS-Realtime validé). Cette distinction doit aussi s’appliquer aux temps de parcours, intervalles et fréquences.

## Données GTFS mobilisées

| Fichier | Usage principal | Points de contrôle |
|---|---|---|
| `stops.txt` | Identification et localisation des arrêts | Identifiants, doublons, accessibilité, arrêt parent/enfant |
| `routes.txt` | Ligne et type de service | Regroupements de lignes et variantes |
| `trips.txt` | Course, direction, service et tracé | `direction_id`, `service_id`, `shape_id` |
| `stop_times.txt` | Heures d’arrivée et de départ | Heures au-delà de 24:00, séquence des arrêts, temps manquants |
| `calendar.txt` | Jours réguliers de service | Date de début, de fin et jours actifs |
| `calendar_dates.txt` | Exceptions de service | Ajouts et suppressions de service |
| `shapes.txt` | Tracés et distance reconstruite | Cohérence avec les arrêts et variantes |
| `frequencies.txt` | Services définis par fréquence | Ne pas les traiter comme des départs explicitement énumérés |

## Méthodes établies à référencer

### Offre programmée, passages et intervalles

Le comptage des voyages GTFS dans une période donnée produit une mesure de l’**offre horaire programmée**. Pour être reproductible, toute extraction doit documenter :

- le jour de service et le traitement de `calendar.txt` et `calendar_dates.txt` ;
- l’arrêt, le segment ou le point de coupure retenu ;
- la direction et le traitement des variantes ;
- la fenêtre temporelle et la convention de bord (par exemple, départ inclus à l’heure de début et exclu à l’heure de fin) ;
- le traitement des heures GTFS supérieures à 24:00 ;
- le traitement des services `frequencies.txt`.

Le résultat doit être diffusé comme « voyages programmés/h » ou « autobus programmés/h », et non comme une fréquence observée.

### Temps de parcours et vitesse commerciale programmée

Les heures de `stop_times.txt` permettent d’estimer le temps programmé entre deux arrêts ou deux bornes de segment. Si la distance de parcours est connue — via `shape_dist_traveled`, un tracé `shapes.txt` correctement projeté ou une mesure externe documentée — une vitesse moyenne programmée peut être produite.

Les unités, le système de coordonnées, la règle de sélection du trajet et le traitement des arrêts intermédiaires doivent être explicités. Une moyenne globale ne doit pas masquer les écarts par période, direction, variante et jour-type.

### Capacité des lignes, arrêts et voies réservées

La capacité d’un corridor d’autobus ne découle pas mécaniquement du nombre de voyages GTFS. Le *Transit Capacity and Quality of Service Manual* (TCQSM) distingue notamment la capacité en véhicules et en personnes, la capacité de voie, la capacité des arrêts et la capacité des stations. La capacité de la ligne est souvent contrainte par l’**arrêt critique**, soit le point dont le temps d’arrêt, la géométrie, le signal, la circulation ou l’aire de charge limite le débit global.

Pour évaluer une voie réservée, utiliser la méthode la plus récente du TCQSM et les données locales nécessaires : temps d’arrêt, nombre et configuration des quais, possibilités de dépassement, priorité aux feux, carrefours, taux de défaillance acceptable, modèles de véhicules, charge et règles d’exploitation. Le GTFS peut quantifier l’offre prévue à confronter à cette capacité ; il ne remplace pas cette analyse.

### Capacité-personnes

Le passage d’une capacité en véhicules/h à une capacité ou un débit en personnes/h exige des hypothèses ou des observations sur la capacité des véhicules et leur taux de charge. Le résultat doit distinguer :

- la capacité nominale théorique ;
- la capacité de conception ou de planification ;
- la charge observée ;
- le débit-personnes estimé à partir d’hypothèses.

Les hypothèses de charge ne doivent pas être confondues avec de l’achalandage mesuré.

## Validation recommandée

Comparer les résultats GTFS statiques aux sources suivantes lorsque disponibles :

- AVL/GPS : temps de parcours, vitesse et fiabilité observés ;
- GTFS-Realtime : prédictions, mises à jour et écarts de service, après évaluation de leur qualité ;
- APC : montées, descentes et charge par arrêt ;
- billettique : validations, avec précautions sur les correspondances et les titres ;
- comptages terrain : charge, temps d’arrêt, files et fonctionnement des arrêts ;
- signalisation et inventaires d’infrastructure : feux, quais, voies de dépassement et restrictions.

Toute comparaison devrait présenter la période, l’échantillon, la couverture spatiale, les exclusions, l’écart moyen, la dispersion et les ruptures de série éventuelles.

## Propositions méthodologiques — hypothèses à tester

> **Statut : non validé.** Les propositions ci-dessous sont des pistes de calcul pour l’exploration et la comparaison de scénarios. Elles ne doivent pas être présentées comme des méthodes institutionnelles validées ni comme des mesures observées. Chaque application doit indiquer ses paramètres, ses hypothèses, son code, sa version de GTFS et son protocole de validation.

### P1. Indice de densité d’offre programmée par corridor

Produire, pour un point de coupure et une direction, les autobus programmés/h, les places théoriques/h et la vitesse commerciale programmée. L’objectif est de comparer des scénarios de desserte ou des périodes GTFS archivées, sans en inférer une performance réelle.

### P2. Comparaison avant/après d’une mesure préférentielle

Comparer des GTFS de périodes distinctes pour un même segment afin d’estimer l’évolution programmée des temps de parcours, de la vitesse commerciale et de l’offre. Une interprétation causale exige de contrôler les changements de parcours, d’arrêts, de période, de travaux, de calendrier et de politique de service. Une validation AVL est requise pour conclure sur la performance réalisée.

### P3. Capacité-personnes scénarisée

Combiner une offre programmée avec une capacité nominale documentée et plusieurs scénarios de charge. Chaque scénario doit être étiqueté — faible, central, élevé — et ne doit pas être appelé « achalandage » sans donnée observée.

### P4. Test exploratoire de corridor SEAM

Comparer un débit-personnes estimé pour une voie réservée avec celui d’une voie générale adjacente. Cet indicateur peut soutenir un suivi exploratoire des seuils DAPP employés dans l’espace — notamment un débit-personnes d’au moins deux fois celui de la voie générale adjacente et un gain de vitesse commerciale bus de 20 %. Ces seuils sont propres au cadre exploratoire SEAM et ne constituent pas des normes TCQSM. Les hypothèses d’occupation automobile, de charge des autobus, de temporalité et de point de comparaison doivent être affichées.

## Implémentations Python proposées

Les scripts associés doivent être placés dans un répertoire distinct et porter un en-tête de traçabilité :

```text
methodes/gtfs/
├── README.md
├── calcul-offre-horaire-gtfs.py
├── calcul-intervalles-programmes.py
├── calcul-vitesse-programmee-gtfs.py
└── propositions/
    ├── capacite-personnes-scenarisee.py
    └── comparaison-debit-voie-reservee.py
```

En-tête minimal attendu :

```python
"""
Statut : méthode établie appliquée / proposition méthodologique non validée
Référence : titre, auteur ou organisme, année, DOI ou URL
Données : fichiers requis, version du GTFS, période de service
Sortie : indicateur programmé, estimé ou observé
Hypothèses : paramètres et valeurs par défaut
Validation : donnée externe ou protocole recommandé
Limites : couverture, biais et usages non appropriés
Dernière vérification : AAAA-MM-JJ
"""
```

Le code ne remplace pas une méthode de référence. Il doit permettre de reproduire les paramètres, les filtres et les résultats d’une analyse.

## Limites et précautions

- Un GTFS statique décrit une intention de service, non les conditions observées de circulation ou d’exploitation.
- La qualité varie selon le producteur, la date de publication, les exceptions de calendrier et la précision des tracés.
- Le GTFS ne renseigne généralement ni la charge réelle, ni le temps de montée, ni les retards, ni les détournements, ni les refus d’embarquement.
- Les résultats sont sensibles au choix de l’arrêt, du segment, de la direction, de la période et de la règle d’agrégation.
- Une vitesse moyenne peut masquer une variabilité importante ; présenter percentiles et distributions lorsque des données observées existent.
- Toute comparaison entre réseaux exige une harmonisation des définitions de capacité, de charge, de période, de véhicule et de niveau de service.

## Références à maintenir

### Méthodes et capacité

- Transportation Research Board. *Transit Capacity and Quality of Service Manual*, TCRP Report 165, 3e édition, et mises à jour associées : https://onlinepubs.trb.org/onlinepubs/tcrp/tcrp_rpt_165ch-01.pdf
- Transportation Research Board. *Transit Capacity and Quality of Service Manual*, documents techniques sur la capacité des autobus, des arrêts et des installations : https://onlinepubs.trb.org/onlinepubs/tcrp/tcrp_webdoc_6-a.pdf
- Bunker, J. M., et Hisham, F. (2021). *Critical Station Practical Capacity on a Bus Rapid Transit Line with Nonstopping Buses*. Transportation Research Record. https://doi.org/10.1177/0361198121999397

### Exactitude et limites du GTFS

- Owen, A., Murphy, B., et Levinson, D. (2020). *On the accuracy of schedule-based GTFS for measuring accessibility by public transit*. Journal of Transport Geography. https://conservancy.umn.edu/items/cb39d759-9a27-4a46-8428-a77471460e66
- Newmark, G. L. (2024). *Assessing GTFS Accuracy*. Mineta Transportation Institute / ROSA P. https://rosap.ntl.bts.gov/view/dot/77205

### Références internes du dépôt

- [`sources/transport-collectif-gtfs-quebec.md`](../sources/transport-collectif-gtfs-quebec.md) — répertoire des ressources GTFS et transport collectif au Québec.
- [`sources/voies-reservees-hov-hot.md`](../sources/voies-reservees-hov-hot.md) — voies réservées et gérées.
- [`methodes/comparabilite-des-donnees-mobilite.md`](comparabilite-des-donnees-mobilite.md) — règles de comparabilité, métadonnées et limites.

## Journal de maintenance

- 2026-08-14 — Création du guide. Les propositions P1 à P4 sont classées comme hypothèses non validées ; les formules opérationnelles sont volontairement renvoyées aux références à jour et aux scripts versionnés.
