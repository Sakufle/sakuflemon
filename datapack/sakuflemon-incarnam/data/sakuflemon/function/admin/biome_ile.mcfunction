# Usage : /function sakuflemon:admin/biome_ile {biome:"minecraft:meadow"}
# Change le biome de Skyloft (collée en 2 84 0 dans grand_incarnam), par quarts de 240 chunks max
gamerule commandModificationBlockLimit 2000000
$execute in sakuflemon:grand_incarnam run function sakuflemon:admin/biome_quart {x1:-256,z1:-208,x2:-1,z2:31,biome:"$(biome)"}
$execute in sakuflemon:grand_incarnam run function sakuflemon:admin/biome_quart {x1:0,z1:-208,x2:239,z2:31,biome:"$(biome)"}
$execute in sakuflemon:grand_incarnam run function sakuflemon:admin/biome_quart {x1:-256,z1:32,x2:-1,z2:271,biome:"$(biome)"}
$execute in sakuflemon:grand_incarnam run function sakuflemon:admin/biome_quart {x1:0,z1:32,x2:239,z2:271,biome:"$(biome)"}
gamerule commandModificationBlockLimit 32768
tellraw @s {"text":"Biome de l'île changé. Reconnecte-toi pour le voir.","color":"green"}
