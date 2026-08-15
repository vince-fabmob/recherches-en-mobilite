# Veille stratégique — mobilité et énergie

Ce répertoire documente des signaux factuels pouvant modifier les trajectoires de mobilité, d’énergie et d’aménagement. Il distingue explicitement les faits observés, les annonces, les hypothèses prospectives et les conditions de bascule.

## Objectifs

- Conserver des sources externes traçables, sans redistribuer leurs données ou contenus protégés.
- Relier les signaux à des scénarios, indicateurs, points de bascule et trajectoires dynamiques.
- Rendre les métadonnées exploitables par CSV, YAML, Python, SQL ou un tableau de bord.
- Préserver des options réelles et éviter les verrouillages technologiques dans l’analyse des infrastructures.

## Statuts épistémiques

| Statut | Définition |
|---|---|
| `fait_observe` | Événement, mesure ou résultat directement documenté. |
| `annonce_promoteur` | Cible, calendrier, coût ou performance déclaré par une organisation. |
| `hypothese_prospective` | Mécanisme plausible mais non confirmé. |
| `condition_de_bascule` | Seuil observable susceptible de modifier une trajectoire. |

## Arborescence

- `fiches/` : une fiche Markdown par signal.
- `catalogue_signaux.csv` : index plat des signaux pour analyse.
- `taxonomie.yml` : vocabulaires contrôlés et échelles.
- `scenarios/` : scénarios-cadres réutilisables.
- `dynamic-pathways/` : trajectoires séquencées, conditions de passage et options réelles.
- `indicateurs/` : dictionnaire et seuils de suivi.
- `templates/` : gabarits de création.

## Méthode

Une fiche ne conclut pas à elle seule qu’une technologie est viable ou souhaitable. Toute fiche doit préciser :

1. le fait et sa source;
2. le niveau de preuve et ses limites;
3. les mécanismes possibles;
4. les scénarios touchés;
5. les points de bascule et indicateurs à suivre;
6. les risques de verrouillage, d’effet rebond et d’inéquité, lorsque pertinents.

Voir le [gabarit de fiche](templates/fiche-signal-prospectif.md) et la [taxonomie](taxonomie.yml).
