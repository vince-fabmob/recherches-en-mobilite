# Estimation des coûts de taxi à Montréal

## Objet

Cette méthode estime le prix d’une course en taxi à compteur dans l’agglomération de Montréal. Le prix final est celui affiché au compteur, auquel peuvent s’ajouter des frais clairement identifiés.

## Données requises

- Origine, destination, heure de prise en charge, kilomètres routiers `d` et temps prévu à faible vitesse ou à l’arrêt `w`.
- Période tarifaire : jour (5 h à 23 h) ou nuit (23 h à 5 h).
- Frais connus : péage, supplément aéroport le cas échéant, réservation ou autre frais autorisé.
- Pourboire souhaité, toujours facultatif et séparé.

## Paramètres de référence

Les tarifs officiels publiés pour 2026 sont les suivants :

| Période | Prise en charge `B` | Distance `r_d` | Attente/lenteur `r_w` |
|---|---:|---:|---:|
| Jour, 5 h–23 h | 4,10 $ | 2,05 $/km | 46,20 $/h |
| Nuit, 23 h–5 h | 4,70 $ | 2,35 $/km | 53,40 $/h |

Source : https://mtl.taxi/en/fares

## Formule

```text
C_compteur = B + d × r_d + w × r_w
C_obligatoire = C_compteur + frais_reglementes
C_avec_pourboire = C_obligatoire × (1 + taux_pourboire)
```

`w` doit être exprimé en heures. Si le trajet est fluide, poser `w = 0`; si le trafic est incertain, calculer une fourchette basse, centrale et haute. Ne pas appliquer simultanément un temps de parcours complet et le tarif d’attente : seuls les ralentissements et immobilisations sont visés.

## Exemple

Course de jour de 6 km avec 8 minutes de ralentissement :

```text
C_compteur = 4,10 + (6 × 2,05) + ((8/60) × 46,20)
           = 22,56 $
```

Avec un pourboire facultatif de 15 % :

```text
C_avec_pourboire = 22,56 × 1,15 = 25,94 $
```

## Règles de qualité

- Utiliser l’itinéraire routier réel; ne pas employer la distance à vol d’oiseau.
- Indiquer explicitement le régime de jour ou de nuit.
- Présenter le pourboire à part du coût obligatoire.
- Vérifier les suppléments applicables auprès du fournisseur ou de l’autorité compétente avant de les inclure.
- Horodater les paramètres tarifaires et les revoir à chaque mise à jour réglementaire.
