# Montréal — Comptages de véhicules, cyclistes et piétons aux intersections

> **Document de travail — à réviser.** Cette fiche décrit un jeu de données public de la Ville de Montréal. Vérifier les ressources, le dictionnaire de données, la licence et les dates de mise à jour sur la page source avant toute utilisation.

## Référence

- **Organisme :** Ville de Montréal.
- **Jeu de données :** *Comptages des véhicules, cyclistes et piétons aux intersections munies de feux de circulation*.
- **Accès :** [Données ouvertes de la Ville de Montréal](https://donnees.montreal.ca/dataset/comptage-vehicules-pietons).
- **Formats indiqués :** CSV, GeoJSON et ZIP; les ressources sont organisées par périodes pluriannuelles.
- **Territoire :** intersections des 19 arrondissements, principalement munies de feux de circulation; certaines intersections où l’installation de feux était à l’étude sont aussi incluses.

## Description

Le jeu regroupe des comptages de véhicules, piétons et cyclistes effectués à des intersections. Les relevés ont été réalisés dans le cadre de la mise aux normes des feux de circulation par les services centraux de la Ville. Les comptages produits par les arrondissements ne sont pas inclus.

Les données détaillent le nombre, la provenance et la direction des véhicules, piétons et cyclistes pour les mouvements possibles à une intersection. Les relevés incluent le passage des cyclistes depuis 2009.

## Méthode indiquée

- Observations sur le terrain à l’aide d’un appareil de comptage électronique.
- Relevés réalisés à des intervalles de 15 minutes.
- Périodes généralement couvertes : pointes du matin et du soir, ainsi que période du midi.
- Durée d’observation quotidienne variable selon l’intersection : de 3 à 8 heures.
- Variables publiées comprenant notamment l’identifiant du comptage, l’intersection, la date, la période, l’heure, les catégories d’usagers et les mouvements ou approches.

## Usages possibles

- Analyse locale des volumes et des mouvements à une intersection.
- Étude de l’exposition relative des véhicules, piétons et cyclistes durant les périodes observées.
- Appui à la planification des feux, des traverses et des aménagements d’intersection.
- Cartographie des sites et comparaison descriptive des comptages disponibles.

## Limites et précautions

- Ce jeu ne constitue pas un échantillon aléatoire de toutes les intersections ni de tous les déplacements à Montréal : la sélection est liée aux besoins de mise aux normes des feux et à certains projets d’installation de feux.
- Les observations couvrent seulement certaines plages horaires, principalement des périodes de pointe et du midi. Elles ne mesurent donc pas une journée complète, une semaine complète, les fins de semaine ou une moyenne annuelle.
- La durée d’observation varie de 3 à 8 heures selon l’intersection; les totaux bruts ne sont pas directement comparables sans vérifier l’horaire précis et la durée de chaque relevé.
- Les comptages peuvent ne pas inclure certains types d’usagers ou de véhicules, par exemple piétons, cyclistes ou camions, selon le site et le relevé.
- La date, la météo, la saison, les travaux, les événements, le réseau cyclable et la configuration des lieux peuvent influencer les résultats.
- Il faut distinguer ces comptages ponctuels aux intersections des données de compteurs cyclistes permanents, qui sont collectées automatiquement et publiées à d’autres granularités temporelles.

## Métadonnées de comparabilité

| Dimension | Description |
|---|---|
| Univers | Usagers et véhicules observés aux intersections comptées; non représentatif automatiquement de tous les Montréalais ou déplacements |
| Géographie | Intersections sélectionnées dans les 19 arrondissements |
| Unité | Passages et mouvements observés par type d’usager durant une période de comptage |
| Temporalité | Intervalles de 15 minutes; périodes de pointe et midi en général; 3 à 8 heures par jour de comptage |
| Saisonnalité | Variable selon la date inscrite dans le relevé; à contrôler dans toute comparaison |
| Méthode | Observation terrain avec appareil de comptage électronique |
| Niveau de comparabilité | Contextuelle à ajustable entre sites ou années; exige l’alignement des mouvements, périodes, durées, saisons et configurations d’intersection |

## Ressources associées

- [Compteurs cyclistes permanents — Ville de Montréal](https://donnees.montreal.ca/fr/dataset/cyclistes) : données issues de détecteurs permanents, avec agrégations aux pas de 15 minutes, horaire, quotidien, mensuel et annuel.
- [Fréquentation des voies actives sécuritaires (VAS)](https://www.donneesquebec.ca/recherche/dataset/vmtl-frequentation-voies-actives-securitaires) : comptages automatisés sur des sites liés aux VAS en 2020, avec limites spécifiques de capteurs, d’entraves et de déplacements d’équipement.

## Mots-clés

`Montréal` · `comptage` · `intersection` · `véhicules` · `piétons` · `cyclistes` · `feux de circulation` · `données ouvertes` · `mobilité active`

*Dernière vérification : 13 août 2026.*
