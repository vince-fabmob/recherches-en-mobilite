# Zones FLEX Communauto — couche indicative

## Statut

**Non officielle et non à jour.** Cette ressource est proposée uniquement pour l’analyse, la visualisation et le partage d’hypothèses de trajet. Elle ne constitue pas une carte de service, une garantie de stationnement ni une autorisation de terminer un trajet.

Des zones FLEX ont été ajoutées ou modifiées depuis la dernière observation ayant servi à compiler la couche. Par conséquent, le dépôt ne publie pas encore de fichier GeoJSON de référence : une géométrie périmée risquerait d’induire les utilisateurs en erreur.

## Règle d’utilisation

Toujours valider dans l’application Communauto, au moment du déplacement :

- la disponibilité du véhicule;
- la possibilité de commencer et de terminer le trajet;
- les restrictions de stationnement applicables à la rue choisie.

## Publication d’une future couche

Un fichier `communauto-flex-zones-indicatives.geojson` pourra être ajouté après une nouvelle compilation complète des zones. Il devra inclure les métadonnées suivantes : `status: non_official`, `observed_at`, `last_reviewed`, `coverage_limitations`, `source_method` et un avertissement d’usage.

## Sources à consulter

- https://montreal.communauto.com/fonctionnement/
- https://montreal.communauto.com/guide-de-stationnement/
- https://montreal.communauto.com/tarifs/
