---
id: SIG-MOB-2026-0002
titre: Recharge bidirectionnelle et flexibilité énergétique des pôles de mobilité
date: 2026-08-15
theme: flexibilite-energetique
statut: proposition
tags:
  - V2G
  - recharge-intelligente
  - vehicules-electriques
  - mobilite-partagee
  - SEAM
territoire: Montréal / Québec
---

# Recharge bidirectionnelle et flexibilité énergétique des pôles de mobilité

## Signal
Les pôles de mobilité concentrent des flottes électrifiées, des usages multimodaux et des équipements de recharge. Lorsqu’ils intègrent une recharge intelligente et, lorsque les conditions techniques et réglementaires le permettent, une recharge bidirectionnelle (*vehicle-to-grid*, V2G), ils peuvent contribuer à déplacer la demande électrique hors des périodes de pointe et à fournir une flexibilité locale au réseau.

## Enjeu
L’électrification de la mobilité réduit les émissions à l’usage au Québec, où l’électricité est largement décarbonée, mais la recharge non pilotée peut accroître les appels de puissance lors des pointes hivernales. Le défi opérationnel consiste à mobiliser la flexibilité des batteries sans compromettre la disponibilité des véhicules pour les déplacements essentiels, l’accessibilité ou les services de logistique légère.

## Hypothèse SEAM
Une flotte partagée, électrifiée, automatisable et intégrée à un pôle multimodal est plus pilotable qu’un parc individuel dispersé. La mutualisation donne à l’opérateur une visibilité sur les horaires, l’état de charge, les réservations et les priorités de service. Cette capacité d’orchestration permet de planifier la recharge, d’effacer temporairement une charge ou de restituer une énergie limitée, sous réserve de garde-fous explicites.

## Cas d’usage
- Autopartage électrique : recharge différée en dehors des pointes, avec un seuil minimal d’état de charge avant chaque réservation.
- Minibus et navettes : recharge en dépôt durant les fenêtres hors service et participation limitée à des programmes de flexibilité.
- Logistique urbaine légère : vélos-cargos, fourgonnettes et micromobilité électrique rechargés en fonction des tournées et de la puissance disponible.
- Pôle multimodal : pilotage coordonné entre bornes publiques, flottes partagées, stockage stationnaire et production locale éventuelle.

## Indicateurs de suivi
| Indicateur | Unité | Finalité |
|---|---:|---|
| Puissance appelée en période de pointe | kW | Mesurer la pression exercée sur le réseau |
| Puissance effacée ou modulée | kW | Quantifier la flexibilité activable |
| Énergie déplacée hors pointe | kWh | Suivre le décalage de recharge |
| Énergie restituée au réseau | kWh | Mesurer la contribution V2G, le cas échéant |
| Disponibilité des véhicules | % | Vérifier que le service de mobilité demeure prioritaire |
| Réservations non satisfaites | nombre / % | Détecter un effet négatif sur les usagers |
| Coût énergétique évité | $ | Évaluer l’intérêt économique |
| Émissions évitées ou déplacées | kg CO₂e | Documenter l’effet climatique selon l’heure de recharge |

## Conditions de réussite
- Interopérabilité des véhicules, bornes, systèmes de gestion de recharge et plateformes de réservation.
- Règles de priorité explicites pour les déplacements essentiels, l’accessibilité universelle et les services critiques.
- Tarification et signaux de flexibilité suffisamment lisibles pour les opérateurs.
- Ententes avec le distributeur et cadre réglementaire compatible avec la recharge bidirectionnelle.
- Mesure transparente de l’état de charge, de l’usage des batteries et de la qualité de service.
- Cybersécurité, protection des données et procédures de reprise manuelle.

## Risques et limites
- Dégradation accélérée des batteries si les cycles V2G sont mal calibrés.
- Indisponibilité de véhicules lors d’une réservation ou d’une urgence si les seuils de charge sont insuffisants.
- Bénéfices réseau dépendants du lieu, de l’heure et de la structure tarifaire.
- Risque d’exclure les usagers sans accès aux outils numériques ou de transférer le coût du pilotage vers certains groupes.
- Les résultats d’un pilote ne sont pas automatiquement généralisables à l’échelle d’un réseau métropolitain.

## Proposition de pilote
Mettre en place un pilote de 12 mois dans un pôle de mobilité combinant autopartage électrique, bornes publiques et un service de logistique légère. Définir un niveau de service minimal avant toute activation de flexibilité, comparer une période de recharge non pilotée à une période de recharge intelligente, puis tester le V2G sur un sous-ensemble de véhicules compatibles.

Les livrables attendus sont un bilan de puissance et d’énergie, une analyse de disponibilité des véhicules, une estimation des coûts et bénéfices, ainsi qu’un protocole de gouvernance transférable à d’autres pôles.

## Sources et liens internes
- `Reference_Espace_Mobilite_Durable` : sections « Électrification du parc & infrastructures de recharge » et « Cadre SEAM ».
- Référence interne à approfondir : données de pointe, programmes de flexibilité et exigences techniques applicables aux projets pilotes au Québec.

## Niveau de maturité
**À instruire.** La recharge intelligente est une pratique déployable; l’application V2G à des pôles de mobilité demande une validation technique, tarifaire, réglementaire et opérationnelle locale avant généralisation.
