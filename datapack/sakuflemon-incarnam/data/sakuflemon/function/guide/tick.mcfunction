# Guide du tutoriel : flèche de particules au sol vers le PNJ de la quête en cours.
# sakuflemon.guide : 1 Arceus, 2 Professeur, 3 Apprenti, 4 Gardes du ciel, 6 Arène Céleste, 0 rien.
# Les quêtes FTB changent ce score (récompenses invisibles), les gardes et l'arène via leurs advancements.
execute as @a[scores={sakuflemon.guide=4..5},advancements={sakuflemon:sakuflemon_garde_vent=true,sakuflemon:sakuflemon_garde_nuee=true}] run scoreboard players set @s sakuflemon.guide 6
execute as @a[scores={sakuflemon.guide=6},advancements={sakuflemon:arene_celeste=true}] run scoreboard players set @s sakuflemon.guide 0
# Toutes les 10 ticks seulement
scoreboard players add #horloge sakuflemon.guide 1
execute if score #horloge sakuflemon.guide matches 10.. run function sakuflemon:guide/afficher
# Les « ! » tournent : un tiers de tour toutes les 2 s, lissé par teleport_duration
scoreboard players add #rotation sakuflemon.guide 1
execute if score #rotation sakuflemon.guide matches 40.. run function sakuflemon:guide/tourner
