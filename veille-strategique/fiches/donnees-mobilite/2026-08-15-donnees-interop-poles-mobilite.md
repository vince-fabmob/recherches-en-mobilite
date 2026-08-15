---
id: SIG-DAT-2026-0003
titre: Données interopérables pour évaluer les pôles de mobilité
date: 2026-08-15
theme: donnees-mobilite
statut: proposition
tags:
  - GTFS
  - GTFS-RT
  - interopérabilité
  - pôles-de-mobilité
  - accessibilité
  - gouvernance-des-données
  - SEAM
territoire: Montréal / Québec
---

# Données interopérables pour évaluer les pôles de mobilité

## Signal
Les pôles de mobilité assemblent plusieurs services — marche, vélo, transport collectif, autopartage, micromobilité, recharge et logistique légère. Sans données interopérables, il est difficile de mesurer la qualité réelle des correspondances, l’accessibilité, la disponibilité des services et les effets énergétiques. Le signal stratégique est le passage d’une logique de comptage par mode à une évaluation porte-à-porte et orientée usager.

## Enjeu
Les systèmes de mobilité produisent de nombreuses données, mais elles sont souvent fragmentées entre opérateurs, formats et finalités. Une intégration insuffisante empêche de détecter les ruptures de chaîne de déplacement : une correspondance ratée, un véhicule partagé indisponible, une borne occupée, un itinéraire inaccessible ou un détour de livraison. À l’inverse, une centralisation mal gouvernée peut accroître les risques pour la vie privée, l’équité et l’autonomie des opérateurs.

## Objectif
Définir un noyau minimal de données et d’indicateurs permettant d’évaluer un pôle de mobilité selon l’accessibilité, la qualité de service, l’énergie, l’utilisation des actifs, l’équité et la résilience, tout en limitant la collecte de données personnelles.

## Noyau de données interopérables
| Domaine | Données minimales | Usages |
|---|---|---|
| Transport collectif | Horaires planifiés, positions et perturbations en temps réel, accessibilité des stations | Planification des correspondances et mesure de fiabilité |
| Marche et vélo | Réseau, continuité, pentes, entraves, stationnement, déneigement lorsque disponible | Évaluer le premier et le dernier kilomètre |
| Services partagés | Disponibilité, localisation agrégée, type de véhicule, zones de service, tarifs | Vérifier les alternatives et l’accès aux véhicules |
| Recharge | Statut des bornes, connecteurs, puissance, occupation, prix, disponibilité | Planifier la recharge et suivre la pression sur le réseau |
| Logistique légère | Fenêtres de livraison, emplacements, occupation et tournées agrégées | Réduire les conflits d’usage et les kilomètres inutiles |
| Accessibilité universelle | Ascenseurs, pentes, obstacles, quais, cheminements, information adaptée | Garantir une chaîne de déplacement utilisable par tous |
| Énergie et environnement | Puissance, énergie, heure de recharge, intensité carbone, état agrégé des flottes | Mesurer les effets énergétiques et climatiques |

## Standards et principes d’intégration
- Utiliser GTFS pour l’offre planifiée et GTFS-RT pour les mises à jour opérationnelles du transport collectif.
- Documenter les jeux de données, leur fréquence de mise à jour, leurs limites, leur propriétaire et leurs règles de réutilisation.
- Privilégier les interfaces standardisées et des identifiants stables pour les lieux, services, équipements et événements.
- Séparer les données ouvertes agrégées, les données opérationnelles partagées sous entente et les données personnelles strictement nécessaires.
- Concevoir l’interopérabilité comme une capacité de service, non comme une obligation de centraliser toutes les bases de données.

## Indicateurs de suivi
| Indicateur | Définition | Finalité |
|---|---|---|
| Temps porte-à-porte médian | Durée totale incluant accès, attente, trajet et correspondances | Mesurer l’expérience réelle des usagers |
| Fiabilité des correspondances | Part des correspondances réussies dans un seuil défini | Identifier les ruptures de chaîne |
| Disponibilité des services partagés | Part du temps avec un véhicule ou un vélo disponible dans la zone | Mesurer la capacité de substitution à l’auto privée |
| Accessibilité des parcours | Part des itinéraires accessibles sans obstacle critique | Suivre l’équité d’accès |
| Taux d’occupation des véhicules | Passagers ou chargement par véhicule-kilomètre | Mesurer l’efficacité d’usage des actifs |
| Kilomètres à vide | Distance parcourue sans passager ni charge utile | Détecter les inefficacités et le rebond |
| Puissance appelée et énergie consommée | kW et kWh par période | Suivre les effets sur le réseau électrique |
| Usage de l’espace | Occupation des quais, bornes, stationnements et aires de livraison | Arbitrer l’allocation de l’espace public |
| Émissions associées | Émissions directes ou facteurs documentés selon le mode et l’énergie | Évaluer l’effet climatique |

## Gouvernance et équité
- Définir une finalité précise pour chaque donnée collectée et limiter les données personnelles au strict nécessaire.
- Publier un dictionnaire de données et un registre des responsables, des droits d’accès et des durées de conservation.
- Mesurer les performances par territoire, horaire et groupe d’usage afin de détecter les inégalités de service.
- Prévoir des mécanismes de recours humain lorsque les décisions de service ou de tarification reposent sur des systèmes automatisés.
- Évaluer les risques de réidentification avant toute diffusion de données de déplacements, même agrégées.

## Proposition de pilote
Déployer pendant 12 mois un socle de données sur un ou deux pôles de mobilité. Produire :
- un tableau de bord public avec données agrégées sur la qualité de service, l’accessibilité et l’énergie;
- un espace sécurisé de données opérationnelles pour les partenaires autorisés;
- un bilan trimestriel des correspondances, de la disponibilité, de l’accessibilité et des effets de recharge;
- une évaluation indépendante de la qualité des données, de l’équité et de la protection des renseignements personnels.

## Risques et limites
- Couverture inégale ou données de mauvaise qualité entre opérateurs.
- Délais de mise à jour incompatibles avec l’information voyageur en temps réel.
- Dépendance à des plateformes propriétaires ou à des conditions de réutilisation restrictives.
- Biais dans les indicateurs si les usagers non connectés ou les déplacements informels sont sous-observés.
- Coûts de normalisation, de cybersécurité et de gouvernance souvent sous-estimés.

## Liens internes
- `Reference_Espace_Mobilite_Durable` : cadre SEAM, pôles de mobilité, recharge intelligente et V2G.
- Référentiel général — Mobilité, énergie et SEAM : domaines `DAT`, `MOB`, `INF`, `ENE` et `GOV`.
- À articuler avec la fiche `SIG-MOB-2026-0002` sur la recharge bidirectionnelle et la flexibilité énergétique des pôles.

## Niveau de maturité
**À instruire.** Les standards de données de transport collectif sont établis, mais l’intégration opérationnelle de la mobilité partagée, de la recharge, de la logistique légère et de l’accessibilité requiert une gouvernance locale, des accords de partage et des critères d’équité explicites.
