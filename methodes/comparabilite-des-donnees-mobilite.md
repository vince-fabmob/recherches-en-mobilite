# Comparabilité des données de mobilité

> **Document de travail — à réviser collectivement.** Cette page a été rédigée avec l’assistance de l’IA à partir de sources publiques et d’une première synthèse méthodologique. Elle ne constitue ni une norme officielle ni un avis professionnel. Avant toute utilisation analytique, décisionnelle ou publication, les définitions, valeurs, liens et interprétations doivent être vérifiés dans la documentation primaire de chaque source.
>
> **Contributions bienvenues.** Ce dépôt vise à rendre les informations publiques plus faciles à trouver, comprendre et réutiliser avec rigueur. Les personnes qui détiennent une expertise, connaissent une source ou repèrent une erreur sont invitées à proposer une correction, une nuance, une nouvelle référence ou un exemple via une issue ou une pull request. Consultez [CONTRIBUTING.md](../CONTRIBUTING.md).

## Objet

Les bases de données de mobilité mesurent rarement le même phénomène. Deux chiffres apparemment comparables peuvent en réalité viser des populations, territoires, jours, saisons, unités ou méthodes de collecte différents. Cette page fournit une grille de lecture pour documenter ces écarts avant de comparer, agréger ou interpréter des données.

**Principe directeur :** une comparaison n’est valide que si les univers observés et les définitions sont alignés, ou si les écarts restants sont explicitement documentés et justifiés.

## Grille de qualification minimale

Toute fiche source devrait, dans la mesure du possible, préciser :

| Champ | Question à documenter |
|---|---|
| Univers | Qui ou quoi est observé : résidents, visiteurs, ménages, personnes, véhicules, abonnés, validations ou appareils? |
| Géographie | Quel périmètre : municipalité, agglomération, CMM, territoire ARTM, zones OD, corridor, ligne ou station? |
| Unité | Que compte-t-on : personnes, déplacements, étapes, passages, validations, véhicules-km, personnes-km ou émissions? |
| Temps | Quelle période : jour moyen, jour ouvrable, pointe, mois, année ou période de collecte? |
| Saisonnalité | Quelles dates, saisons, vacances, périodes scolaires ou conditions météorologiques sont couvertes? |
| Méthode | Enquête déclarative, comptage, billettique, GPS, application, téléphonie mobile, capteur ou estimation modélisée? |
| Échantillon et pondération | Taille, taux de réponse, règles d’exclusion, pondérations et marges d’erreur? |
| Ruptures de série | Les définitions, questionnaires, méthodes, zonages, réseaux ou traitements ont-ils changé? |
| Accès et réutilisation | Données ouvertes, accès sur demande, agrégation, licence et restrictions de confidentialité? |

## Principaux défis

### Univers et population observée

Une enquête ménage décrit généralement les déplacements des résidents d’un territoire. Une validation de titre de transport mesure des transactions ou des montées, pas nécessairement des personnes uniques ni l’ensemble du trajet. Les données d’un service partagé reflètent les usagers de ce service, sans représenter automatiquement toute la population.

**Conséquence :** ne pas comparer directement un nombre de validations, de trajets BIXI, de véhicules observés et de déplacements de personnes sans expliciter l’unité et le dénominateur.

### Géographie et zonage

Les frontières administratives, aires de desserte, zones OD et bassins de déplacement ne coïncident pas toujours. Un indicateur pour l’île de Montréal ne peut pas être rapproché automatiquement d’un indicateur pour la région métropolitaine ou le territoire ARTM. Les modifications de zonage peuvent aussi créer des ruptures artificielles.

**Pratique recommandée :** privilégier les périmètres emboîtables; sinon, présenter les résultats côte à côte plutôt que de les agréger.

### Temporalité et calendrier

Un « jour moyen » peut désigner un jour ouvrable, une journée de semaine, une moyenne annuelle ou une période de collecte spécifique. Les pointes, les week-ends et les jours fériés répondent à des logiques différentes.

**Exemple :** l’Enquête métropolitaine 2023 de l’ARTM décrit un jour moyen de semaine à l’automne. Ses résultats ne caractérisent donc pas directement la mobilité des fins de semaine, des jours fériés ou des autres saisons.

### Saisonnalité et contexte

Le vélo, la marche, les déplacements de loisirs, le tourisme et certains usages du transport collectif varient fortement selon la saison, la météo, les vacances et les événements. Une différence entre deux années peut relever de ces facteurs plutôt que d’un changement structurel.

**Pratique recommandée :** comparer des fenêtres calendaires semblables et conserver les dates de collecte exactes.

### Unités, définitions et chaînes de déplacement

Un déplacement peut être défini par son origine et sa destination, alors qu’une étape correspond à une portion unimodale d’un trajet. Les véhicules-km, personnes-km, validations et passages répondent à des questions différentes.

**Pratique recommandée :** inscrire l’unité dans le titre de chaque graphique, tableau et ratio; ne pas employer « achalandage » ou « déplacements » sans définition.

### Méthodes de mesure et biais

Les enquêtes déclaratives sont exposées au rappel, à la non-réponse et aux règles de pondération. Les capteurs et données transactionnelles ont des limites de couverture et d’interprétation. Les données d’applications ou de téléphonie peuvent exclure une partie de la population ou dépendre d’algorithmes propriétaires.

**Pratique recommandée :** distinguer systématiquement les données observées, estimées et modélisées, et documenter la couverture connue.

### Ruptures de série

Une évolution apparente peut résulter d’un changement de questionnaire, de recrutement, de pondération, de géolocalisation, de zonage, de réseau, de tarification ou de fournisseur de données.

**Pratique recommandée :** traiter tout changement méthodologique comme une rupture potentielle jusqu’à preuve du contraire.

## Niveaux de comparabilité

| Niveau | Critère | Usage permis |
|---|---|---|
| Directe | Même univers, territoire, unité, période, saison et méthode, ou écarts négligeables | Comparaison quantitative et évolution |
| Ajustable | Écarts connus pouvant être harmonisés par une transformation explicite | Comparaison après documentation et test de sensibilité |
| Contextuelle | Sources utiles pour interpréter une tendance, mais univers ou unités différents | Mise en perspective qualitative; pas de ratio direct |
| Non comparable | Écarts majeurs ou documentation insuffisante | Ne pas agréger ni inférer une évolution commune |

## Protocole avant comparaison

1. Formuler la question et l’indicateur recherché avant de sélectionner les sources.
2. Remplir la grille de qualification minimale pour chaque source.
3. Vérifier l’alignement de l’univers, du territoire, de l’unité, des jours couverts et de la saison.
4. Repérer les changements de méthode, de périmètre ou de traitement.
5. Classer la comparaison selon les quatre niveaux ci-dessus.
6. Documenter les ajustements, hypothèses et incertitudes dans le livrable final.
7. Si les données ne sont que contextuellement comparables, éviter les calculs de variation, de part ou de causalité.

## Cas d’usage québécois

- **Enquêtes ARTM / origine-destination :** référence structurante pour les comportements des résidents, mais résultats associés à une période et à un jour moyen de semaine précis.
- **Achalandage STM, REM et autres opérateurs :** données opérationnelles utiles pour suivre le réseau, mais qui ne correspondent pas nécessairement à des personnes uniques ou à des chaînes de déplacement complètes.
- **BIXI, autopartage et VTC :** activité d’un service ou d’une flotte; utile pour analyser l’usage du service, sans extrapolation automatique à la part modale régionale.
- **Comptages vélo et piétons :** très informatifs localement, mais sensibles à l’emplacement, à la météo, aux horaires et aux dispositifs de comptage.
- **Enquêtes de Statistique Canada :** comparabilité dépendante du plan d’échantillonnage, de la population cible, de la période de référence et des définitions propres à chaque programme.

## Checklist de publication

Avant de publier un résultat comparatif, confirmer :

- [ ] Les populations et territoires couverts sont identifiés.
- [ ] Les unités et définitions sont compatibles.
- [ ] Les jours, périodes et saisons sont indiqués.
- [ ] La méthode, l’échantillonnage et la pondération sont connus.
- [ ] Les ruptures de série possibles ont été vérifiées.
- [ ] Les limites sont visibles près du résultat, et non seulement dans une annexe.
- [ ] Les liens vers la source primaire et sa documentation sont fournis.

## Références de départ

- [ARTM — Enquête métropolitaine Perspectives mobilité](https://www.artm.quebec/planification/enquete-metropolitaine-perspectives-mobilite/)
- [Transport Canada — Guide on Sustainable Transportation Surveying](https://publications.gc.ca/collections/collection_2012/tc/T22-209-2012-eng.pdf)
- [Eurostat — Passenger Mobility Guidelines](https://circabc.europa.eu/sd/a/dbaad8ad-7573-4092-bd2e-996ee64d6f05/Passenger%20Mobility%20Guidelines%20July%202016(0).pdf)

## À améliorer

- Ajouter des exemples vérifiés de ruptures de séries au Québec.
- Proposer un schéma de métadonnées réutilisable dans `catalogue.csv`.
- Ajouter des méthodes d’harmonisation documentées, avec leurs limites.
- Recenser les licences et restrictions d’accès des principales bases québécoises.
- Faire relire cette page par des spécialistes des enquêtes, de la statistique, du transport et des données ouvertes.

*Dernière mise à jour : 13 août 2026.*
