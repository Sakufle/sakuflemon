# Usage (op, à côté du PNJ) : /function sakuflemon:admin/cible {etape:7}
# L'entité la plus proche devient la cible de la flèche pour l'étape donnée (7 Pêcheur, 8 Marchand, 9+ libres).
# Relancer pour la même étape remplace l'ancienne cible. Le chunk reste chargé pour que la flèche marche de loin.
$kill @e[type=minecraft:marker,tag=sakuflemon.cible,scores={sakuflemon.guide=$(etape)}]
execute as @e[type=!minecraft:player,type=!minecraft:marker,type=!minecraft:block_display,type=!minecraft:text_display,type=!minecraft:item,distance=..6,sort=nearest,limit=1] at @s run summon minecraft:marker ~ ~ ~ {Tags:["sakuflemon.cible","sakuflemon.cible_neuve"]}
execute as @e[type=minecraft:marker,tag=sakuflemon.cible_neuve] at @s run forceload add ~ ~
$scoreboard players set @e[type=minecraft:marker,tag=sakuflemon.cible_neuve] sakuflemon.guide $(etape)
$execute if entity @e[type=minecraft:marker,tag=sakuflemon.cible_neuve] run tellraw @s {"text":"Cible de la flèche posée pour l'étape $(etape).","color":"gold"}
execute unless entity @e[type=minecraft:marker,tag=sakuflemon.cible_neuve] run tellraw @s {"text":"Aucun PNJ à moins de 6 blocs.","color":"red"}
tag @e[type=minecraft:marker,tag=sakuflemon.cible_neuve] remove sakuflemon.cible_neuve
