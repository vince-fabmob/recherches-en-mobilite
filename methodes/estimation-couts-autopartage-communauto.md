# Méthodologie d'estimation des coûts d'autopartage à Montréal (Communauto, Leo Autopartage)

## Objectif

Documenter, de façon descriptive et factuelle, la structure de facturation utilisée
par les principaux opérateurs d'autopartage à Montréal (Communauto et Leo
Autopartage) afin de permettre l'estimation du coût d'un trajet à partir des
règles publiées par les producteurs. Cette fiche décrit une méthode de calcul ;
elle ne reproduit pas les grilles tarifaires complètes des opérateurs, celles-ci
étant sujettes à changement et devant être vérifiées directement à la source
avant tout usage décisionnel.

## Sources primaires

- **Communauto (Montréal)** — [Tarifs Communauto](https://montreal.communauto.com/tarifs/) — date de consultation : 2026-08-10
- **Leo Autopartage** — [Tarifs Leo Autopartage](https://leoautopartage.com/tarifs/) — date de consultation : 2026-08-10

Les montants numériques affichés sur la page Communauto sont générés
dynamiquement (calculateur interactif) et ne sont pas systématiquement
présents dans le contenu statique de la page ; la structure de facturation et
les règles de calcul décrites ci-dessous, elles, sont explicitement publiées.

## Modèle général de facturation Communauto

Communauto distingue deux modes de tarification, applicables selon le type de
véhicule utilisé :

### 1. Véhicule « en station »

Formule générique, telle que décrite par le producteur :

```
Coût_station = min(durée × tarif_horaire_du_forfait, plafond_journalier_du_forfait)
             + max(0, km_parcourus − km_inclus) × tarif_par_km_du_forfait
             + supplément_samedi_dimanche (si applicable)
             + exonération_de_dommages (si l'option est souscrite)
             + taxes
```

- Le tarif horaire, le plafond journalier, le seuil de kilomètres inclus et le
  tarif par kilomètre excédentaire dépendent du forfait souscrit (Liberté,
  Liberté Plus, Économique, Économique Plus, Économique Extra) et doivent être
  vérifiés au calculateur officiel au moment du calcul.
- La durée minimale de réservation d'un véhicule en station est de 30 minutes.
- Les forfaits Économique Plus et Économique Extra incluent une plage horaire
  gratuite entre 1 h et 6 h lorsque le trajet est facturé au tarif « en
  station ».
- Le forfait Économique Extra donne accès à un tarif « Travail » forfaitaire
  (jour de semaine seulement, maximum 10 heures consécutives, plage non
  comptabilisée de minuit à 6 h).

### 2. Véhicule FLEX (libre-service, sans réservation de retour à une station)

```
Coût_FLEX = min(durée_min × tarif_minute, plafond_horaire, plafond_journalier)
          + max(0, km_parcourus − km_inclus) × tarif_par_km
```

- Communauto applique automatiquement le tarif le plus bas entre le calcul
  FLEX ci-dessus et le calcul « en station » du forfait de l'usager — la
  comparaison est faite systématiquement, quelle que soit la durée du trajet.
- Si le tarif finalement appliqué est celui du véhicule en station, un minimum
  de 4 heures est facturable même si le trajet est plus court. Il n'y a pas de
  minimum d'heures facturables lorsque le tarif FLEX s'applique.
- À partir de 4 heures de trajet, les deux grilles tendent à converger vers un
  montant similaire.
- Un « laissez-passer FLEX », offert à prix réduit aux détenteurs d'un forfait
  Économique, rend gratuits les trajets FLEX de 30 minutes ou moins ; la
  facturation ne débute qu'à la 31ᵉ minute.
- Le supplément du samedi et du dimanche ne s'applique pas aux trajets FLEX.

### 3. Tarif longue distance

Réservé aux détenteurs d'un forfait de la formule Économique. S'applique aux
trajets nécessitant un grand nombre de kilomètres, avec un prix forfaitaire à
la journée ou à la semaine (essence incluse), appliqué automatiquement lorsque
plus avantageux. Un supplément horaire s'applique pour chaque heure excédant le
forfait, jusqu'à concurrence du tarif journalier. Les seuils de kilomètres
inclus et les tarifs diffèrent entre la basse saison (16 octobre – 14 juin) et
la haute saison (15 juin – 15 octobre).

## Modèle général de facturation Leo Autopartage

Leo publie des forfaits par tranche de durée (à la minute, à l'heure, à la
journée), chacun incluant un même seuil de kilomètres, à sommer avec deux frais
fixes appliqués à chaque trajet :

```
Coût_Leo = forfait_de_durée_choisi
         + max(0, km_parcourus − km_inclus_du_forfait) × tarif_par_km_excédentaire
         + frais_d_accès_fixe
         + frais_d_assurance_fixe
         + taxes
```

Exemple de calcul publié par l'opérateur (Mile-End → Verdun, 32 minutes,
trajet court) : 30 minutes (9,50 $) + 2 minutes excédentaires (2 × 0,43 $) +
frais d'accès (1,49 $) + assurance (1,99 $) = 13,84 $ avant taxes ([Leo Autopartage — Tarifs](https://leoautopartage.com/tarifs/)).

## Exemples de calculs publiés par les opérateurs

Les exemples suivants sont repris tels que publiés par les producteurs à des
fins d'illustration de la méthode ; ils ne constituent pas une grille
tarifaire à jour et doivent être revérifiés à la source avant tout usage.

| Cas illustré | Opérateur | Paramètres | Résultat publié | Source |
|---|---|---|---|---|
| Aller-retour rapide, tarif préférentiel automatique | Communauto | 1 h, 60 km | 24,15 $ (tarif préférentiel) vs 31,90 $ (forfait Économique) vs 27,10 $ (forfait Économique Plus) | [Tarifs Communauto](https://montreal.communauto.com/tarifs/) |
| Abonnement familial, 3 membres | Communauto | Forfait Économique Extra | 37,50 $/mois facturés au lieu de 90 $ (30 $ × 3), soit une économie annoncée de près de 60 % | [Tarifs Communauto](https://montreal.communauto.com/tarifs/) |
| Trajet court urbain | Leo Autopartage | Mile-End → Verdun, 32 min | 13,84 $ avant taxes | [Tarifs Leo Autopartage](https://leoautopartage.com/tarifs/) |
| Escapade de fin de semaine | Leo Autopartage | Montréal → Saint-Sauveur, 2 jours 2 h 2 min, 150 km | 146,34 $ avant taxes | [Tarifs Leo Autopartage](https://leoautopartage.com/tarifs/) |

## Éléments à valider à la source avant tout calcul

Les paramètres suivants varient selon le forfait souscrit et sont modifiés
périodiquement par les opérateurs. Ils doivent être confirmés au calculateur
officiel ou dans l'application au moment du calcul plutôt que présumés fixes :

- Frais d'abonnement (mensuel ou annuel) par forfait
- Tarif horaire et plafond journalier « en station » par forfait
- Tarif par minute, plafond horaire et plafond journalier FLEX
- Seuil de kilomètres inclus et tarif par kilomètre excédentaire
- Coût du laissez-passer FLEX (illimité ou par nombre de trajets)
- Suppléments (fin de semaine, véhicule familial, minifourgonnette)
- Options et coûts d'exonération de dommages collision

## Limites méthodologiques

- Le calculateur de prix intégré à la page Communauto repose sur un rendu
  dynamique (JavaScript) ; les montants ne sont donc pas nécessairement
  extractibles d'une simple lecture du contenu statique de la page.
- Les grilles tarifaires des deux opérateurs sont sujettes à modification sans
  préavis. Toute estimation produite avec cette méthode a une durée de validité
  limitée et doit être recalculée avec les paramètres en vigueur à la date du
  trajet.
- Cette fiche ne reproduit aucune donnée personnelle ni aucun historique de
  trajet ; elle documente uniquement la structure de calcul publiée par les
  producteurs.

## Documentation associée

- [Tarifs Communauto — Montréal](https://montreal.communauto.com/tarifs/)
- [Tarifs Leo Autopartage](https://leoautopartage.com/tarifs/)

## Mots-clés

`autopartage` · `Communauto` · `Leo Autopartage` · `tarification` · `FLEX` · `Montréal` · `méthode de calcul`
