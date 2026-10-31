# 1) Sur Skyloft : monter sur un teleporteur Safari envoie vers le vrai, cache dans l'overworld
execute in sakuflemon:grand_incarnam as @a[distance=0..,tag=!sksafari.retour,tag=!sksafari.aller] at @s if block ~ ~-0.2 ~ cobblesafari:safari_teleporter run function sksafari:aller
execute in sakuflemon:grand_incarnam as @a[distance=0..,tag=!sksafari.retour,tag=!sksafari.aller] at @s if block ~ ~ ~ cobblesafari:safari_teleporter run function sksafari:aller
# Revenu du Safari : on attend qu'il descende du teleporteur pour le reactiver
execute as @a[tag=sksafari.retour] at @s unless block ~ ~-0.2 ~ cobblesafari:safari_teleporter unless block ~ ~ ~ cobblesafari:safari_teleporter run tag @s remove sksafari.retour
# 2) Entre dans le dome
execute in cobblesafari:domedimension as @a[distance=0..,tag=sksafari.aller] run function sksafari:entre
# 3) Pas accepte au bout de 30 s : retour a Skyloft
execute in minecraft:overworld as @a[distance=0..,tag=sksafari.aller] run scoreboard players add @s sksafari.t 1
execute as @a[tag=sksafari.aller,scores={sksafari.t=600..}] run function sksafari:retour
# 4) Sorti du Safari (fin du temps ou /safariexit) : retour a Skyloft
execute in minecraft:overworld as @a[distance=0..,tag=sksafari.dedans] run function sksafari:retour
