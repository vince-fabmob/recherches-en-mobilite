# Québec — Débits de circulation du MTMD

> **Document de travail — à réviser.** Cette fiche décrit une ressource publique du ministère des Transports et de la Mobilité durable (MTMD). Vérifier le dictionnaire de données, la date de mise à jour, les méthodes et les conditions de réutilisation avant toute analyse ou publication.

## Référence

- **Organisme :** Ministère des Transports et de la Mobilité durable (MTMD), Gouvernement du Québec.
- **Jeu de données :** *Débit de circulation*.
- **Accès :** [Portail ouvert du Canada — fiche du jeu](https://ouvert.canada.ca/data/fr/dataset/c77c495a-2a4c-447e-9184-25722289007f).
- **Licence indiquée :** Licence Creative Commons Attribution 4.0 — Québec (CC-BY).
- **Formats indiqués :** CSV, GeoJSON, GeoPackage, SHP, WFS, WMS, carte interactive et dictionnaire de données.

## Description

Le jeu représente, sous forme de réseau linéaire, les débits de circulation estimés pour les routes et autoroutes gérées par le MTMD. Les valeurs sont estimées à partir de données provenant de plus de **4 500 sites de collecte** répartis sur les principales routes du Québec.

Les indicateurs comprennent notamment :

| Indicateur | Définition |
|---|---|
| DJMA | Débit journalier moyen annuel |
| DJME | Débit journalier moyen estival, couvrant juin à septembre |
| DJMH | Débit journalier moyen hivernal, couvrant décembre à mars |

Les valeurs publiées sont calculées pour le **total des directions de circulation**.

## Ressources associées

La carte interactive associée donne notamment accès, selon les sections de trafic, à :

- des données agrégées historiques;
- des rapports annuels pour les sites permanents, en PDF et Excel;
- des données horaires, soit une moyenne horaire par jour de semaine et par mois, en Excel.

## Usages possibles

- Cartographie des débits routiers sur le réseau sous gestion provinciale.
- Mise en contexte des flux routiers dans les analyses de sécurité, d’entretien, d’émissions ou de transport de marchandises.
- Comparaison saisonnière entre DJME et DJMH pour une même section, avec prudence méthodologique.
- Sélection de corridors ou de sections à approfondir au moyen des rapports de sites permanents.
- Croisement géographique avec les réseaux de transport collectif, les infrastructures de recharge ou les données de comptage locales.

## Limites et précautions

- Le jeu décrit les routes et autoroutes **gérées par le MTMD**; il ne couvre donc pas automatiquement toutes les rues municipales, ni l’ensemble du réseau routier montréalais.
- Les débits sont des **estimations statistiques** issues de sites de collecte; ils ne sont pas des comptages observés en continu sur chaque segment publié.
- Les valeurs représentent le total des deux directions : elles ne permettent pas, sans ressource complémentaire, d’analyser la direction dominante, les mouvements aux intersections ou l’heure de pointe.
- DJMA, DJME et DJMH répondent à des périodes de référence distinctes. Ils ne doivent pas être comparés ou agrégés comme s’ils représentaient la même saison ou la même période.
- Le débit de véhicules ne mesure ni les personnes transportées, ni les véhicules-kilomètres d’un corridor complet, ni les déplacements des résidents; il n’est donc pas directement comparable à une enquête OD, à l’achalandage TC ou à des passages cyclistes.
- Les changements de géométrie, de sectionnement, de réseau, de méthodologie ou de couverture des sites peuvent produire des ruptures de série.
- Le dictionnaire de données et les rapports associés sont nécessaires pour interpréter correctement les champs et la période de chaque observation.

## Métadonnées de comparabilité

| Dimension | Description |
|---|---|
| Univers | Véhicules circulant sur les routes et autoroutes gérées par le MTMD |
| Géographie | Sections du réseau routier sous gestion provinciale au Québec |
| Unité | Débit journalier moyen de véhicules, total des directions |
| Temporalité | DJMA annuel; DJME de juin à septembre; DJMH de décembre à mars; ressources horaires pour certains sites |
| Saisonnalité | Explicitement représentée par les indicateurs estival et hivernal |
| Méthode | Estimation statistique à partir de plus de 4 500 sites de collecte |
| Niveau de comparabilité | Ajustable entre sections ou années seulement après vérification des définitions, périodes et ruptures; contextuelle avec les données de personnes ou de déplacements |

## Mots-clés

`Québec` · `MTMD` · `débit routier` · `DJMA` · `DJME` · `DJMH` · `trafic` · `réseau routier` · `données géospatiales`

*Dernière vérification : 13 août 2026.*
