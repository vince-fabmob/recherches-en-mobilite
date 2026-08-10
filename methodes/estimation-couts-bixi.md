# Estimation des coûts BIXI à Montréal

## Objet

Cette méthode estime le coût d’un trajet BIXI à Montréal. Elle sert à comparer BIXI avec les autres modes de transport; elle ne remplace pas le prix présenté dans l’application BIXI.

## Périmètre et données requises

- Lieu et heure de départ et d’arrivée, afin de vérifier l’existence de stations, la disponibilité des vélos et des ancrages, ainsi que les conditions météo.
- Durée estimée en minutes `t`, nombre de segments BIXI `n`, type de vélo (régulier ou électrique), forfait et statut de membre.
- Frais d’abonnement déjà payés : les exclure du coût marginal du trajet, mais les afficher séparément dans une analyse de coût total annuel.

## Tarifs de référence

Les montants doivent être validés dans la page officielle BIXI avant chaque mise à jour du calculateur. À titre de paramètres initiaux pour 2026, les membres saisonniers ou mensuels ont des trajets réguliers de 45 minutes ou moins inclus; un dépassement et un trajet électrique sont facturés 0,19 $/min. Le trajet ponctuel comprend des frais de déverrouillage et des frais/minute distincts selon le type de vélo. Les montants sont avant taxes.

Source : https://bixi.com/fr/tarifs/

## Formules

### Membre — vélo régulier

Pour chaque segment `i` :

```text
C_i = max(0, t_i - 45) × r_depassement
```

### Membre — vélo électrique

```text
C_i = t_i × r_electrique
```

### Utilisateur ponctuel

```text
C_i = frais_deverrouillage + t_i × r_type_velo
```

### Total

```text
C_sous_total = somme(C_i) + frais_remorque + frais_penalite
C_total = C_sous_total × (1 + taux_TPS_TVQ)
```

Ne jamais agréger plusieurs segments : la période incluse d’un membre se réinitialise lorsque le vélo est correctement retourné et verrouillé à une station.

## Exemple

Membre, vélo régulier, deux segments de 35 minutes :

```text
C = max(0, 35 - 45) × 0,19 + max(0, 35 - 45) × 0,19 = 0 $ avant taxes
```

Membre, vélo électrique, 20 minutes :

```text
C = 20 × 0,19 = 3,80 $ avant taxes
```

## Règles de qualité

- Exclure BIXI pour les itinéraires hors zone, si aucune station de départ ou d’arrivée n’est disponible, ou lorsque la météo rend le vélo inapproprié.
- Signaler séparément les frais de dépassement, de remorque, de vélo non retourné et les pénalités : ils ne font pas partie du coût normal du trajet.
- Afficher le coût avant taxes et le coût taxes incluses.
- Conserver la date de validation des tarifs dans tout résultat automatisé.
