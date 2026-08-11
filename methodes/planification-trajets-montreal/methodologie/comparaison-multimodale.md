# Comparaison multimodale avec validation utilisateur

## Objectif

Comparer les options de déplacement à Montréal sans déclencher inutilement des requêtes vers des services externes. Le planificateur produit d'abord une pré-sélection locale, puis vérifie seulement les options approuvées par l'utilisateur.

## Étape 1 — Pré-sélection locale

À partir de l'origine, de la destination, de l'heure, des abonnements et des contraintes, retenir les modes plausibles :

- Transport collectif pour les déplacements urbains.
- Marche pour les courtes distances compatibles avec la contrainte de temps.
- BIXI si l'utilisateur accepte le vélo et si les conditions semblent compatibles.
- Communauto lorsque la durée, les bagages, l'horaire ou la destination le justifient.
- Taxi ou VTC lorsque la rapidité, les bagages, l'heure tardive ou l'accessibilité le justifient.

Cette étape emploie uniquement les règles et tarifs locaux disponibles. Elle ne prétend pas confirmer une disponibilité, une zone FLEX, un stationnement, un itinéraire temps réel ou un prix dynamique.

## Première réponse

Afficher les options plausibles dans un tableau comparatif avec :

- Temps porte à porte estimé.
- Coût estimé avant et après taxes lorsqu'il est calculable.
- Hypothèses et niveau de confiance.
- Action de confirmation requise, le cas échéant.

Puis poser une seule question :

> Souhaitez-vous une estimation seulement, ou voulez-vous que je vérifie les données actuelles? Si oui, quels modes dois-je vérifier?

Exemple : « Je peux vérifier seulement Communauto et STM, les deux meilleures options, ou tous les modes. »

## Étape 2 — Vérification dynamique approuvée

Ne vérifier que les modes explicitement choisis par l'utilisateur. À défaut de choix précis, vérifier au plus les deux options les mieux classées si l'utilisateur demande « les meilleures options ».

| Élément | Exemple de vérification |
|---|---|
| Transport collectif | Horaire, perturbations, durée et correspondances |
| BIXI | Disponibilité aux stations de départ et d'arrivée |
| Communauto | Véhicule, zone FLEX, possibilité de fermeture et tarif affiché |
| Taxi/VTC | Estimation dynamique et catégorie de véhicule |

## Niveaux de confiance

- **Estimation** : résultat calculé localement avec règles et données connues.
- **Confirmé** : donnée vérifiée dans une source actuelle ou l'application de l'opérateur.
- **À confirmer dans l'application** : disponibilité, stationnement, zone, véhicule ou prix dynamique non vérifié.

## Règles de sortie

- Toujours signaler les hypothèses.
- Ne pas présenter une estimation comme un prix garanti.
- Pour tout itinéraire extérieur, fournir un lien Google Maps facilement copiable.
- Respecter les abonnements déclarés; utiliser Économique Extra par défaut pour Communauto lorsque le forfait est inconnu dans ce projet.
- Ne pas appeler tous les services par défaut.

## Exemple

> Pré-sélection : STM (32 min), BIXI (25 min si météo favorable), Communauto FLEX (20 min, coût estimé), taxi/VTC (18 min, prix dynamique non vérifié).
>
> Voulez-vous que je vérifie maintenant STM et Communauto, les deux meilleures options, ou un autre groupe de modes?
