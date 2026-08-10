# Transport Montréal — données de mobilité

Jeu de données versionné et règles de calcul pour assister la planification de trajets multimodaux à Montréal : Communauto, BIXI, STM et Leo Autopartage.

## Statut

Version : `2.0.0-draft.1`  
Dernière révision éditoriale : 2026-08-10  
Territoire : Montréal, Québec, Canada  
Devise : CAD

Cette publication est une base de données et de calcul. Elle ne remplace pas les conditions de service des opérateurs ni leurs applications. Les données de disponibilité, de circulation, de météo et de tarification dynamique doivent être vérifiées en temps réel.

## Contenu

- `donnees_transport_montreal.v2.json` : données, provenance et règles de calcul;
- `../../methodes/estimation-couts-autopartage-communauto-montreal.md` : méthode d’estimation Communauto;
- `../../scripts/convert_flex_zones_to_geojson.py` : conversion du fichier de zones FLEX existant vers GeoJSON.

## Règle Communauto FLEX

Pour un déplacement réalisable en FLEX, l’estimation doit comparer le tarif FLEX et le tarif stationnaire Économique Extra pour la même durée et distance. Le calcul retient le montant le plus bas lorsque les conditions tarifaires de Communauto le permettent. La possibilité de terminer le trajet doit toujours être confirmée dans l’application Communauto.

## Sources officielles

- Communauto : https://montreal.communauto.com/tarifs/
- BIXI : https://bixi.com/fr/tarifs/
- STM : https://www.stm.info/
- Leo Autopartage : https://leoautopartage.com/tarifs/

## Mise à jour

Vérifier les tarifs mensuellement; vérifier les zones FLEX après tout changement détecté dans l’application ou son flux de zones; consigner la date de vérification dans Git. Vérifier les droits de réutilisation des données des opérateurs avant toute republication.