# Joueur qui a cliqué sur l'autel
execute if entity @s[tag=sakuflemon.victini] run return run tellraw @s [{"text":"La flamme brûle déjà pour toi. Victini t'a choisi.","color":"gold","italic":true}]
execute unless entity @s[tag=sakuflemon.flamme] run return run tellraw @s [{"text":"L'autel reste froid... Bats 10 dresseurs différents pour prouver ta valeur.","color":"gray","italic":true}]
execute if score @s sakuflemon.autel_cd matches 1.. run return run tellraw @s [{"text":"Les braises sont encore chaudes. Reviens dans une minute.","color":"gray","italic":true}]
scoreboard players set @s sakuflemon.autel_cd 1200
execute at @e[type=interaction,tag=sakuflemon.autel,sort=nearest,limit=1] run function sakuflemon:victini/apparition
tellraw @s [{"text":"La flamme de la Victoire se rallume ! ","color":"gold","bold":true},{"text":"Victini apparaît : capture-le !","color":"yellow","bold":false}]
