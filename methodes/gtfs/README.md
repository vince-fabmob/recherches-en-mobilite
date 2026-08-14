# Scripts GTFS — offre planifiée

## Objet

Ce répertoire contient des scripts Python reproductibles pour analyser un **GTFS statique**. Les résultats décrivent une offre planifiée : ils ne constituent pas des mesures de l’exploitation réelle.

La documentation méthodologique générale est disponible dans [Valorisation des données GTFS et capacité des services d’autobus](../valorisation-donnees-gtfs-et-capacite-bus.md).

## Statuts des scripts

| Statut | Signification |
|---|---|
| Implémentation d’une méthode établie | Code appliquant un principe documenté dans une source de référence ; les paramètres et résultats doivent rester traçables |
| Proposition méthodologique non validée | Hypothèse de travail ou scénario à tester ; ne pas l’interpréter comme une norme ou une mesure observée |

Chaque script doit inclure en tête : statut, référence, données requises, sortie, hypothèses, méthode de validation, limites et date de vérification.

## Prérequis

- Python 3.10 ou plus récent
- `pandas`
- Un GTFS statique sous forme de dossier ou d’archive `.zip`

Installation minimale :

```bash
pip install pandas
```

## Script disponible

### `calcul-offre-horaire-gtfs.py`

**Produit :** le nombre de voyages programmés par heure à un arrêt donné, pour une date de service, avec filtre optionnel par direction.

**Fichiers requis :**

- `trips.txt`
- `stop_times.txt`
- au moins un des fichiers de calendrier : `calendar.txt` ou `calendar_dates.txt`

**Fichiers GTFS utiles à consulter en parallèle :** `stops.txt`, `routes.txt`, `agency.txt` et `feed_info.txt`. Ils servent à vérifier les identifiants, les libellés, le producteur du GTFS et sa période de validité.

### Exemple d’exécution

```bash
python methodes/gtfs/calcul-offre-horaire-gtfs.py \
  --gtfs donnees/gtfs.zip \
  --date 2026-09-15 \
  --stop-id 12345 \
  --direction-id 0 \
  --start-hour 6 \
  --end-hour 10 \
  --output sorties/offre_horaire.csv
```

Arguments :

| Argument | Rôle |
|---|---|
| `--gtfs` | Dossier GTFS ou archive `.zip` |
| `--date` | Date de service au format `AAAA-MM-JJ` ; le script applique les règles de `calendar.txt` et `calendar_dates.txt` |
| `--stop-id` | Identifiant exact de l’arrêt dans `stops.txt` |
| `--direction-id` | Filtre optionnel correspondant à `trips.txt` ; ne pas présumer que `0` et `1` ont la même signification entre réseaux |
| `--start-hour` | Première heure incluse ; valeur par défaut : `0` |
| `--end-hour` | Première heure exclue ; valeur par défaut : `30` afin de conserver les heures GTFS après minuit |
| `--output` | Chemin CSV optionnel ; sans cet argument, le résultat est affiché à l’écran |

### Sortie

| Colonne | Description | Statut |
|---|---|---|
| `hour` | Heure GTFS de début de la fenêtre `[HH:00:00, HH+1:00:00[` | Planifié |
| `route_id` | Identifiant technique de ligne GTFS | Planifié |
| `voyages_programmes` | Nombre de `trip_id` distincts pour la ligne, l’arrêt et l’heure | Planifié |
| `voyages_programmes_total` | Nombre total de `trip_id` distincts toutes lignes confondues | Planifié |

Le script utilise `departure_time` si elle existe ; autrement, il utilise `arrival_time`. Il accepte les heures GTFS supérieures à 24:00:00, qui représentent généralement un service poursuivi après minuit dans le même jour de service.

## Choisir la date et le point de mesure

### Jour de service

Choisir une date précise appartenant à la période de validité du GTFS. Ne pas présenter une date donnée comme un « jour moyen » sans démontrer sa représentativité. Les jours fériés, vacances, périodes d’été, périodes scolaires, travaux et événements peuvent produire une offre très différente.

Pour une comparaison, documenter au minimum :

- les dates exactes et versions de GTFS ;
- le type de jour visé : semaine scolaire, semaine estivale, samedi, dimanche ou jour férié ;
- les `service_id` actifs ;
- les exceptions appliquées par `calendar_dates.txt`.

### Arrêt, direction et point de coupure

Un comptage à un arrêt mesure les passages programmés à cet arrêt, pas nécessairement le débit d’un corridor entier. Pour comparer une voie réservée, un axe ou un tronçon, choisir un **point de coupure** explicite et vérifier :

- que toutes les variantes pertinentes le traversent ;
- qu’aucune course courte ou branche locale ne fausse l’interprétation ;
- que le sens retenu est documenté ;
- que les changements d’arrêt ou de tracé entre deux versions GTFS sont traités.

## Services `frequencies.txt`

Le script disponible ne développe pas automatiquement les voyages décrits par `frequencies.txt`. Il ne faut donc pas l’utiliser seul pour un réseau ou une ligne dont l’offre repose sur ce fichier.

Avant publication, vérifier :

1. Si `frequencies.txt` est absent, vide ou non pertinent pour les lignes étudiées.
2. Si le fichier est utilisé, appliquer la spécification GTFS correspondante pour développer les départs ou adapter le script ; documenter le traitement de `exact_times`.
3. Si la méthode ne peut pas être appliquée, signaler explicitement que le résultat sous-estime ou exclut cette portion de l’offre.

## Protocole minimal de validation

Avant de diffuser un résultat :

1. Vérifier la provenance, la date de publication, la validité et la licence du GTFS.
2. Contrôler quelques arrêts, lignes et heures contre les horaires publics de l’opérateur.
3. Vérifier les services actifs pour la date choisie et les exceptions de calendrier.
4. Contrôler les valeurs aberrantes : heures manquantes, heures invalides, `trip_id` dupliqués ou arrêts incohérents.
5. Vérifier la signification locale de `direction_id` et des identifiants de ligne.
6. Comparer, lorsque possible, les passages programmés avec AVL/GPS, GTFS-Realtime, données de contrôle ou observations de terrain.
7. Archiver ou identifier la version exacte du GTFS et la version du script utilisée.

## Interprétation correcte

| Énoncé acceptable | Énoncé à éviter sans données observées |
|---|---|
| « 18 voyages sont programmés entre 7 h et 8 h à cet arrêt, pour la date de service étudiée. » | « 18 autobus circulent réellement entre 7 h et 8 h. » |
| « Le temps prévu à l’horaire a diminué entre deux versions GTFS. » | « La vitesse commerciale réelle a augmenté. » |
| « La capacité d’offre théorique est estimée à partir d’une hypothèse de capacité et de charge. » | « Le corridor transporte ce nombre de personnes. » |

## Limites communes

Les scripts GTFS statiques ne mesurent pas directement :

- les retards, annulations, détournements et temps de parcours réellement observés ;
- la fiabilité et la régularité effective ;
- les montées, descentes, charges à bord ou refus d’embarquement ;
- les temps d’arrêt réels ;
- la capacité effective d’un arrêt, d’une station ou d’une voie réservée.

La capacité d’une installation d’autobus doit être évaluée avec des données d’infrastructure et d’exploitation appropriées, notamment selon le *Transit Capacity and Quality of Service Manual* (TCQSM).

## Références

- [Guide méthodologique GTFS et capacité des services d’autobus](../valorisation-donnees-gtfs-et-capacite-bus.md)
- [Répertoire de ressources GTFS et transport collectif au Québec](../../sources/transport-collectif-gtfs-quebec.md)
- [MobilitéData — GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
- Transportation Research Board — *Transit Capacity and Quality of Service Manual* : https://onlinepubs.trb.org/onlinepubs/tcrp/tcrp_rpt_165ch-01.pdf

## Journal de maintenance

- 2026-08-14 — Création du README et documentation de `calcul-offre-horaire-gtfs.py`.
