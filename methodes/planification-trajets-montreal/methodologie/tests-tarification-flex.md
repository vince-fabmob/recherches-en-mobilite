# Cas de test — Tarification Communauto

## Objectif

Ces cas de test vérifient que l’estimation dépend du forfait utilisateur et qu’elle ne suppose pas un prix FLEX fixe.

| Cas | Données connues | Résultat attendu |
|---|---|---|
| Forfait inconnu | Origine, destination et durée connus; forfait absent | L’IA demande le forfait avant de fournir un coût ferme. |
| Laissez-passer actif | Forfait et laissez-passer confirmés; durée et conditions respectées | L’IA applique le tarif du laissez-passer configuré. |
| Seuil dépassé | Laissez-passer actif; durée estimée supérieure au seuil | L’IA applique le tarif de repli et explique le dépassement. |
| Destination dans la zone | Destination dans une zone FLEX; stationnement non confirmé | L’IA indique que la fermeture doit être confirmée dans l’application. |
| Destination hors zone | Fin de trajet hors zone | L’IA ne recommande pas de terminer le trajet et propose une alternative. |
| Conflit de documents | Prompt et fichier tarifaire donnent des valeurs différentes | Le fichier `donnees/tarifs-communauto.json` prévaut. |

## Cas conversationnel

**Question** : « Combien coûte une FLEX pour aller à Montréal-Nord? »

**Réponse attendue si le forfait est inconnu** :

> « Quel forfait Communauto avez-vous actuellement? Si vous avez un laissez-passer FLEX actif, son prix et ses conditions peuvent modifier l’estimation. »
