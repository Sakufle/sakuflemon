stopsound @s music
scoreboard players remove @s[scores={sakuflemon.musique=1..}] sakuflemon.musique 1
execute unless score @s sakuflemon.musique matches 1.. run function sakuflemon:musique/jouer
