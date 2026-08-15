# Vitesse commerciale programmée par corridor GTFS

## Statut

**Implémentation reproductible indicative d’une méthode établie.** Le calcul décrit une vitesse prévue à l’horaire GTFS ; ce n’est pas une vitesse observée. Toute interprétation de la performance réelle exige une validation par AVL, GPS, GTFS-Realtime ou autre donnée opérationnelle.

## Objet

Cette méthode mesure le temps programmé entre deux arrêts-borne et la distance correspondante **le long du tracé GTFS** associé à chaque voyage. Elle vise des corridors longs, généralement de 1 à 3 km, afin d’atténuer l’influence d’un seul arrêt, feu ou arrondi d’horaire.

## Entrées

- GTFS statique : `trips.txt`, `stop_times.txt`, `stops.txt`, `shapes.txt`, et fichiers de calendrier.
- CSV de corridors : `corridor_id`, `corridor_name`, `from_stop_id`, `to_stop_id`.
- Date de service précise.
- Système de coordonnées métrique approprié au territoire ; le script utilise EPSG:32188 par défaut, adapté au Québec méridional.

## Méthode

1. Déterminer les `service_id` actifs à la date demandée.
2. Filtrer les voyages actifs et associer chaque voyage à son `shape_id`.
3. Vérifier que l’arrêt aval suit l’arrêt amont dans `stop_sequence`.
4. Définir le temps programmé comme le départ à l’arrêt amont jusqu’à l’arrivée à l’arrêt aval.
5. Reprojeter la forme et les arrêts dans un système métrique.
6. Projeter les deux arrêts-borne sur la forme associée au voyage.
7. Mesurer la différence de distance curviligne sur la forme.
8. Calculer une vitesse par voyage, puis agréger par corridor, ligne et direction.

## Contrôles et exclusions

Un voyage est exclu si un champ requis est absent, si la forme est invalide, si l’arrêt aval ne suit pas l’arrêt amont, si le temps ou la distance sont non positifs, ou si l’écart entre un arrêt et sa projection sur la forme dépasse `--max-stop-shape-error-m`.

Les fichiers de sortie indiquent la méthode de distance, l’erreur maximale arrêt–forme, les voyages retenus et les motifs d’exclusion. Une proportion élevée de voyages exclus doit être analysée avant toute diffusion.

## Agrégation

Le fichier corridor agrégé fournit :

- le nombre de voyages retenus ;
- la distance et le temps médians par voyage ;
- la vitesse médiane par voyage ;
- la vitesse pondérée, calculée comme somme des distances divisée par somme des temps ;
- l’erreur maximale d’appariement arrêt–forme.

La vitesse pondérée est la mesure de synthèse recommandée lorsque les variantes de tracé ou de distance diffèrent entre voyages.

## Interprétation

Utiliser les libellés **vitesse commerciale programmée** ou **vitesse prévue à l’horaire**. Ne pas conclure que les autobus atteignent réellement cette vitesse sans données observées.

## Limites

- La forme GTFS peut être imprécise ou non représentative d’un détournement.
- L’appariement d’un arrêt à une forme reste une approximation géométrique.
- Le GTFS ne contient généralement pas les retards, les temps d’arrêt réellement observés, les charges ou la fiabilité.
- Les comparaisons avant/après exigent des jours de service comparables, des bornes identiques et un contrôle des changements de parcours ou d’arrêts.

## Références

- GTFS Schedule Reference : https://gtfs.org/documentation/schedule/reference/
- GTFS Schedule Best Practices : https://gtfs.org/documentation/schedule/schedule-best-practices/
- Guide principal : [`valorisation-donnees-gtfs-et-capacite-bus.md`](../valorisation-donnees-gtfs-et-capacite-bus.md)
- README des scripts : [`README.md`](README.md)
