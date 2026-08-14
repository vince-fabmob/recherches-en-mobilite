# Données GTFS et temps réel de transport collectif au Québec

> **Document de travail — à réviser collectivement.** Ce répertoire recense des ressources publiques décrivant l’offre de transport collectif au Québec, notamment les fichiers GTFS et les flux temps réel. Il ne reproduit pas les données. Vérifier la licence, l’URL active, la fréquence de mise à jour, les modalités d’accès et la documentation de chaque organisme avant toute utilisation.
>
> **Contributions bienvenues.** Les liens manquants, changements d’API, précisions sur les licences et nouveaux producteurs peuvent être proposés par issue ou pull request. Consultez [CONTRIBUTING.md](../CONTRIBUTING.md).

## Objet

Les données GTFS et GTFS-Realtime décrivent principalement l’offre de service de transport collectif : agences, arrêts, lignes, trajets, horaires, calendriers, positions de véhicules, alertes et mises à jour. Elles ne constituent pas, à elles seules, des mesures de l’achalandage, des déplacements de personnes, de l’occupation des véhicules ou de la performance complète d’un réseau.

## Formats à distinguer

| Format ou ressource | Usage principal | Limite importante |
|---|---|---|
| GTFS statique | Offre planifiée : arrêts, lignes, horaires, trajets et calendriers | Ne décrit pas nécessairement le service réellement effectué ni la demande |
| GTFS-Realtime | Mises à jour de trajets, positions de véhicules et alertes de service | La disponibilité, la qualité et l’historique varient selon l’opérateur |
| TCIP | Échanges d’information de transport collectif utilisés par certains réseaux | Les modalités d’accès et les versions doivent être vérifiées auprès de l’opérateur |
| API ou portail développeurs | Diffusion de données et services numériques | Les conditions d’utilisation, quotas et clés d’accès peuvent changer |

## Répertoire québécois

| Organisme | Ressources publiques à vérifier | Territoire ou réseau | Accès et précautions |
|---|---|---|---|
| [STM — Espace développeurs](https://www.stm.info/fr/a-propos/developpeurs) | Horaires, réseau, information voyageurs, données GTFS et flux temps réel selon les ressources disponibles | Île de Montréal | Distinguer offre planifiée, données temps réel et achalandage. Vérifier les conditions d’utilisation et les API actives. |
| [exo — Données ouvertes](https://exo.quebec/fr/a-propos/donnees-ouvertes) | Données GTFS planifiées; données GTFS-Realtime et TCIP pour les trains de banlieue selon les modalités publiées | Couronnes métropolitaines et réseau exo | Les données temps réel des trains de banlieue peuvent nécessiter une demande d’accès. Vérifier la licence et la fraîcheur des fichiers. |
| [STL — Données ouvertes](https://stlaval.ca/a-propos/informations-publiques/donnees-ouvertes) | Horaires planifiés et information temps réel publiée pour les développeurs | Laval | Vérifier les conditions applicables aux données planifiées et temps réel, ainsi que les ressources disponibles. |
| [RTL](https://www.rtl-longueuil.qc.ca/) | Informations voyageurs, horaires et ressources numériques à vérifier | Longueuil et agglomération | Identifier les éventuels fichiers GTFS, API ou flux temps réel publiés par le réseau avant réutilisation. |
| [RTC — Données ouvertes](https://www.rtcquebec.ca/fr/a-propos/donnees-ouvertes) | GTFS : arrêts, horaires et parcours; ressources géospatiales associées | Québec et environs | Les ressources GTFS décrivent l’offre. Les jeux publiés dans Données Québec doivent être vérifiés quant à leur date et leur licence. |
| [STO — Espace développeurs](https://www.sto.ca/fr/espace-affaires/espace-developpeurs-donnees-ouvertes/) | GTFS planifié et GTFS-Realtime | Gatineau | Les flux temps réel peuvent nécessiter une clé API; vérifier les conditions et limites d’utilisation. |
| [Société des traversiers du Québec](https://www.donneesquebec.ca/recherche/dataset?tags=GTFS) | GTFS pour les traverses | Québec | Le GTFS décrit les horaires et l’offre de traverses; il ne mesure pas les passagers, véhicules embarqués ni le fret. |
| [ARTM](https://www.artm.quebec/) | Informations et outils régionaux à vérifier; l’ARTM n’est pas nécessairement le producteur direct de tous les flux GTFS des opérateurs | Région métropolitaine de Montréal | Identifier l’opérateur producteur, la version du fichier et la licence avant d’agréger des données régionales. |

## Ressources de catalogage

| Organisme | Ressource | Utilité |
|---|---|---|
| [Données Québec — jeux GTFS](https://www.donneesquebec.ca/recherche/dataset/?tags=GTFS) | Catalogue de jeux GTFS publiés par divers organismes | Point d’entrée pour repérer des producteurs québécois; vérifier chaque fiche source |
| [Statistique Canada — Base de données sur les réseaux de transport en commun du Canada](https://www150.statcan.gc.ca/n1/fr/catalogue/23260003) | Base consolidée de données GTFS statiques de réseaux canadiens | Comparaison et cartographie nationale; ne remplace pas nécessairement la publication locale la plus récente |
| [Transport Canada — Transportation Data and Information Hub](https://tdih-cdit.tc.canada.ca/en) | Portail fédéral de données, rapports et cartes sur les transports | Point d’entrée complémentaire pour données nationales et interurbaines |

## Usages possibles

- Cartographier les arrêts, lignes, calendriers et fréquences planifiées.
- Calculer des indicateurs d’offre, de couverture ou de temps de parcours théoriques.
- Construire des analyses multimodales avec des données de marche, vélo, réseau routier ou partage.
- Documenter les modifications d’offre et les perturbations lorsqu’un flux temps réel ou un historique est disponible.
- Comparer la structure de l’offre entre réseaux, après harmonisation des périodes et définitions.

## Limites et précautions

- GTFS ne mesure pas directement les déplacements réalisés, les correspondances effectivement effectuées, l’occupation ni l’achalandage.
- Un horaire planifié peut différer de l’offre réellement effectuée en raison d’annulations, travaux, congestion, météo ou aléas d’exploitation.
- Les fichiers GTFS de réseaux différents peuvent utiliser des conventions et calendriers différents.
- Les flux GTFS-Realtime sont souvent éphémères; leur archivage et leur accès historique doivent être confirmés avant toute analyse de fiabilité.
- Les comparaisons entre réseaux doivent contrôler le territoire, la période, les jours de service, les règles de fréquence et les définitions de ligne, trajet ou arrêt.
- La licence, les conditions d’API et les règles d’attribution doivent être vérifiées individuellement.

## Ressources associées

- [Producteurs de données de mobilité au Québec](producteurs-donnees-mobilite-quebec.md)
- [Guide de comparabilité des données de mobilité](../methodes/comparabilite-des-donnees-mobilite.md)
- [ARTM — Enquête métropolitaine 2023](transport-montreal/artm-enquete-metropolitaine-2023.md)

## À compléter

- [ ] Ajouter les liens directs vers les fichiers GTFS et API lorsque les producteurs les publient officiellement.
- [ ] Ajouter les autres sociétés de transport du Québec et les réseaux interurbains disposant de ressources publiques.
- [ ] Documenter séparément les données d’achalandage ouvertes, lorsqu’elles existent.
- [ ] Ajouter les licences, fréquences de mise à jour et conditions d’accès par réseau.
- [ ] Vérifier la disponibilité de données temps réel pour chaque opérateur.

*Dernière vérification : 13 août 2026.*
