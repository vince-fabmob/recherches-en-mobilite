# Bundle Communauto pour IA — Montréal

> Collez ce document complet dans une IA qui ne suit pas les liens du README. Conçu et validé avec Perplexity; vérifiez toujours les estimations et les tarifs officiels.

## Instruction

Utilise les règles et données ci-dessous pour estimer un trajet Communauto à Montréal. Utilise Économique Extra par défaut. Compare FLEX, station et, à partir de 24 h, Longue distance; retiens l'option admissible la moins chère. Indique hypothèses, coût avant taxes, taxes incluses et niveau de confiance.

## Règles

- Réservation station : minimum 30 min. FLEX : `min(minutes × tarif_minute, plafonds horaire et journalier) + km excédentaires`.
- Pour les forfaits admissibles, comparer FLEX au tarif station; une comparaison station appliquée à FLEX emploie au moins 4 h facturables.
- Longue distance : seulement Économique, Économique Plus et Économique Extra; essence incluse. Comparer si durée ≥ 24 h et date de départ connue. Basse saison : 16 octobre–14 juin; haute saison : 15 juin–15 octobre.
- Si le tarif station de jours additionnels est absent, ne pas l'inventer : comparer tout de même FLEX et Longue distance.
- Montants avant taxes : TPS 5 %, TVQ 9,975 %. Les JSON ci-dessous prévalent sur le texte.

## Cas de test

| Cas | Résultat attendu |
|---|---|
| Économique Extra, 30 min, 10 km | FLEX : 12,90 $ avant taxes |
| Économique Extra, 24 h, 200 km, départ 2026-02-01 | Longue distance : 101,00 $ avant taxes |
| Économique Extra, 25 h, 200 km, départ 2026-02-01 | Station indisponible; Longue distance : 116,00 $ avant taxes, devant FLEX 138,75 $ |
| Liberté, 30 h | Ne pas appliquer Longue distance |

## Données JSON — station et FLEX

```json
{"metadata":{"service":"Communauto Montréal","currency":"CAD","taxes_included":false,"source_officielle":"https://montreal.communauto.com/tarifs/","observed_at":"2026-08-10"},"taxes":{"tps":0.05,"tvq":0.09975,"total":0.14975},"flex_base":{"minute_rate":0.43,"hourly_cap":14.25,"daily_cap":50,"included_distance_km":75,"distance_rate_after_included_km":0.31},"plans":{"liberte":{"label":"Liberté","station":{"hourly_rate":14.25,"first_day_cap":55,"additional_day_rate":50,"included_distance_km":75,"distance_rate":0,"distance_rate_after_km":75,"distance_rate_after_threshold":0.31,"weekend_hourly_surcharge":0.35,"weekend_daily_surcharge":3.5},"flex":{"eligible_for_station_rate_if_lower":false,"long_distance_eligible":false}},"liberte_plus":{"label":"Liberté Plus","station":{"hourly_rate":7.05,"first_day_cap":50,"additional_day_rate":35.5,"included_distance_km":0,"distance_rate":0.29,"distance_rate_after_km":50,"distance_rate_after_threshold":0.26},"flex":{"eligible_for_station_rate_if_lower":true,"long_distance_eligible":false}},"economique":{"label":"Économique","station":{"hourly_rate":3.8,"first_day_cap":31.5,"additional_day_rate":null,"included_distance_km":0,"distance_rate":0.49,"distance_rate_after_km":50,"distance_rate_after_threshold":0.36},"flex":{"eligible_for_station_rate_if_lower":true,"long_distance_eligible":true}},"economique_plus":{"label":"Économique Plus","station":{"hourly_rate":3.3,"first_day_cap":26.5,"additional_day_rate":null,"included_distance_km":0,"distance_rate":0.41,"distance_rate_after_km":50,"distance_rate_after_threshold":0.33},"flex":{"eligible_for_station_rate_if_lower":true,"long_distance_eligible":true}},"economique_extra":{"label":"Économique Extra","station":{"hourly_rate":3,"first_day_cap":23,"additional_day_rate":null,"included_distance_km":0,"distance_rate":0.33,"distance_rate_after_km":null,"distance_rate_after_threshold":null},"flex":{"eligible_for_station_rate_if_lower":true,"long_distance_eligible":true}}}}
```

## Données JSON — Longue distance

```json
{"metadata":{"service":"Communauto Montréal","currency":"CAD","taxes_included":false,"source_officielle":"https://montreal.communauto.com/tarifs/","observed_at":"2026-08-11"},"long_distance":{"eligible_plans":["economique","economique_plus","economique_extra"],"auto_apply_if_cheaper":true,"fuel_included":true,"excess_hour_rate":15,"seasons":{"low":{"start":"10-16","end":"06-14","first_day_rate":45,"additional_day_rate":35,"weekly_rate":210,"distance_rate_until_km":300,"distance_rate":0.28,"distance_rate_after_km":300,"distance_rate_after_threshold":0.19},"high":{"start":"06-15","end":"10-15","first_day_rate":55,"additional_day_rate":45,"weekly_rate":270,"distance_rate_until_km":300,"distance_rate":0.28,"distance_rate_after_km":300,"distance_rate_after_threshold":0.19}}}}
```

## Limites

Estimation seulement. Confirmez disponibilité, zone FLEX, stationnement, véhicule, tarifs et conditions dans l'application Communauto avant réservation.
