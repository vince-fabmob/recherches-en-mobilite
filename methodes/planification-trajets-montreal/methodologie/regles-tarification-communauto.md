# Règles de tarification Communauto

## Objectif

Produire une estimation qui dépend du forfait détenu par l’utilisateur, des caractéristiques réelles du trajet et de la grille tarifaire officielle en vigueur.

## Source de vérité

Les tarifs numériques sont conservés dans `donnees/tarifs-communauto.json`. Ce fichier prévaut sur les exemples, les prompts, les anciennes estimations et tout texte explicatif. Chaque tarif doit inclure une date de vérification et l’URL de la source officielle.

## Ordre de décision

1. Identifier le forfait actif de l’utilisateur.
2. Si le forfait est inconnu, poser une seule question : « Quel forfait Communauto avez-vous actuellement : FLEX sans forfait, Économique, Économique Extra, ou un laissez-passer FLEX actif? »
3. Identifier le type de véhicule : FLEX ou véhicule en station.
4. Vérifier si le départ et la destination permettent de commencer et de fermer le trajet dans l’application.
5. Estimer la durée réelle : marche vers le véhicule, déverrouillage, conduite, recherche de stationnement et fermeture du trajet.
6. Charger uniquement les tarifs, plafonds, kilomètres inclus et avantages associés au forfait actif.
7. Évaluer les calculs admissibles selon la grille officielle, incluant le mécanisme du meilleur tarif lorsqu’il existe.
8. Afficher le coût avant taxes et taxes incluses, avec le forfait et les hypothèses utilisés.

## Règles FLEX

- Ne jamais appliquer un prix fixe FLEX sans confirmer le forfait ou le laissez-passer actif.
- Un prix de laissez-passer ne s’applique que si sa durée maximale, ses kilomètres inclus, ses conditions de fermeture et ses exclusions sont respectés.
- Si la durée estimée franchit un seuil tarifaire, afficher une fourchette et expliquer le seuil.
- Une destination dans une zone FLEX n’est pas une garantie de stationnement : la possibilité de fermer le trajet doit être confirmée dans l’application.

## Niveau de confiance

- **Confirmé** : forfait, grille tarifaire, véhicule et conditions de fin vérifiés.
- **Estimation** : distance et durée estimées, mais disponibilité ou stationnement non confirmés.
- **À confirmer dans l’application** : zone, véhicule, stationnement ou tarif manquant.

## Format de réponse

> Forfait utilisé : [nom du forfait].
>
> Hypothèses : [durée], [distance], [FLEX ou station], [fin de trajet].
>
> Estimation : [montant] avant taxes, soit [montant] taxes incluses.
>
> Niveau de confiance : [confirmé / estimation / à confirmer dans l’application].
