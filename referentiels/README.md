# Référentiels transversaux

Ces catalogues fournissent des identifiants stables pour relier les fiches de veille stratégique aux données, opérateurs et solutions déjà documentés dans le dépôt. Ils ne redistribuent pas les données de tiers : ils conservent des métadonnées, des liens et des chemins vers les fiches sources du dépôt.

## Structure

- `donnees/` : jeux de données, producteurs et infrastructures informationnelles.
- `operateurs/` : organisations qui exploitent ou administrent des services et infrastructures de mobilité.
- `solutions/` : solutions techniques, numériques ou de mobilité utiles dans une chaîne de déplacement.

## Règle de liaison

Dans une fiche de veille, utiliser les identifiants `DATA-*`, `OP-*` et `SOL-*` dans le bloc YAML `relations`. Le validateur vérifie que chaque identifiant cité existe dans le catalogue correspondant.
