# Halos de Skyloft : plonger vers la terre ferme
# Ajouter un halo = une ligne particules + une ligne zone (et un fichier particules_N)
scoreboard players add #horloge sakuflemon.halo 1
execute if score #horloge sakuflemon.halo matches 4.. in sakuflemon:grand_incarnam run function sakuflemon:halo/particules_1
execute if score #horloge sakuflemon.halo matches 4.. run scoreboard players set #horloge sakuflemon.halo 0
# Zone du halo 1
execute in sakuflemon:grand_incarnam as @a[x=13,y=31,z=188,dx=4,dy=4,dz=4] run function sakuflemon:halo/entrer
# Chute hors d'un halo : retour sur la place
execute in sakuflemon:grand_incarnam as @a[x=-1000,y=-200,z=-1000,dx=2000,dy=180,dz=2000] run function sakuflemon:aller/grand_incarnam
# Ralentir la chute pres du sol apres un plongeon
execute as @a[tag=sakuflemon.chute] at @s if dimension minecraft:overworld unless block ~ ~-12 ~ air run function sakuflemon:halo/atterrir
execute as @a[tag=sakuflemon.chute] at @s if dimension minecraft:overworld unless block ~ ~-24 ~ air run function sakuflemon:halo/atterrir
