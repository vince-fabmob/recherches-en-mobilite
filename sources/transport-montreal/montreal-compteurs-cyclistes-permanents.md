# Montréal — Compteurs cyclistes permanents

> **Document de travail — à réviser.** Cette fiche décrit un jeu de données public de la Ville de Montréal. Les sites, ressources, méthodes, données manquantes et conditions de réutilisation doivent être vérifiés sur la page source avant toute analyse.

## Référence

- **Organisme :** Ville de Montréal — Service de l’urbanisme et de la mobilité, Direction de l’urbanisme.
- **Jeu de données :** *Compteurs cyclistes permanents*.
- **Accès :** [Données ouvertes de la Ville de Montréal](https://donnees.montreal.ca/fr/dataset/cyclistes).
- **Mise à jour indiquée :** quotidienne.
- **Territoire :** sites de détection vélo installés à différents emplacements à Montréal.

## Description

Le jeu provient de détecteurs de comptage vélo installés sur différents sites par le Service de l’urbanisme et de la mobilité (SUM-DIGD). Les capteurs enregistrent le nombre de passages de cyclistes à chaque minute. Certains emplacements fournissent également des données de vitesse moyenne.

Les données brutes sont publiées sous plusieurs agrégations :

- 15 minutes;
- horaire;
- quotidienne;
- mensuelle;
- annuelle.

## Variables documentées

| Variable | Description publiée |
|---|---|
| `_id` | Identifiant unique de chaque comptage |
| `agg_code` | Niveau d’agrégation : 15 minutes, heure, jour, mois ou année |
| `instance` | Identifiant unique du site de comptage |
| `longitude`, `latitude` | Position du site en WGS 84 |
| `arrondissement` | Arrondissement |
| `numeroVoie` | Numéro de la voie de comptage |
| `direction` | Direction des vélos |
| `periode` | Période de comptage |
| `volume` | Nombre de passages durant la période |
| `vitesse` | Vitesse moyenne durant la période, lorsque disponible |

## Usages possibles

- Suivi de séries temporelles de passages cyclistes à des sites instrumentés.
- Analyse des variations horaires, quotidiennes, mensuelles et saisonnières.
- Comparaison avant-après d’un aménagement ou d’un événement à proximité d’un site, avec protocole explicite.
- Cartographie des volumes et des directions aux sites couverts.
- Appui aux analyses de fréquentation d’un corridor ou d’une infrastructure cyclable.

## Limites et précautions

- Les données représentent des **passages à des sites instrumentés**, et non le nombre de personnes cyclistes uniques, les déplacements complets ou l’ensemble de la pratique cycliste montréalaise.
- Les sites ne constituent pas nécessairement un échantillon représentatif du réseau ou de la population cycliste; l’emplacement et la configuration du compteur structurent fortement les résultats.
- Les variations observées reflètent aussi la météo, la saison, les vacances, les travaux, les changements de réseau et les événements locaux.
- La Ville indique comme limites possibles l’**occlusion** et la **perte de communication réseau**. Il faut vérifier les périodes de données manquantes ou anormales avant de calculer des totaux ou des taux de croissance.
- Les agrégations ne doivent pas être additionnées entre elles : il faut choisir un seul niveau temporel pour une analyse donnée.
- Les comparaisons entre sites exigent la vérification de la période de fonctionnement, du nombre de voies, de la direction mesurée et de l’exposition à l’infrastructure cyclable.
- Cette ressource est distincte des comptages manuels ponctuels aux intersections; les univers, temporalités et méthodes de mesure ne sont pas directement interchangeables.

## Métadonnées de comparabilité

| Dimension | Description |
|---|---|
| Univers | Passages de cyclistes détectés aux sites équipés de compteurs permanents |
| Géographie | Emplacements instrumentés sur le territoire de Montréal |
| Unité | Passage cycliste durant une période d’agrégation; vitesse moyenne sur certains sites |
| Temporalité | Mesure à la minute, puis agrégations de 15 minutes, horaire, quotidienne, mensuelle et annuelle |
| Saisonnalité | Observable dans les séries, mais à contrôler explicitement lors de comparaisons entre périodes |
| Méthode | Détecteurs installés sur fût; traitements automatisés d’agrégation |
| Niveau de comparabilité | Ajustable entre périodes pour un même site après contrôle de la complétude; contextuelle entre sites aux configurations différentes |

## Lien avec d’autres sources

- [Comptages de véhicules, cyclistes et piétons aux intersections](montreal-comptages-vehicules-cyclistes-pietons.md) : relevés ponctuels par mouvement et période, distincts des séries continues des compteurs permanents.
- [Enquête métropolitaine 2023 de l’ARTM](artm-enquete-metropolitaine-2023.md) : enquête ménage régionale sur les déplacements, non comparable directement avec des passages locaux de vélos.

## Mots-clés

`Montréal` · `vélo` · `compteur permanent` · `mobilité active` · `passages cyclistes` · `saisonnalité` · `données ouvertes` · `série temporelle`

*Dernière vérification : 13 août 2026.*
