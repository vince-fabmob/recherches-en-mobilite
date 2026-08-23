# Contribuer

Merci de contribuer à ce répertoire.

## Règles de contribution

Toute fiche doit inclure :

1. Un lien officiel vers la source primaire
2. Le producteur et le territoire couvert
3. La date de consultation
4. Les conditions d’utilisation, ou un lien vers celles-ci
5. Une description strictement factuelle

## Ne pas ajouter

- De copie de données de tiers
- De données personnelles ou sensibles
- De contenu protégé reproduit sans autorisation
- D’opinions, recommandations, hypothèses ou évaluations non attribuées

## Processus

1. Utiliser le modèle `templates/fiche-source.md`
2. Classer la fiche dans une section thématique et, si utile, territoriale
3. Vérifier les liens et l’attribution
4. Soumettre une issue ou une pull request expliquant brièvement l’ajout

Les liens peuvent changer. Une source est décrite telle qu’elle est accessible à la date de consultation.

## Règles pour les analyses (`analyses/`)

Contrairement aux fiches de `sources/`, un document d’analyse peut présenter des valeurs numériques calculées à partir de sources externes, à condition de respecter ce qui suit :

1. Chaque valeur doit remonter à une source primaire identifiée précisément (nom du tableau ou du jeu de données, identifiant, URL complète, date de consultation)
2. La méthode de calcul (sommes, conversions d’unités, agrégations, variations) doit être explicitée, pas seulement le résultat
3. Ne pas reproduire l’intégralité d’un fichier ou d’un tableau source ; ne retenir que les valeurs nécessaires à l’analyse
4. Signaler les limites, ruptures de série ou données manquantes plutôt que de les combler par estimation silencieuse
5. Conserver le principe de neutralité : décrire des tendances factuelles, pas des positions sur des politiques publiques
6. Suivre la structure du modèle `templates/fiche-analyse.md`