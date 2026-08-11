# Vérification de disponibilité BIXI en temps réel

## Objectif

Vérifier la faisabilité d’une option BIXI après la pré-sélection multimodale, sans interroger le service par défaut. La vérification confirme les stations proches, les vélos disponibles au départ et les bornes libres à l’arrivée. Elle ne garantit pas qu’un vélo ou une borne sera encore disponible au moment de l’utilisateur.

## Source officielle

BIXI publie un flux de données ouvertes au format GBFS :

```text
https://gbfs.velobixi.com/gbfs/2-2/gbfs.json
```

Le document de découverte indique les URL actuelles des flux, notamment :

- `station_information` : identifiant, nom et coordonnées des stations.
- `station_status` : nombre de vélos disponibles, nombre de bornes libres et état opérationnel.

Ne pas coder en dur les URL de ces deux flux : les découvrir à partir de `gbfs.json` pour la langue et la version retenues.

## Déclenchement

La vérification n’est lancée qu’après une demande explicite de l’utilisateur, par exemple :

- « Vérifie BIXI. »
- « Vérifie les stations de départ et d’arrivée. »
- « Vérifie les deux meilleures options. »

Sans demande explicite, présenter BIXI comme une estimation et indiquer que la disponibilité n’est pas confirmée.

## Procédure

1. Charger `station_information` et `station_status` à partir du flux GBFS.
2. Associer les deux jeux de données par `station_id`.
3. Trouver les deux ou trois stations actives les plus proches de l’origine.
4. Retenir une station de départ ayant au moins un vélo disponible et autorisant la location.
5. Trouver les deux ou trois stations actives les plus proches de la destination.
6. Retenir une station d’arrivée ayant au moins une borne libre et autorisant le retour.
7. Si la meilleure station échoue, proposer une station de repli avec sa distance de marche estimée.
8. Afficher l’horodatage du flux et préciser que la disponibilité peut changer avant le départ ou l’arrivée.

## Conditions minimales

| Extrémité | Condition minimale |
|---|---|
| Départ | Station active, location autorisée, au moins un vélo disponible |
| Arrivée | Station active, retour autorisé, au moins une borne libre |

Lorsque le flux distingue les vélos réguliers et électriques, indiquer les deux quantités. Ne pas promettre un type de vélo qui n’est pas explicitement disponible dans le statut.

## Format de réponse

```text
BIXI — disponibilité vérifiée à [heure du flux]

Départ : [station], [distance de marche]
- Vélos disponibles : [nombre]
- Vélos électriques : [nombre ou non précisé]

Arrivée : [station], [distance de marche]
- Bornes libres : [nombre]

Repli : [station de départ ou d’arrivée], [distance de marche]
Niveau de confiance : à confirmer au moment du départ et du retour.
```

## Exemple conversationnel

> Les stations BIXI sont disponibles à vérifier. Voulez-vous que je vérifie maintenant les vélos près du départ et les bornes près de l’arrivée?

Après accord :

> BIXI — disponibilité vérifiée à 17 h 05. La station A, à 2 minutes du départ, a 6 vélos. La station B, à 3 minutes de l’arrivée, a 9 bornes libres. Une station de repli est indiquée pour chaque extrémité. Confirmez dans l’application juste avant le trajet.

## Limites

- Le flux est une photographie à un instant donné; il ne réserve ni vélo ni borne.
- La disponibilité peut changer pendant le trajet.
- Les tarifs, la météo, les travaux, les voies cyclables et la sécurité du parcours doivent être évalués séparément.
- Cette procédure ne doit pas lancer de réservation ou modifier un compte BIXI.
