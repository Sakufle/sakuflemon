# Datapack Sakuflemon : Incarnam

Ajoute 4 dimensions vides (biome the_void, aucun Pokémon sauvage naturel) :

| Dimension | Rôle | Heure |
|---|---|---|
| `sakuflemon:petit_incarnam_a` | Tutoriel, variante A (Sanctuaire verdoyant) | toujours midi |
| `sakuflemon:petit_incarnam_b` | Tutoriel, variante B (Ruines célestes) | toujours midi |
| `sakuflemon:petit_incarnam_c` | Tutoriel, variante C (Jardin des étoiles) | toujours midi |
| `sakuflemon:grand_incarnam` | Capitale permanente | cycle jour/nuit |

## Installation (serveur)
1. Sauvegarder le monde dans AMP.
2. Copier le dossier `sakuflemon-incarnam` dans `world/datapacks/`.
3. Redémarrer le serveur (les nouvelles dimensions ne se chargent qu'au démarrage).

## Commandes (op)
- `/gamemode creative` puis `/function sakuflemon:aller/grand_incarnam` : aller sur la capitale (place centrale de Skyloft, 0 200 0).
- `/function sakuflemon:admin/plateforme` : pose une dalle 9x9 sous soi pour commencer à construire.
- `/function sakuflemon:aller/monde` : retour au monde principal.

## Hub
- À la première connexion, chaque joueur est envoyé sur la place de Skyloft (tag `sakuflemon.arrive`).
- Après une mort, un joueur sans lit réapparaît au hub ; avec un lit, il réapparaît à son lit.
- Pour renvoyer quelqu'un au hub à la prochaine connexion : `/tag <joueur> remove sakuflemon.arrive`.

## Protection
- Dans les dimensions Incarnam, les joueurs passent automatiquement en mode Aventure (ils ne peuvent rien casser ni poser), et repassent en Survie ailleurs.
- Pour construire : `/tag <joueur> add sakuflemon.builder` (retirer avec `remove`).
