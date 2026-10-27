scoreboard players set #horloge sakuflemon.guide 0
execute as @a[scores={sakuflemon.guide=1}] at @s if dimension sakuflemon:grand_incarnam positioned 26.5 101 -153.5 unless entity @s[distance=..6] run function sakuflemon:guide/fleche {x:26.5,y:101,z:-153.5}
execute as @a[scores={sakuflemon.guide=2}] at @s if dimension sakuflemon:grand_incarnam positioned 26.6 101 -111.4 unless entity @s[distance=..5] run function sakuflemon:guide/fleche {x:26.6,y:101,z:-111.4}
execute as @a[scores={sakuflemon.guide=3}] at @s if dimension sakuflemon:grand_incarnam positioned 17.6 74 80.3 unless entity @s[distance=..5] run function sakuflemon:guide/fleche {x:17.6,y:74,z:80.3}
# Gardes : d'abord le Garde du vent, puis le Garde de la nuée
execute as @a[scores={sakuflemon.guide=4..5},advancements={sakuflemon:sakuflemon_garde_vent=false}] at @s if dimension sakuflemon:grand_incarnam positioned 8 84 32.3 unless entity @s[distance=..5] run function sakuflemon:guide/fleche {x:8,y:84,z:32.3}
execute as @a[scores={sakuflemon.guide=4..5},advancements={sakuflemon:sakuflemon_garde_vent=true}] at @s if dimension sakuflemon:grand_incarnam positioned 72.3 74 -44.4 unless entity @s[distance=..5] run function sakuflemon:guide/fleche {x:72.3,y:74,z:-44.4}
execute as @a[scores={sakuflemon.guide=6}] at @s if dimension sakuflemon:grand_incarnam positioned 187 64 252 unless entity @s[distance=..6] run function sakuflemon:guide/fleche {x:187,y:64,z:252}
