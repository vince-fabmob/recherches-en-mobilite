# Contribuer à la veille stratégique

## Ajouter une fiche

1. Copier `templates/fiche-signal-prospectif.md` dans le dossier thématique approprié sous `fiches/`.
2. Attribuer un identifiant unique de forme `SIG-DOMAINE-AAAA-NNNN`.
3. Remplir toutes les métadonnées YAML et conserver les valeurs prévues dans `taxonomie.yml`.
4. Distinguer explicitement le fait observé, l’annonce du promoteur, l’hypothèse prospective et la condition de bascule.
5. Ajouter au moins une URL de source dans la section « Sources ».
6. Ajouter une ligne correspondante dans `catalogue_signaux.csv`.
7. Lancer localement :

```bash
pip install -r requirements-dev.txt
python scripts/validate_veille.py
```

## Règles de rédaction

- Écrire les mécanismes prospectifs au conditionnel.
- Ne pas déduire la viabilité commerciale d’une démonstration.
- Distinguer une mesure observée d’une cible ou d’une projection.
- Justifier les scores d’impact, de force du signal et d’incertitude dans le corps de la fiche.
- Éviter la reproduction de données ou contenus de tiers; privilégier les liens, métadonnées et extraits strictement nécessaires.

## Contrôles automatisés

Le workflow GitHub Actions vérifie le front matter YAML, les catégories de la taxonomie, les sections requises, l’unicité des identifiants et la cohérence avec `catalogue_signaux.csv`.
