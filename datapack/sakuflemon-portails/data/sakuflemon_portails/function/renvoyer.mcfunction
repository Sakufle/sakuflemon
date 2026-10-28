advancement revoke @s only sakuflemon_portails:bloque_the_nether
advancement revoke @s only sakuflemon_portails:bloque_the_end
execute store result storage sakuflemon:portails x int 1 run scoreboard players get @s sakuflemon.px
execute store result storage sakuflemon:portails y int 1 run scoreboard players get @s sakuflemon.py
execute store result storage sakuflemon:portails z int 1 run scoreboard players get @s sakuflemon.pz
execute unless score @s sakuflemon.px = @s sakuflemon.px run return run function sakuflemon:aller/grand_incarnam
function sakuflemon_portails:renvoyer_pos with storage sakuflemon:portails
function sakuflemon_portails:message
