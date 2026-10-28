# sakuflemon-loot

Ajoute du loot Pokémon (Cobblemon 1.8.3) dans les coffres des structures, en plus de leur loot d'origine.

- `sakuflemon:coffres/commun` : Poké Balls, Potions, soins, baies, Noigrumes, petits Bonbons Exp.
- `sakuflemon:coffres/rare` : Super/Hyper Balls, Balls spéciales, pierres d'évolution, vitamines, aromates, objets tenus, fossiles, Super Bonbons.
- `sakuflemon:coffres/legendaire` : Max Potions, Rappels Max, objets Choix, Orbe Vie, Pièce Relique, rouleaux de Wushours, Capsule/Patch Talent, Master Ball (très rare).

Coffres branchés (liste complète et niveau de chacun : `../sakuflemon-loot-tables.txt`) :
vanilla 1.21.1, YUNG's (Dungeons, Strongholds, Desert/Jungle Temples, Witch Huts, Ocean Monuments, Nether Fortresses, Extras),
CTOV 3.6.3, Towns and Towers 1.13.11, Dungeons and Taverns 4.4.4, Incendium 5.4.4.
Les coffres de Cobblemon Cities & Structures et de Cobblemon Opponents ont déjà du loot Pokémon : non modifiés.
Mineshafts, End Island, Bridges, Nullscape et CobbleStructures n'ont pas de table de coffre propre.

Ces fichiers remplacent les tables des mods : à régénérer si un mod de structures est mis à jour.

Loot unique par joueur et réapparition toutes les 3 h : mod **Lootr** 1.21.1-1.11.38.127 (client + serveur),
config `config/lootr-common.toml` (nom à confirmer sur le serveur) :

```toml
randomise_seed = true
refresh_dimensions = ["minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"]
refresh_value = 216000   # 3 h en ticks
```

Régénérer : `python3 serveur/loot/generer.py <tables vanilla chests/> <ids Cobblemon> datapack/sakuflemon-loot <jars dézippés>`
