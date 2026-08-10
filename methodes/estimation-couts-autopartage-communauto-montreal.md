# Méthode d’estimation — Communauto Montréal

## Objet

Cette méthode produit une estimation pour un déplacement Communauto à Montréal avec le profil par défaut **Économique Extra**. Elle compare une option FLEX à une option avec véhicule stationnaire, sans se substituer à la facture réelle ni à l’application Communauto.

## Entrées minimales

- `duration_minutes` : durée totale prévue;
- `distance_km` : distance facturable prévue;
- `origin` et `destination` : adresses ou coordonnées;
- `trip_type` : `flex`, `station_based` ou `unknown`;
- `destination_flex_eligible` : `true`, `false` ou `unknown`.

Si la durée, la distance ou l’admissibilité de fin de trajet sont inconnues, le résultat doit être présenté comme incomplet.

## Calcul FLEX

À la date de vérification du jeu de données, le tarif FLEX de référence est :

```text
flex_cost = min(duration_minutes × 0.43, ceil(duration_minutes / 60) × 14.25)
```

Cette formule représente le tarif minute et le plafond horaire affichés. Avant un calcul de production, remplacer les constantes par la table tarifaire officielle en vigueur et appliquer ses règles de plafonds, de journées, de kilomètres, de taxes et de frais éventuels.

Un résultat FLEX est admissible uniquement si un véhicule est disponible, le trajet est compatible avec les règles de service et l’application confirme que la fin de trajet est autorisée.

## Calcul stationnaire — Économique Extra

La version de production doit stocker une table complète et datée du forfait Économique Extra :

```text
station_cost = tariff_economique_extra(duration_minutes, distance_km, applicable_rules)
```

Ne pas utiliser de valeur par défaut si la table tarifaire n’a pas été validée. Retourner plutôt `manual_verification_required`.

## Optimisation FLEX

Lorsque les deux scénarios sont admissibles et calculables :

```text
recommended_cost = min(flex_cost, station_cost)
recommended_option = argmin(flex_cost, station_cost)
```

La recommandation doit toujours expliciter les hypothèses et indiquer qu’il s’agit d’une estimation.

## Sources

- Tarifs Communauto Montréal : https://montreal.communauto.com/tarifs/
- Méthode de référence : https://github.com/vince-fabmob/recherches-en-mobilite/blob/main/methodes/estimation-couts-autopartage-communauto.md
