# sakuflemon-loot

Ajoute du loot Pokémon (Cobblemon 1.8.3) dans les coffres des structures, en plus du loot vanilla.

- `sakuflemon:coffres/commun` : Poké Balls, Potions, soins, baies, Noigrumes, petits bonbons Exp.
- `sakuflemon:coffres/rare` : Super/Hyper Balls, Balls spéciales, pierres d'évolution, vitamines, aromates, objets tenus, fossiles, Super Bonbons.
- `sakuflemon:coffres/legendaire` : Max Potions, Rappels Max, objets Choix, Orbe Vie, Pièce Relique, rouleaux de Kubfu, Capsule/Patch Talent, Master Ball (très rare).

Répartition : villages, mines, donjons, portails en ruine, épaves (provisions) = commun ;
temples, trésors, avant-postes, manoirs, forteresses du Nether, bastions = rare ;
cités antiques, trésor des bastions, cités de l'End = légendaire.
Les coffres des mods de structures seront branchés sur ces tables après leur installation.

Loot unique par joueur et réapparition toutes les 3 h : mod **Lootr** (client + serveur), config
`config/lootr-common.toml` (nom à confirmer sur le serveur) :

```toml
randomise_seed = true
refresh_dimensions = ["minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"]
refresh_value = 216000   # 3 h en ticks
```

Régénérer : `python3 serveur/loot/generer.py <tables vanilla 1.21.1 chests/> <ids Cobblemon> datapack/sakuflemon-loot`
