# Estimation des coûts de VTC à Montréal

## Objet

Cette méthode estime le coût d’une course en véhicule de transport avec chauffeur (VTC), notamment Uber et Lyft. À la différence du taxi à compteur, le meilleur prix de référence est l’estimation affichée par la plateforme immédiatement avant la réservation.

## Principe

La tarification VTC est dynamique. Elle varie notamment selon la demande, l’offre de chauffeurs, le lieu, l’heure, le type de véhicule et les frais appliqués par la plateforme. Une formule fixe distance-temps ne doit donc être utilisée que comme estimation de secours, jamais comme prix ferme.

Uber indique que l’estimé obtenu en entrant le lieu de prise en charge et la destination tient compte de la tarification dynamique lorsqu’elle s’applique.

Source : https://www.uber.com/ca/fr-ca/newsroom/introduction-de-la-tarification-dynamique-pour-uberx/

## Données requises

- Adresse ou point de prise en charge, destination, date et heure.
- Catégorie demandée : par exemple UberX, UberXL, véhicule adapté ou option équivalente.
- Prix affiché `P_affiche` et intervalle de prix, s’il est fourni.
- Frais de réservation, péages, frais d’annulation possibles et pourboire souhaité.

## Hiérarchie des estimations

1. **Prix affiché dans l’application** : source primaire; conserver une capture ou l’horodatage.
2. **Fourchette affichée** : publier les bornes basse et haute, sans les transformer en prix garanti.
3. **Historique comparable** : seulement si aucun prix temps réel n’est disponible; indiquer clairement la date, le créneau horaire, la catégorie et l’incertitude.

## Formules

### Prix temps réel disponible

```text
C_obligatoire = P_affiche + peages_inclus_non_inclus + autres_frais_confirmes
C_avec_pourboire = C_obligatoire × (1 + taux_pourboire)
```

Ne pas ajouter de coefficient de majoration au `P_affiche` : celui-ci est présumé déjà intégré.

### Aucun prix temps réel

```text
C_bas, C_central, C_haut = statistiques des courses comparables
```

Une course comparable doit partager la même plateforme, catégorie, zone origine-destination, plage horaire et période de l’année. L’échantillon et la date de collecte doivent être affichés.

## Exemple

L’application affiche 18–24 $ pour une catégorie standard. Le résultat doit être présenté ainsi :

```text
Coût obligatoire estimé : 18–24 $
Coût avec pourboire facultatif de 15 % : 20,70–27,60 $

Prix à confirmer immédiatement avant la demande : la majoration dynamique peut évoluer.
```

## Règles de qualité

- Comparer la même catégorie de véhicule entre plateformes.
- Ne pas présenter un prix historique comme un prix actuel ou garanti.
- Séparer les frais obligatoires, les péages et le pourboire.
- Signaler les conditions qui rendent l’estimation volatile : pointe, météo défavorable, grands événements, fin de service du métro et faible disponibilité.
- Ne pas lancer de réservation sans confirmation explicite de l’utilisateur.
