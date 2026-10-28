# skyloft.ogg dure 191 s = 3820 ticks, citrouille.ogg 192 s = 3843 ticks
execute if score @s sakuflemon.zone matches 1 run playsound sakuflemon:musique.skyloft record @s ~ ~ ~ 1 1 1
execute if score @s sakuflemon.zone matches 1 run scoreboard players set @s sakuflemon.musique 3820
execute if score @s sakuflemon.zone matches 2 run playsound sakuflemon:musique.citrouille record @s ~ ~ ~ 1 1 1
execute if score @s sakuflemon.zone matches 2 run scoreboard players set @s sakuflemon.musique 3843
