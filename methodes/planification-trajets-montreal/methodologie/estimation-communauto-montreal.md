# Estimation Communauto — Montréal

## Objet

Méthode d’estimation d’un déplacement Communauto avec le forfait par défaut **Économique Extra**. Elle compare une option FLEX à une option stationnaire et ne remplace ni la facture réelle ni l’application Communauto.

## Entrées

- `duration_minutes` : durée totale prévue;
- `distance_km` : distance facturable prévue;
- `origin` et `destination`;
- `trip_type` : `flex`, `station_based` ou `unknown`;
- `destination_flex_eligible` : `true`, `false` ou `unknown`.

Si une entrée est inconnue, afficher une estimation incomplète.

## FLEX

```text
flex_cost = min(duration_minutes × 0.43, ceil(duration_minutes / 60) × 14.25)
```

Cette formule simplifie le tarif minute et le plafond horaire de référence. Vérifier la grille officielle, les taxes, les kilomètres, les plafonds et les règles applicables avant un calcul de production.

## Stationnaire et optimisation

```text
station_cost = tariff_economique_extra(duration_minutes, distance_km, applicable_rules)
recommended_cost = min(flex_cost, station_cost)
```

Une recommandation FLEX est admissible seulement si un véhicule est disponible et si l’application confirme la fin de trajet à destination. Si la table Économique Extra n’a pas été validée, retourner `manual_verification_required`.

## Source

- https://montreal.communauto.com/tarifs/
