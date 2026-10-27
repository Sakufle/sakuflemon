tag @s add sakuflemon.chute
effect give @s minecraft:resistance 20 4 true
# Cobblemon range le Pokemon au changement de dimension : 8 s de chute lente pour le ressortir
effect give @s minecraft:slow_falling 8 0 true
execute in minecraft:overworld run tp @s 1000 320 1000
playsound minecraft:item.elytra.flying player @s ~ ~ ~ 1 1.2
title @s title {"text":"Plongeon !","color":"aqua","bold":true}
title @s subtitle {"text":"Sors ton Pokémon volant !","color":"white"}
