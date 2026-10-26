# Usage : /function sakuflemon:admin/biome_ile {biome:"minecraft:meadow"}
# Change le biome de Skyloft (collée en 2 84 0 dans grand_incarnam). Applique 5 s plus tard, le temps de charger les chunks.
$data modify storage sakuflemon:admin biome set value "$(biome)"
execute in sakuflemon:grand_incarnam run forceload add -256 -208 -1 31
execute in sakuflemon:grand_incarnam run forceload add 0 -208 239 31
execute in sakuflemon:grand_incarnam run forceload add -256 32 -1 271
execute in sakuflemon:grand_incarnam run forceload add 0 32 239 271
gamerule commandModificationBlockLimit 60000000
tellraw @a {"text":"Chargement de l'île, biome appliqué dans 5 secondes...","color":"yellow"}
schedule function sakuflemon:admin/biome_appliquer 100t
