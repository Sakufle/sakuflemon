tag @s add sakuflemon.chute
effect give @s minecraft:resistance 20 4 true
# Monture : on emmene le Pokemon avec le joueur puis on le remet en selle au tick suivant
execute on vehicle run tag @s add sakuflemon.monture
execute if entity @e[tag=sakuflemon.monture] run tag @s add sakuflemon.remonter
ride @s dismount
execute in minecraft:overworld run tp @e[tag=sakuflemon.monture] 1000 320 1000
execute in minecraft:overworld run tp @s 1000 320 1000
playsound minecraft:item.elytra.flying player @s ~ ~ ~ 1 1.2
title @s title {"text":"Plongeon !","color":"aqua","bold":true}
title @s subtitle {"text":"Sors ton Pokémon volant !","color":"white"}
