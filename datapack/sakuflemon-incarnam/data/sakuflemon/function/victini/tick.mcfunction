scoreboard players remove @a[scores={sakuflemon.autel_cd=1..}] sakuflemon.autel_cd 1
execute as @e[type=interaction,tag=sakuflemon.autel] if data entity @s interaction run function sakuflemon:victini/clic
execute at @e[type=interaction,tag=sakuflemon.autel] run particle minecraft:small_flame ~ ~0.8 ~ 0.3 0.2 0.3 0.01 2
