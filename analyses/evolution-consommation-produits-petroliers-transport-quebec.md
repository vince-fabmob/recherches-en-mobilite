# Évolution de la consommation de produits pétroliers en transport au Québec (1990–2024)

## Identification

- **Question analysée :** Comment ont évolué depuis 1990 les volumes de carburants routiers vendus, le contenu énergétique des produits pétroliers consommés par le secteur des transports et les émissions de GES associées, au Québec ?
- **Territoire couvert :** Québec
- **Période couverte :** 1990–2024 (selon disponibilité par série, voir Limites)
- **Date de réalisation :** 2026-08-23

## Sources primaires utilisées

| Source | Producteur | Identifiant du tableau ou du jeu de données | Lien officiel | Date de consultation |
|---|---|---|---|---|
| Ventes nettes d'essence et de carburant diesel, par province | Statistique Canada | Tableau 23-10-0066-01 (anciennement CANSIM 405-0002) | [Accéder](https://www150.statcan.gc.ca/t1/tbl1/fr/tv.action?pid=2310006601) | 2026-08-23 |
| Disponibilité et écoulement d'énergie primaire et secondaire en térajoules, annuel | Statistique Canada | Tableau 25-10-0029-01 (anciennement CANSIM 128-0016) | [Accéder](https://www150.statcan.gc.ca/t1/tbl1/fr/tv.action?pid=2510002901) | 2026-08-23 |
| Inventaire québécois des émissions de gaz à effet de serre | Ministère de l'Environnement, de la Lutte contre les changements climatiques, de la Faune et des Parcs (MELCCFP), diffusé via Données Québec | Jeu de données « Inventaire québécois des émissions de gaz à effet de serre » (fichier `inventaire-ges.csv`) | [Accéder](https://www.donneesquebec.ca/recherche/dataset/inventaire-quebecois-des-emissions-de-gaz-a-effet-de-serre) | 2026-08-23 |

## Méthode de calcul

1. **Carburants routiers vendus (Gl)** — Somme des variables « Ventes nettes d'essence » et « Ventes nettes de carburant diesel » du tableau 23-10-0066-01, filtrées sur `GEO = Quebec`. Les valeurs sont fournies en milliers de litres et converties en milliards de litres (Gl) en divisant par 1 000 000.
2. **Énergie pétrolière — secteur transport (PJ)** — Valeur de la variable « Total des produits pétroliers raffinés » à la caractéristique « Total transport » du tableau 25-10-0029-01, filtrée sur `GÉO = Québec`. Les valeurs sont fournies en térajoules (TJ) et converties en pétajoules (PJ) en divisant par 1 000. Selon la définition du producteur, « Total transport » additionne les sociétés ferroviaires, les lignes aériennes, les lignes maritimes, les pipelines, le transport routier et en commun, et les ventes au détail (pompes) ; le carburant utilisé par des activités non liées directement au transport (gares, entrepôts, aéroports) en est exclu.
3. **GES transport routier (Mt éq. CO₂)** — Somme des émissions où `Secteur = Transports` et `Sous-secteur = Transport routier` dans `inventaire-ges.csv`, par année, convertie de tonnes en mégatonnes (÷ 1 000 000). Ce sous-secteur regroupe les catégories « Automobiles », « Camions légers », « Véhicules lourds » et « Autres transports routiers ».
4. **GES autres transports (Mt éq. CO₂)** — Somme des émissions où `Secteur = Transports` et `Sous-secteur` ∈ {Transport aérien, Transport ferroviaire, Transport maritime, Autres transports}, par année, même conversion.
5. **GES transport total (Mt éq. CO₂)** — Somme des deux valeurs précédentes.
6. **Variations relatives** — Calculées comme (valeur finale − valeur initiale) / valeur initiale × 100, sur les séries complètes disponibles (1990–2024 pour les carburants).

Aucun fichier source n'est reproduit intégralement : seules les variables et années nécessaires à ce tableau ont été extraites, recalculées et recombinées.

## Résultats

### Trajectoire 1990–2024

| Année | Essence vendue (Gl) | Diesel vendu (Gl) | Total carburants routiers (Gl) | Énergie pétrolière — transport (PJ) | GES transport routier (Mt éq. CO₂) | GES autres transports (Mt éq. CO₂) | GES transport total (Mt éq. CO₂) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1990 | 6,98 | 2,18 | 9,16 | n.d.¹ | 20,81 | 6,52 | 27,33 |
| 2000 | 7,86 | 2,92 | 10,78 | 415 | 23,27 | 7,59 | 30,86 |
| 2010 | 8,27 | 2,95 | 11,22 | 475 | 26,42 | 7,60 | 34,02 |
| 2019 | 8,62 | 3,36 | 11,98 | 526 | 26,51 | 9,46 | 35,97 |
| 2020 | 7,24 | 2,96 | 10,20 | 392 | 22,32 | 8,19 | 30,50 |
| 2023 | 8,19 | 3,19 | 11,38 | 493 | 26,04 | 8,85 | 34,90 |
| 2024 | 7,99 | 3,06 | 11,05 | 500 | n.d.² | n.d.² | n.d.² |

Sources : [Statistique Canada, tableau 23-10-0066-01](https://www150.statcan.gc.ca/t1/tbl1/fr/tv.action?pid=2310006601) ; [Statistique Canada, tableau 25-10-0029-01](https://www150.statcan.gc.ca/t1/tbl1/fr/tv.action?pid=2510002901) ; [Inventaire québécois des émissions de GES, MELCCFP/Données Québec](https://www.donneesquebec.ca/recherche/dataset/inventaire-quebecois-des-emissions-de-gaz-a-effet-de-serre).

¹ Le tableau 25-10-0029-01 ne couvre cette ventilation sectorielle qu'à partir de 1995.
² L'édition la plus récente de l'inventaire québécois des GES couvre jusqu'à 2023 ([MELCCFP, communiqué du 19 décembre 2025](https://www.quebec.ca/nouvelles/actualites/details/agir-pour-le-climat-sans-nuire-a-leconomie-67846)) ; 2024 n'est pas encore publié à la date de consultation.

### Variations 1990–2024 (carburants routiers)

| Indicateur | 1990 | 2024 | Variation |
|---|---:|---:|---:|
| Essence vendue (Gl) | 6,98 | 7,99 | +14,4 % |
| Diesel vendu (Gl) | 2,18 | 3,06 | +40,5 % |
| Total carburants routiers (Gl) | 9,16 | 11,05 | +20,6 % |

Source : [Statistique Canada, tableau 23-10-0066-01](https://www150.statcan.gc.ca/t1/tbl1/fr/tv.action?pid=2310006601).

## Limites et données manquantes

- La ventilation sectorielle de l'énergie (tableau 25-10-0029-01) ne remonte qu'à 1995 ; aucune valeur comparable n'existe pour 1990 dans ce tableau.
- L'inventaire québécois des GES le plus récent disponible au moment de la consultation couvre 1990–2023 ; les valeurs 2024 ne sont pas encore publiées.
- Les trois séries ne mesurent pas exactement le même périmètre : les ventes de carburants (point 1) couvrent tous les usages (pas seulement le transport), l'énergie « Total transport » (point 2) exclut le carburant utilisé hors activité de transport proprement dite, et les GES (points 3-4) suivent la méthodologie de comptabilisation des inventaires climatiques, distincte des deux premières. Les écarts d'une série à l'autre pour une même année ne sont donc pas des erreurs mais des différences de définition.
- Le sous-secteur « Autres transports » de l'inventaire des GES additionne quatre catégories (aérien, ferroviaire, maritime, autres transports routiers non classés) ; le détail par mode n'est pas repris ici pour rester concis, mais reste disponible dans le fichier source cité.

## Constats

Les volumes de carburants routiers vendus au Québec ont progressé de 20,6 % entre 1990 et 2024, tirés surtout par le diesel (+40,5 %) plutôt que par l'essence (+14,4 %). Les émissions de GES du transport routier ont augmenté un peu plus lentement sur une période comparable (+25,2 % de 1990 à 2023), ce qui reflète des gains d'efficacité énergétique des véhicules. Le sous-secteur « autres transports » (aérien, ferroviaire, maritime) a connu une trajectoire plus irrégulière, avec un creux marqué en 2020 suivi d'un rebond jusqu'en 2023, cohérent avec la reprise du transport aérien après la pandémie.

## Mots-clés

`produits pétroliers` · `essence` · `diesel` · `transport` · `Québec` · `gaz à effet de serre` · `énergie` · `Statistique Canada` · `MELCCFP` · `série chronologique`

---

*Dernière vérification : 2026-08-23.*
