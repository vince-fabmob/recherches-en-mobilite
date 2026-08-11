# Planification de trajets et estimation des coûts — Montréal

> **Conception et validation.** Ce planificateur a été conçu et testé avec **Perplexity**, qui navigue vers l’URL de ce README, suit ses liens relatifs et charge les fichiers JSON de règles tarifaires dans `donnees/`. Son comportement avec d’autres IA génératives n’est pas garanti : certaines ne suivent pas les liens relatifs ou ne naviguent pas du tout. Voir la section [Compatibilité IA](#compatibilité-ia) avant de vous fier aux résultats obtenus avec un autre outil.

## Utilisation avec une IA générative

Utilisez cette page comme point d’entrée pour planifier un trajet à Montréal et comparer les coûts. Fournissez à l’IA l’origine, la destination, la date et l’heure, le nombre de voyageurs, ainsi que vos contraintes (temps, budget, bagages, accessibilité).

Prompt suggéré :

> Utilise les méthodes et outils de cette page pour comparer les itinéraires et estimer le coût d’un trajet à Montréal. Indique les hypothèses, les liens de planification utilisés, le coût obligatoire avant et après taxes, et sépare le pourboire facultatif. Pour Communauto, utilise le forfait Économique Extra et compare station, FLEX et longue distance.

## Méthodes de calcul

- [Communauto — autopartage](../estimation-couts-autopartage-communauto.md)
- [BIXI](../estimation-couts-bixi.md)
- [Taxi](../estimation-couts-taxi.md)
- [VTC — Uber et Lyft](../estimation-couts-vtc.md)

## Planificateurs et sources

| Outil ou mode | Planifier ou estimer | Usage principal |
|---|---|---|
| Chrono (ARTM) | [Chrono](https://www.chronoapp.quebec/) | Planification dans le Grand Montréal, transport collectif, BIXI et autres modes disponibles; horaires et données temps réel. |
| Citymapper | [Citymapper — Montréal](https://citymapper.com/montreal) | Comparaison multimodale : transport collectif, marche, vélo/BIXI, taxi/VTC et autopartage selon les données disponibles. |
| Plans d’Apple | [Plans d’Apple](https://maps.apple.com/) | Itinéraires voiture, marche, vélo et transport collectif dans l’écosystème Apple. |
| Google Maps | [Google Maps — itinéraires](https://www.google.com/maps/dir/) | Itinéraires multimodaux et onglet **Courses** pour les options de VTC disponibles. |
| Transit | [Transit — Montréal](https://transitapp.com/fr/region/montreal) | Transport collectif, données temps réel et options multimodales disponibles. |
| Communauto | [Carte et réservation Communauto](https://montreal.communauto.com/?city=montreal) | Disponibilité et réservation; voir aussi les [tarifs](https://montreal.communauto.com/tarifs/). |
| BIXI | [Carte BIXI](https://bixi.com/fr/) | Stations, disponibilité et itinéraires; voir aussi les [tarifs](https://bixi.com/fr/tarifs/). |
| Taxi | [Estimateur Uber Taxi](https://www.uber.com/global/fr-ca/r/taxi-calculator/) | Estimation complémentaire; vérifier les [tarifs officiels du taxi](https://mtl.taxi/en/fares). |
| VTC | [Estimateur Uber](https://www.uber.com/global/en/price-estimate/) et [Lyft — estimation](https://help.lyft.com/hc/en-ca/all/articles/115013080308-How-to-estimate-the-cost-of-a-Lyft-ride) | Prix dynamique par catégorie, à vérifier immédiatement avant la réservation. |

Pour une comparaison large des modes à Montréal, Citymapper est l’outil commercial le plus complet de cette liste : il peut comparer le transport collectif, la marche, le vélo/BIXI, le taxi/VTC et l’autopartage lorsque ces données sont intégrées. Chrono est la référence institutionnelle pour le Grand Montréal, notamment pour le transport collectif, BIXI et l’information temps réel.

Dans Google Maps, saisissez l’origine et la destination, puis sélectionnez l’onglet **Courses** pour comparer les options de transport avec chauffeur offertes au moment de la recherche. Les prix de VTC sont des estimations temps réel : ils peuvent changer avant la réservation.

## Planificateurs open source

Ces solutions sont surtout destinées aux organismes, aux développeurs et aux projets qui souhaitent déployer ou intégrer leur propre planificateur. Elles ne constituent pas nécessairement un service prêt à l’emploi pour Montréal.

| Projet | Rôle et capacités | Lien |
|---|---|---|
| OpenTripPlanner (OTP) | Moteur open source de planification multimodale combinant transport collectif, marche, vélo et services de mobilité à partir notamment de GTFS, GTFS-RT et OpenStreetMap. | [Projet](https://www.opentripplanner.org/) · [Code](https://github.com/opentripplanner/OpenTripPlanner) |
| Digitransit | Plateforme open source complète, combinant OTP, interface Web/mobile, géocodage et fonds de carte. | [Code](https://github.com/HSLdevcom/digitransit) |
| MOTIS | Plateforme open source de routage multimodal, de géocodage et d’API; intègre transport collectif, marche, vélo et mobilité partagée. | [Code](https://github.com/motis-project/motis) |
| Navitia | Moteur et API open source pour le calcul d’itinéraires multimodaux, les horaires, départs, arrêts et isochrones. | [Code](https://github.com/hove-io/navitia) |
| Transitous | Instance publique fondée sur MOTIS, avec couverture dépendante des données ouvertes disponibles; vérifier sa politique d’utilisation avant toute intégration. | [API](https://api.transitous.org/) |

## Compatibilité IA

Ce README est un **index** : il renvoie vers des fichiers séparés (méthodes de calcul, règles tarifaires JSON dans `donnees/`, scripts, tests). Partager uniquement l’URL du README suffit seulement si l’IA de destination navigue activement vers cette page **et** suit ses liens relatifs pour charger ces fichiers. Certaines IA affichent une réponse plausible sans avoir réellement chargé les règles — vérifiez toujours les montants obtenus avant de les considérer fiables.

### Procédure de test à deux niveaux

1. **Test « lien seul »** : collez uniquement l’URL de ce README dans l’IA et posez une question de trajet incluant Communauto. Notez si l’IA cite des montants cohérents avec les règles de `donnees/tarifs-communauto.json` et `donnees/tarifs-communauto-longue-distance.json`.
2. **Test « contenu collé »** : si le test 1 échoue ou semble incohérent, collez manuellement le contenu de ce README et des fichiers JSON pertinents, puis reposez la même question. Un succès ici mais un échec au test 1 indique un problème de navigation, pas de raisonnement.

### Tableau à mettre à jour au fil des tests

| IA | Suit les liens du README | Charge les JSON de tarifs | Applique les règles de calcul | Notes |
|---|---|---|---|---|
| Perplexity | ✅ | ✅ | ✅ | Utilisé pour concevoir et valider ce planificateur. |
| ChatGPT | à tester | à tester | à tester | |
| Gemini | à tester | à tester | à tester | |
| Copilot | à tester | à tester | à tester | |
| Claude | à tester | à tester | à tester | |

Mettez à jour ce tableau par pull request au fur et à mesure de vos tests et de ceux de vos testeurs.

### À venir

Un fichier « bundle » unique, concaténant ce README et les règles tarifaires, pourra être ajouté pour les IA sans navigation fiable, afin qu’un simple copier-coller remplace la navigation multi-fichiers.

## Données à fournir

- Origine et destination précises
- Date et heure de départ ou d’arrivée
- Nombre de voyageurs et bagages
- Durée prévue d’une location, si applicable
- Abonnements pertinents : Communauto Économique Extra, BIXI membre, transport collectif
- Priorité : coût, rapidité, confort, accessibilité ou émissions

## Limites

Les résultats sont des estimations. Vérifiez toujours la disponibilité des véhicules, les conditions de circulation, les travaux, les tarifs affichés au moment de réserver et les frais additionnels éventuels.
