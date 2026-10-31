execute store result score @s sksafari.x run data get entity @s Pos[0] 100
execute store result score @s sksafari.y run data get entity @s Pos[1] 100
execute store result score @s sksafari.z run data get entity @s Pos[2] 100
scoreboard players set @s sksafari.t 0
tag @s add sksafari.aller
execute in minecraft:overworld run tp @s 0.5 251 0.5
tellraw @s {"text":"Accepte la demande du téléporteur pour entrer dans la Zone Safari.","color":"gold"}
