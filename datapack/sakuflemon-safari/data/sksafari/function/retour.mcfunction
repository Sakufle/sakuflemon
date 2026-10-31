tag @s remove sksafari.aller
tag @s remove sksafari.dedans
tag @s add sksafari.retour
scoreboard players set @s sksafari.t 0
execute store result storage sksafari:pos x double 0.01 run scoreboard players get @s sksafari.x
execute store result storage sksafari:pos y double 0.01 run scoreboard players get @s sksafari.y
execute store result storage sksafari:pos z double 0.01 run scoreboard players get @s sksafari.z
function sksafari:tp_retour with storage sksafari:pos
