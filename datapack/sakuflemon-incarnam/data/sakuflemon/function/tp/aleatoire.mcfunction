# Menu /tp : endroit au hasard dans l'overworld (halo debloque, 30 s entre deux)
execute unless entity @s[tag=sakuflemon.plongeon] run return run function sakuflemon:tp/verrouille
execute if score @s sakuflemon.tp_cd matches 1.. run return run title @s actionbar {"text":"Attends un peu avant de repartir à l'aventure...","color":"red"}
scoreboard players set @s sakuflemon.tp_cd 600
effect give @s minecraft:resistance 10 4 true
execute in minecraft:overworld run spreadplayers 0 0 500 4000 false @s
function sakuflemon:tp/effet {nom:"Exploration"}
