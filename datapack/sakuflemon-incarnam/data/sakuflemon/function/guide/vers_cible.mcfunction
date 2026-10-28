# Exécuté par le joueur (étape 7+) : flèche vers le marqueur posé avec admin/cible pour son étape
tag @s add sakuflemon.moi
scoreboard players operation #cherche sakuflemon.guide = @s sakuflemon.guide
execute as @e[type=minecraft:marker,tag=sakuflemon.cible] if score @s sakuflemon.guide = #cherche sakuflemon.guide at @s if entity @a[tag=sakuflemon.moi,distance=6..] at @a[tag=sakuflemon.moi,limit=1] facing entity @s feet rotated ~ 0 positioned ~ ~0.15 ~ run function sakuflemon:guide/dessiner_moi
tag @s remove sakuflemon.moi
