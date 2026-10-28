stopsound @s music
# Zone voulue : 1 = Skyloft, 2 = île Citrouille (158 164 -> 255 252)
scoreboard players set @s sakuflemon.zone_v 1
execute if entity @s[x=158,y=40,z=164,dx=97,dy=100,dz=88] run scoreboard players set @s sakuflemon.zone_v 2
execute unless score @s sakuflemon.zone_v = @s sakuflemon.zone run function sakuflemon:musique/changer
scoreboard players remove @s[scores={sakuflemon.musique=1..}] sakuflemon.musique 1
execute unless score @s sakuflemon.musique matches 1.. run function sakuflemon:musique/jouer
