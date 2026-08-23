# Consommation de produits pétroliers au Québec

> **Document de travail — à réviser collectivement.** Ce répertoire recense des sources publiques permettant de suivre la consommation, l'approvisionnement, le raffinage, les importations et les émissions de GES associées aux produits pétroliers au Québec. Il ne reproduit pas les données chiffrées de ces sources. Vérifier l'unité, la méthode, le millésime, la couverture géographique et les conditions d'accès directement auprès de chaque producteur avant toute utilisation.
>
> **Contributions bienvenues.** Les liens manquants, changements de tableau, ruptures de série ou précisions méthodologiques peuvent être proposés par issue ou pull request. Consultez [CONTRIBUTING.md](../CONTRIBUTING.md).

## Objet

Aucune source unique ne décrit à elle seule « la consommation de produits pétroliers au Québec ». Plusieurs producteurs publient des mesures complémentaires mais distinctes : volumes vendus au détail, bilan offre-demande du raffinage, importations douanières, bilan énergétique agrégé, émissions de GES qui en résultent, et parc de véhicules qui explique une partie de la demande. Ce répertoire aide à repérer la bonne source selon la question posée, sans en reproduire les valeurs.

## Concepts à distinguer

| Concept | Description | Précaution |
|---|---|---|
| Ventes de carburants routiers | Volumes d'essence et de carburant diesel vendus au détail pour les véhicules automobiles | Mesure les ventes, pas nécessairement la consommation réelle sur le territoire (achats transfrontaliers, stocks) |
| Approvisionnement et utilisation de produits pétroliers | Bilan mensuel production, importations, exportations, stocks et livraisons de produits raffinés | Portée généralement nationale ou régionale (Canada, Québec/Ontario/Atlantique regroupés selon le tableau); vérifier le niveau géographique exact |
| Utilisation finale des produits pétroliers raffinés | Répartition annuelle de la consommation par secteur (transport, résidentiel, industrie, etc.), habituellement en térajoules | Agrégat énergétique, pas un volume de litres directement comparable aux ventes au détail |
| Raffinage et pétrole brut | Charges de brut traitées par les raffineries, approvisionnement en pétrole brut, origine des arrivages | Ne mesure pas la consommation finale; le brut raffiné au Québec n'est pas nécessairement consommé au Québec |
| Importations (commerce international) | Valeur et parfois volumes de produits pétroliers déclarés aux douanes | Les statistiques de commerce extérieur utilisent des catégories douanières; les valeurs sont souvent en dollars, pas en volumes |
| Bilan énergétique agrégé (État de l'énergie au Québec) | Synthèse annuelle multi-source de la consommation d'énergie par secteur et par forme d'énergie | Synthèse secondaire; citer la source primaire indiquée dans chaque édition |
| Émissions de GES du transport | Émissions résultant de la combustion de carburants, en Mt éq. CO₂ | Mesure indirecte : ne donne pas un volume de litres et dépend de facteurs d'émission et de méthodes d'inventaire |
| Parc de véhicules et véhicules-kilomètres (VKT) | Nombre de véhicules en circulation et distances parcourues | Explique une partie de la demande de carburant, mais ne mesure pas directement la consommation |

## Répertoire des sources — ventes et prix de carburants routiers

| Source | Ressource | Portée | Accès et précautions |
|---|---|---|---|
| Statistique Canada | [Tableau 23-10-0066-01 — Ventes de carburants destinés aux véhicules automobiles, annuel](https://www150.statcan.gc.ca/t1/tbl1/fr/tv.action?pid=2310006601) · [miroir Gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/6797dd39-8a2d-4ec3-b285-6123ef61699b) | Canada, provinces et territoires | Volumes annuels d'essence et de carburant diesel vendus au détail (x 1 000 litres). Vérifier la période couverte et les révisions. |
| Statistique Canada | [Tableau 18-10-0001-01 — Prix de détail moyens mensuels, essence et mazout, par géographie](https://www150.statcan.gc.ca/t1/tbl1/fr/tv.action?pid=1810000101) | Canada, grandes villes | Série mensuelle de prix; ne renseigne pas les volumes vendus. |
| Statistique Canada | [Graphique — Ventes brutes d'essence au Canada, 2004 à 2024](https://www150.statcan.gc.ca/n1/daily-quotidien/250922/cg-e001-fra.htm) | Canada | Communiqué du Quotidien présentant une série longue; vérifier la source tabulaire sous-jacente avant réutilisation. |

## Répertoire des sources — utilisation finale des produits pétroliers raffinés (bilan sectoriel annuel)

| Édition | Lien | Précaution |
|---|---|---|
| Année de référence 2024 | [Le Quotidien, 7 novembre 2025](https://www150.statcan.gc.ca/n1/daily-quotidien/251107/dq251107d-fra.htm) | Répartition par secteur en térajoules; vérifier la définition du secteur transport utilisée. |
| Année de référence 2023 | [Le Quotidien, 18 novembre 2024](https://www150.statcan.gc.ca/n1/daily-quotidien/241118/dq241118b-fra.htm) | — |
| Année de référence 2022 | [Le Quotidien, 17 novembre 2023](https://www150.statcan.gc.ca/n1/daily-quotidien/231117/dq231117e-fra.htm) | — |
| Année de référence 2020 | [Le Quotidien, 18 novembre 2021](https://www150.statcan.gc.ca/n1/daily-quotidien/211118/dq211118c-fra.htm) | Éditions publiées annuellement avec un décalage d'environ un an; vérifier si une édition plus récente existe. |

## Répertoire des sources — raffinage, approvisionnement et pétrole brut

| Source | Ressource | Portée | Accès et précautions |
|---|---|---|---|
| Statistique Canada | [Tableau 25-10-0081-01 — Approvisionnement et utilisation de produits pétroliers, mensuel](https://www150.statcan.gc.ca/t1/tbl1/fr/tv.action?pid=2510008101) · [miroir Open Government](https://open.canada.ca/data/en/dataset/792aad48-1745-41dd-8424-55e49d98fa0c) | Canada et régions | Bilan mensuel production/importations/exportations/stocks par produit. L'ancien tableau 25-10-0076-01 est marqué [inactif](https://www150.statcan.gc.ca/n1/fr/catalogue/2510007601); ne pas l'utiliser pour des données récentes. |
| Statistique Canada | [Approvisionnement et utilisation du pétrole brut et équivalent](https://ouvert.canada.ca/data/fr/dataset/386b0b66-916d-4c36-96f1-2493076b0ae3) | Canada et régions | Bilan du pétrole brut, distinct des produits raffinés. |
| Statistique Canada | [Pétrole brut et pentanes plus, arrivages et utilisation mensuels par région d'origine](https://ouvert.canada.ca/data/fr/dataset/fcbbc7e7-1a3f-4998-9263-745d65503a9a) | Canada, par région d'origine | Utile pour tracer l'origine du brut traité dans les raffineries desservant le Québec. |
| Régie de l'énergie du Canada (REC/CER) | [Aperçu des marchés — Charges de brut des raffineries canadiennes](https://www.cer-rec.gc.ca/fr/donnees-analyse/marches-energetiques/apercu-marches/2026/apercu-marche-charges-de-brut-des-raffineries-canadiennes-stables-en-2025.html) · [jeu de données associé](https://ouvert.canada.ca/data/fr/dataset/5c0099e0-7081-404e-a95f-b0541de06630) | Canada, par raffinerie/région | Analyses de marché publiées par la Régie; vérifier la couverture des raffineries québécoises. |
| Statistique Canada | [Transport du pétrole brut et des produits pétroliers raffinés par pipeline](https://www150.statcan.gc.ca/n1/fr/catalogue/55-201-X) | Canada | Catalogue marqué **ARCHIVÉ** : ne pas présumer d'une mise à jour continue; vérifier s'il existe un successeur avant utilisation. |
| Statistique Canada | [Bulletin sur la disponibilité et l'écoulement de l'énergie au Canada (57-003-X)](https://www150.statcan.gc.ca/n1/fr/catalogue/57-003-X) — éditions [2023](https://www150.statcan.gc.ca/n1/pub/57-003-x/57-003-x2023001-fra.htm) et [2025](https://www150.statcan.gc.ca/n1/pub/57-003-x/57-003-x2025001-fra.htm) | Canada | Bulletin explicatif accompagnant les statistiques énergétiques; utile pour comprendre la méthode avant d'utiliser les tableaux. |
| Ressources naturelles Canada | [Centre canadien d'information sur l'énergie — Produits pétroliers raffinés](https://information-energie.canada.ca/fr/sujets/produits-petroliers-raffines) · [Ressources générales](https://information-energie.canada.ca/fr/ressources) | Canada | Portail de vulgarisation regroupant des liens vers les statistiques fédérales sur les produits pétroliers. |

## Répertoire des sources — importations et commerce international

| Source | Ressource | Portée | Accès et précautions |
|---|---|---|---|
| Institut de la statistique du Québec (ISQ) | [Commerce international de marchandises](https://statistique.quebec.ca/fr/produit/publication/commerce-international-marchandises) · [données mensuelles](https://statistique.quebec.ca/fr/document/commerce-international-donnees-mensuelles) · [données annuelles](https://statistique.quebec.ca/fr/document/commerce-international-donnees-annuelles) · [bulletin](https://statistique.quebec.ca/fr/document/commerce-international-de-marchandises-du-quebec-bulletin) | Québec | Classement par catégories douanières; les produits pétroliers y apparaissent comme poste commercial. Vérifier si les valeurs sont exprimées en dollars, en volumes, ou les deux. |
| Ministère de l'Économie, de l'Innovation et de l'Énergie (MEIE) | [Calepin du commerce extérieur du Québec](https://www.economie.gouv.qc.ca/bibliotheques/etudes-et-analyses/analyses-et-indicateurs-sur-les-echanges-exterieurs/calepin-le-commerce-exterieur-du-quebec) · [PDF](https://www.economie.gouv.qc.ca/fileadmin/contenu/publications/etudes_statistiques/echanges_exterieurs/calepin_exterieur.pdf) | Québec | Publication périodique synthétisant les échanges extérieurs; vérifier le niveau de détail par produit pétrolier. |

## Répertoire des sources — bilan énergétique global (État de l'énergie au Québec)

| Source | Ressource | Portée | Accès et précautions |
|---|---|---|---|
| Chaire de gestion du secteur de l'énergie, HEC Montréal | [État de l'énergie au Québec — page d'accueil](https://energie.hec.ca/eeq/) | Québec | Rapport annuel de synthèse. Éditions PDF : [2020](https://energie.hec.ca/wp-content/uploads/2020/03/EEQ2020_WEB.pdf) · [2023](https://energie.hec.ca/wp-content/uploads/2023/05/EEQ2023_WEB.pdf) · [2024](https://energie.hec.ca/wp-content/uploads/2024/03/EEQ2024_WEB.pdf) · [2025](https://energie.hec.ca/wp-content/uploads/2025/03/EEQ2025_WEB.pdf) · [2026](https://energie.hec.ca/wp-content/uploads/2026/02/EEQ2026_web.pdf). |
| HEC Montréal (communiqués) | Contexte par édition : [2023](https://www.hec.ca/salle_de_presse/communiques/2023/chaire-gestion-secteur-energie-hec-montreal-publie-etat-de-l-energie-au-quebec-2023.html) · [2024](https://www.hec.ca/nouvelles/2024/dixieme-edition-etat-energie-au-quebec.html) · [2025](https://www.hec.ca/salle_de_presse/communiques/2025/chaire-gestion-secteur-energie-hec-montreal-publie-onzieme-edition-etat-de-energie-au-quebec.html) · [2026](https://www.hec.ca/nouvelles/2026/letat-de-lenergie-au-quebec-2026-dresse-un-bilan-contraste) | Québec | Communiqués de presse résumant les constats de chaque édition; ne remplacent pas le rapport complet. |

Voir aussi la fiche existante [État de l'énergie au Québec — Tableau 9 : parc de véhicules et énergie](etat-energie-quebec-tableau-9-parc-vehicules-energie.md), qui indexe spécifiquement le tableau sur le parc routier et l'énergie.

## Répertoire des sources — émissions de GES associées au transport

| Source | Ressource | Portée | Accès et précautions |
|---|---|---|---|
| MELCCFP | [Inventaire québécois des émissions de GES — page index](https://www.environnement.gouv.qc.ca/changements/ges/index.htm) · [rapport 1990-2022](https://www.environnement.gouv.qc.ca/changements/ges/2022/inventaire-ges-1990-2022.pdf) · [supplément méthodologique](https://www.environnement.gouv.qc.ca/changements/ges/2022/inventaire-1990-2022-supplement-calculs.pdf) | Québec | Émissions en Mt éq. CO₂ par secteur, incluant le transport. Ne fournit pas de volumes de carburant; vérifier la méthode de calcul et le secteur exact (véhicules légers, lourds, autres transports). |
| Données Québec | [Inventaire québécois des émissions de GES (jeu de données)](https://www.donneesquebec.ca/recherche/dataset/inventaire-quebecois-des-emissions-de-gaz-a-effet-de-serre/resource/99fb6b0e-edac-455f-8c8a-c0bb4ef92255) · [Registre des émissions de GES des grands émetteurs](https://www.donneesquebec.ca/recherche/dataset/registre-des-emissions-de-gaz-a-effet-de-serre) | Québec | Le registre des grands émetteurs couvre les établissements industriels déclarants, pas l'ensemble du secteur transport. |
| Statistique Québec (ISQ) | [Émissions de gaz à effet de serre (GES) — indicateur](https://statistique.quebec.ca/fr/produit/publication/indicateurs-progres-emissions-ges) | Québec | Indicateur de suivi; vérifier l'année de référence et la source primaire citée. |
| Gouvernement du Québec | [Plan pour une économie verte 2030](https://www.quebec.ca/gouvernement/politiques-orientations/plan-economie-verte) — plans de mise en œuvre : [2021-2026](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/environnement/publications-adm/plan-economie-verte/plan-mise-oeuvre-2021-2026.pdf) · [2022-2027](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/environnement/publications-adm/plan-economie-verte/plan-mise-oeuvre-2022-2027.pdf) · [2023-2028](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/environnement/publications-adm/plan-economie-verte/plan-mise-oeuvre-2023-2028.pdf) · [2025-2030](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/environnement/publications-adm/plan-economie-verte/plan-mise-oeuvre-2025-2030.pdf) · [2026-2031](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/environnement/publications-adm/plan-economie-verte/plan-mise-oeuvre-2026-2031.pdf) | Québec | Chaque édition présente un scénario de référence et des cibles sectorielles; les rééditions annuelles peuvent modifier la méthode ou les scénarios. Voir aussi [état d'avancement de l'action climatique gouvernementale](https://www.quebec.ca/gouvernement/politiques-orientations/plan-economie-verte/gouvernance-diffusion-resultats/etat-avancement-action-climatique-gouvernementale). |
| Gouvernement du Canada | [Inventaire national des émissions de GES](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/emissions-gaz-effet-serre/inventaire/emissions.html) · [Sources et puits de GES au Canada — sommaire 2025](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/emissions-gaz-effet-serre/sources-puits-sommaire-2025.html) | Canada, ventilé par province | Méthodologie fédérale, distincte de l'inventaire québécois; vérifier les écarts de méthode avant de comparer les deux séries. |

## Répertoire des sources — parc de véhicules et déplacements (contexte de la demande)

| Source | Ressource | Portée | Accès et précautions |
|---|---|---|---|
| Ressources naturelles Canada (OEE) | [Base nationale de données sur la consommation d'énergie — accueil](https://oee.rncan.gc.ca/organisme/statistiques/bnce/apd/accueil.cfm) · [tableaux complets par secteur transport](https://oee.nrcan.gc.ca/organisme/statistiques/bnce/apd/menus/evolution/tableaux_complets/liste.cfm) | Canada et provinces | Séries énergétiques sectorielles utiles pour situer le transport routier par rapport aux autres secteurs. |
| Données Québec / SAAQ | [Véhicules en circulation (jeu de données)](https://www.donneesquebec.ca/recherche/dataset/vehicules-en-circulation) · exemples de rapports annuels : [2022](https://saaq.gouv.qc.ca/blob/saaq/documents/publications/donnees-statistiques-2022.pdf), [2020](https://saaq.gouv.qc.ca/blob/saaq/documents/publications/donnees-statistiques-2020.pdf), [2019](https://saaq.gouv.qc.ca/blob/saaq/documents/publications/donnees-statistiques-2019.pdf), [2017](https://saaq.gouv.qc.ca/blob/saaq/documents/publications/donnees-statistiques-2017.pdf) | Québec | Parc immatriculé, pas une mesure directe de consommation. Voir la fiche [Véhicules, électrification et recharge au Québec](vehicules-electrification-recharge-quebec.md) pour le détail des concepts. |
| Statistique Canada | [Enquête sur les véhicules au Canada (EVC) — description de l'enquête](https://www23.statcan.gc.ca/imdb/p2SV_f.pl?Function=getSurvey&Id=31393) — exemple de tableau : [véhicules-kilomètres par type de véhicule (23-10-0198-01)](https://www150.statcan.gc.ca/t1/tbl1/fr/tv.action?pid=2310019801) | Canada, provinces et territoires | **Enquête largement discontinuée** : plusieurs tableaux associés n'ont pas été mis à jour depuis la fin des années 2000; vérifier la date de dernière diffusion avant d'utiliser ces séries pour une analyse récente. |

## Usages possibles

- Repérer la source pertinente selon que la question porte sur les ventes au détail, le bilan raffinage/approvisionnement, les importations, le bilan énergétique global ou les émissions de GES.
- Construire un tableau de bord distinguant explicitement litres vendus, térajoules consommés et Mt éq. CO₂ émises, plutôt que de les traiter comme une seule série.
- Suivre l'évolution du poids relatif des « autres transports » (aviation, maritime, ferroviaire, hors route) dans les inventaires de GES, en complément des véhicules légers et lourds.
- Alimenter des analyses publiées (par exemple sur Medium) en citant systématiquement la source primaire et sa date de consultation.

## Limites et précautions

- Ce dépôt ne reproduit aucune valeur chiffrée : chaque tableau ou rapport doit être consulté directement à la source pour obtenir les données.
- Les ventes de carburants au détail, le bilan d'approvisionnement, l'utilisation finale par secteur et les émissions de GES ne sont pas des mesures interchangeables; elles ont des unités, des méthodes et des périmètres différents.
- Plusieurs séries fédérales portent sur le Canada dans son ensemble ou sur des regroupements régionaux; vérifier si le Québec est isolé ou agrégé avec d'autres provinces avant toute comparaison.
- Certaines ressources sont explicitement archivées ou inactives (transport par pipeline 55-201-X, ancien tableau 25-10-0076-01, Enquête sur les véhicules au Canada pour la plupart de ses tableaux); vérifier le statut de mise à jour avant utilisation.
- Les statistiques de commerce extérieur (ISQ, MEIE) utilisent des catégories douanières qui ne correspondent pas nécessairement à un découpage par produit pétrolier fin (essence, diesel, carburéacteur, mazout).
- Les émissions de GES du transport sont un résultat calculé, pas une mesure directe de volumes de carburant; une variation d'émissions peut refléter un changement de méthode ou de facteur d'émission autant qu'un changement réel de consommation.
- Les rapports de synthèse (État de l'énergie au Québec, Plan pour une économie verte) sont des sources secondaires qui citent des données primaires; toujours remonter à la source primaire indiquée dans le document pour une réutilisation rigoureuse.

## Ressources associées

- [Producteurs de données de mobilité au Québec](producteurs-donnees-mobilite-quebec.md)
- [Véhicules, électrification et recharge au Québec](vehicules-electrification-recharge-quebec.md)
- [État de l'énergie au Québec — Tableau 9 : parc de véhicules et énergie](etat-energie-quebec-tableau-9-parc-vehicules-energie.md)
- [MTMD — Débits de circulation](debits-circulation-mtmd-quebec.md)
- [Guide de comparabilité des données de mobilité](../methodes/comparabilite-des-donnees-mobilite.md)
- [Analyse : Évolution de la consommation de produits pétroliers en transport au Québec](../analyses/evolution-consommation-produits-petroliers-transport-quebec.md)

## À compléter

- [ ] Vérifier périodiquement si les identifiants de tableaux Statistique Canada (23-10-0066-01, 18-10-0001-01, 25-10-0081-01, 57-003-X) ont changé ou ont été remplacés.
- [ ] Ajouter un lien direct vers le détail par produit (essence, diesel, carburéacteur, mazout) lorsque disponible dans le bilan d'approvisionnement.
- [ ] Confirmer si l'Enquête sur les véhicules au Canada publie encore des tableaux actifs pour le Québec, ou identifier une source de remplacement pour les véhicules-kilomètres.
- [ ] Ajouter les données de la Régie de l'énergie du Canada spécifiques aux raffineries situées au Québec, si publiées séparément.
- [ ] Documenter les licences et conditions de réutilisation précises de chaque tableau (StatCan, ISQ, MELCCFP, HEC Montréal).
- [ ] Vérifier si une édition plus récente du bilan « Utilisation finale des produits pétroliers raffinés » a été publiée après l'année de référence 2024.

## Mots-clés

`produits pétroliers` · `essence` · `diesel` · `raffinage` · `approvisionnement énergétique` · `importations` · `commerce international` · `GES transport` · `Plan pour une économie verte` · `État de l'énergie au Québec` · `Québec`

*Dernière vérification : 23 août 2026.*
