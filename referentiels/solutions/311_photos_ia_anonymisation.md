# Photos citoyennes 311, IA et anonymisation

## Objet

Ce répertoire documente les pratiques municipales qui utilisent des photos liées aux demandes de service 311, ou des images comparables du domaine public, pour améliorer le triage, l’étiquetage, la priorisation et la gestion des actifs au moyen de la vision par ordinateur.

L’objectif est d’identifier des approches transférables à Montréal et au Québec qui respectent une logique de protection de la vie privée dès la conception : anonymisation précoce, minimisation des données, supervision humaine et limitation stricte des finalités.

> **Principe de non-surveillance** — Ce type de projet vise l’entretien, la sécurité et l’accessibilité du domaine public. Il ne doit pas servir à identifier des personnes, suivre des déplacements individuels, alimenter des bases biométriques, effectuer une surveillance généralisée ou imposer automatiquement des mesures réglementaires.

## Périmètre

Le corpus couvre trois modèles complémentaires :

- Assistance à la saisie : la photo guide le citoyen vers la bonne catégorie de demande 311
- Triage municipal : la photo est classée, étiquetée, géolocalisée, dédoublonnée ou priorisée après réception
- Détection proactive : des véhicules municipaux ou partenaires captent des images de rue ensuite analysées par IA

Les images citoyennes et la détection proactive ne sont pas équivalentes. Les premières reflètent les problèmes perçus et prioritaires pour les résidents; les secondes peuvent fournir une couverture territoriale plus systématique. Un programme mature peut combiner les deux.

## Cas documentés

| Ville | Entrée visuelle | Usage IA | Protection de la vie privée connue | Statut et intérêt |
|---|---|---|---|---|
| New York, États-Unis | Photo téléversée dans NYC311 | AI Smart Select propose un formulaire de demande de service à partir d’une photo | Les pages publiques consultées ne suffisent pas à établir un protocole détaillé d’anonymisation d’image; il faut vérifier la politique de confidentialité et l’architecture fournisseur | Cas direct photo citoyenne → suggestion de catégorie 311 |
| San Francisco, États-Unis | Photos jointes à SF311 | Smart photo recognition suggère le bon type de requête et reconnaît certains détails, dont des objets et des plaques | Le mécanisme de floutage, la conservation et le réemploi pour l’entraînement ne sont pas documentés dans la page produit consultée | Cas direct d’assistance à la déclaration 311 |
| Cleveland, États-Unis | Images captées depuis un véhicule municipal, parallèlement au 311 | City Detect détecte des conditions de propriété et produit des dossiers à réviser | Visages et plaques floutés; la Ville indique ne pas recevoir les images non expurgées; inspection humaine avant intervention coercitive | Référence forte en matière de séparation entre IA, anonymisation et décision humaine |
| San José, États-Unis | Images de voirie captées depuis des véhicules | Vision IA pour risques routiers et enjeux municipaux, avec géolocalisation et score de confiance | Documentation publique à compléter au niveau des modalités précises de traitement et de conservation | Cas pertinent pour la voirie, les nids-de-poule et les obstructions |
| Markham, Canada | Images captées par CITYROVER | Détection de conditions du domaine public par vision IA | Le fournisseur indique un floutage intégré des plaques, visages et autres renseignements personnels | Cas canadien utile pour un balayage municipal anonymisé |
| Boston / Jamaica Plain, États-Unis | Historique de 311 et inventaire visuel de chaussée distinct | Comparaison analytique entre signalements résidents et défauts détectés par vision | Information non établie dans la source consultée | Montre que les plaintes 311 et la détection proactive couvrent des problèmes largement différents |

## Enseignements

- L’IA doit être conçue comme une aide au classement, à la priorisation et à l’inspection, non comme un mécanisme de sanction automatisé
- La confirmation par un employé ou un inspecteur est requise pour les cas à incidence élevée, les faibles niveaux de confiance et toute intervention réglementaire
- Une photo citoyenne est un signal de vécu et de priorité sociale; elle ne doit pas être assimilée à un inventaire objectif de l’état du réseau
- La détection proactive réduit les angles morts territoriaux, mais peut créer de nouveaux risques de surveillance si elle n’est pas strictement encadrée
- Les modèles doivent pouvoir proposer plusieurs étiquettes et exprimer leur incertitude plutôt que forcer une classification unique

## Architecture cible proposée

1. Le citoyen transmet une photo, une localisation approximative et une description dans le canal 311.
2. Le système retire les métadonnées non nécessaires, notamment les EXIF et identifiants d’appareil.
3. Avant toute consultation large ou tout entraînement, un service d’anonymisation détecte et masque les visages, les plaques, les numéros civiques et, selon le cas, les éléments privés visibles.
4. Le modèle de vision produit des étiquettes, une probabilité, une estimation de gravité et des indices utiles au routage.
5. La plateforme suggère une catégorie au citoyen ou au préposé, sans empêcher le dépôt d’une demande divergente.
6. Les cas sont regroupés avec prudence selon le lieu, le temps et le type, sans effacer les demandes qui signalent des impacts distincts.
7. Un agent municipal valide les signalements à faible confiance ou à incidence élevée.
8. Les originaux sont supprimés selon une période de conservation définie; les données de performance reposent ensuite sur des versions anonymisées ou des attributs dérivés.

## Catégories pilotes envisageables

- Nids-de-poule, fissures, affaissements et dégradation de chaussée
- Signalisation ou marquage routier endommagé, masqué ou absent
- Trottoirs, traversées et aménagements universels obstrués ou dégradés
- Pistes cyclables obstruées ou mobilier de mobilité endommagé
- Dépôts sauvages, corbeilles débordantes et déchets sur le domaine public
- Graffitis
- Enjeux hivernaux : déneigement, glace, accès aux arrêts et traversées impraticables

## Exigences minimales de gouvernance

- Floutage des visages et plaques avant l’accès par les services municipaux lorsque ces éléments ne sont pas nécessaires à la demande
- Suppression des métadonnées qui ne sont pas nécessaires à la prestation du service
- Séparation technique entre le dossier nominatif 311 et un corpus d’images anonymisées servant à l’analyse ou à l’amélioration des modèles
- Durée de conservation courte, explicitement publiée et appliquée automatiquement
- Interdiction de la reconnaissance faciale, de l’identification de personnes et des réemplois secondaires incompatibles
- Interdiction d’utiliser une étiquette IA comme seule base d’une sanction, d’une inspection coercitive ou d’une décision défavorable
- Contrôle humain, échantillonnage qualité et voie de correction des erreurs
- Évaluation des facteurs relatifs à la vie privée avant le pilote et ententes contractuelles précises avec les fournisseurs
- Audit régulier de précision, d’erreurs, de performance par arrondissement et de biais socio-territoriaux
- Transparence publique : finalités, catégories, fournisseurs, durées de conservation, taux d’erreur et mécanisme de plainte
- Traitement local ou dans l’environnement municipal de confiance avant transmission lorsque cela est techniquement possible
- Chiffrement en transit et au repos, contrôle d’accès fondé sur les rôles, authentification multifacteur et journalisation des accès
- Clauses fournisseurs interdisant la vente, la publicité comportementale, la réidentification, les transferts non autorisés et l’entraînement de modèles avec les images municipales sans autorisation explicite
- Plan de réponse aux incidents : détection, confinement, avis, suppression ou révocation des données compromises, analyse des causes et suivi public

## Risques, limites et incidents documentés

### Le floutage ne rend pas une image automatiquement anonyme

Le floutage des visages et des plaques est une mesure nécessaire, mais insuffisante à lui seul. Une personne peut rester reconnaissable par le lieu, l’heure, sa silhouette, ses vêtements, un véhicule, son domicile, son activité ou la combinaison de ces éléments. La densité spatiale et temporelle d’images de rue peut aussi permettre des inférences sur des groupes ou des activités sensibles, même lorsque les visages et plaques sont masqués.

Conséquence : une architecture sécuritaire ne doit pas reposer uniquement sur le floutage. Elle doit minimiser la collecte, traiter les images au plus près de la source, limiter la conservation, réduire l’accès aux originaux et conserver autant que possible des attributs dérivés plutôt que les images.

### Incidents et précédents utiles

| Cas | Ce qui s’est produit | Leçon pour un projet 311 / vision municipale |
|---|---|---|
| Google Street View, 2008–2010 | Des véhicules Street View ont capté des données de réseaux Wi-Fi non chiffrés, allant au-delà de la finalité de cartographie annoncée. Des autorités ont imposé des sanctions, notamment aux États-Unis et en Allemagne. | Interdire explicitement toute captation de données réseau, audio ou capteurs non nécessaires. Faire auditer les équipements, micrologiciels et paramètres de collecte. |
| Clearview AI, Canada, 2021 | Les commissaires à la vie privée du Canada, du Québec, de la Colombie-Britannique et de l’Alberta ont conclu que la collecte massive d’images et l’usage de reconnaissance faciale sans consentement enfreignaient les lois applicables. | Interdiction formelle de reconnaissance faciale, d’identification biométrique, de recherche d’identité et de réutilisation des images pour constituer un corpus biométrique. |
| Images de rue à haute densité | La recherche montre que le floutage des visages et plaques ne neutralise pas les risques d’identification contextuelle ni certaines inférences sur des groupes sensibles. | Réduire la fréquence, la résolution, le champ de vision et la durée de conservation; empêcher les requêtes exploratoires par lieu ou personne; évaluer les risques de réidentification. |
| Données de lecture de plaques et surveillance urbaine | Des systèmes de caméras peuvent dériver vers des usages de surveillance secondaire, notamment par le partage interinstitutionnel ou des recherches non liées à la mission initiale. | Établir une interdiction de partage avec des bases policières ou de contrôle migratoire, sauf base légale distincte, processus public, journalisation et approbation explicite. |

## Indicateurs d’évaluation

| Dimension | Indicateurs proposés |
|---|---|
| Qualité du modèle | précision, rappel, taux de rejet, taux de correction humaine, performance par catégorie |
| Efficacité opérationnelle | temps médian de triage, taux de réacheminement, délai jusqu’à la première action, volume dédoublonné |
| Service aux résidents | taux de dépôt réussi, compréhension de la catégorie suggérée, satisfaction, accessibilité linguistique et numérique |
| Équité territoriale | couverture par arrondissement, taux d’erreur par secteur, délais de traitement et écarts de service |
| Vie privée | part d’images anonymisées avant consultation, échecs de floutage, durée réelle de rétention, incidents et demandes d’accès ou de suppression |
| Gestion d’actifs | défauts confirmés, gravité, récurrence spatiale, délai de réparation, diminution des incidents récurrents |

## Questions à documenter avant déploiement

- Quelles catégories 311 comportent suffisamment de photos, et de qualité suffisante, pour soutenir un pilote?
- Les photos sont-elles rendues publiques, partagées entre services ou conservées dans des systèmes distincts?
- Quel est le rôle de la géolocalisation : coordonnées précises, adresse déclarée ou position approximative?
- Les images peuvent-elles être traitées sur une infrastructure municipale, québécoise ou canadienne?
- Un fournisseur peut-il conserver les images, les réutiliser ou entraîner ses modèles avec celles-ci? La réponse devrait être non sans autorisation explicite et encadrement approprié.
- Quels usages présentent un risque disproportionné : personnes, immeubles résidentiels, mineurs, plaintes de voisinage ou application réglementaire?
- Quels mécanismes permettront de vérifier la qualité du floutage avant tout partage, publication ou entraînement?

## Sources initiales

- NYC311, *AI Smart Select* dans les fiches des boutiques d’applications : la fonction permet de prendre une photo d’un problème et de recevoir une suggestion de formulaire de demande de service. https://play.google.com/store/apps/details?id=gov.nyc.doitt.ThreeOneOne
- SF.gov, *SF311 mobile app* : la fonction Smart photo recognition permet de joindre des photos et suggère un type de demande, avec reconnaissance de détails visuels. https://www.sf.gov/sf311-mobile-app
- City of Cleveland, *Citizen Support Vehicle* : partenariat City Detect pour la détection proactive de conditions urbaines. https://www.clevelandohio.gov/311/citizen-support-vehicle
- Signal Cleveland, *Cleveland wants more eyes on city property conditions* : éléments publics sur le floutage des visages et plaques et l’absence d’accès municipal aux images non expurgées. https://signalcleveland.org/cleveland-property-conditions-ai-photos-city-detect/
- City Detect, *Responsible AI Strategy* : déclarations du fournisseur sur le floutage par défaut, l’absence de suivi d’information personnelle et l’absence de liens avec des bases fédérales ou policières. https://www.citydetect.com/responsible-ai-strategy
- StateScoop, *AI now powers street hazard detection in San Jose, Calif.* : détection IA de risques routiers à San José. https://statescoop.com/san-jose-ai-street-hazard-detection/
- CITYROVER, *City of San José, CA* : cas d’usage de vision IA pour risques routiers et enjeux de service municipal. https://www.cityrover.com/case-studies/city-of-san-jose-ca/
- CITYROVER, *Markham, ON* : le fournisseur décrit le floutage intégré des plaques, visages et autres renseignements personnels. https://www.cityrover.com/wp-content/uploads/2025/04/Markham-brochure-cityrover-for-CITYROVER-site-14.pdf
- Harvard Data-Smart City Solutions, *When Residents and Algorithms See Different Problems* : comparaison entre 187 408 signalements 311 de Jamaica Plain et 4 856 défauts routiers détectés par vision. https://datasmart.hks.harvard.edu/residents-algorithms-see-different-problems
- Commissariat à la protection de la vie privée du Canada, *Enquête conjointe sur Clearview AI* : conclusions concernant la collecte et l’usage de reconnaissance faciale. https://www.priv.gc.ca/en/opc-actions-and-decisions/investigations/investigations-into-businesses/2021/pipeda-2021-001/
- Reuters, *German state fines Google for Street View data breach* : sanction liée à la collecte de données Wi-Fi durant la captation Street View. https://www.reuters.com/article/technology/german-state-fines-google-for-street-view-data-breach-idUSBRE93L0VU/
- BBC, *Google hit by $7m Street View fine in US* : règlement relatif à la collecte de données Wi-Fi. https://www.bbc.com/news/technology-21762545
- Taylor & Francis, *From object obfuscation to contextually-dependent identification* : limites de l’obfuscation et risque d’identification contextuelle dans les plateformes d’images de rue. https://www.tandfonline.com/doi/full/10.1080/13600834.2024.2321052

## Statut du référentiel

Version initiale révisée le 24 août 2026.

Le contenu doit être mis à jour avant toute décision de déploiement : les fonctionnalités de produits, politiques de conservation, contrats fournisseurs et exigences légales évoluent rapidement.