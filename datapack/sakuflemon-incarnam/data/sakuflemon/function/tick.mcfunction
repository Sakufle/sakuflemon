# Nouveau joueur sans grade : debutant
team join debutant @a[team=]
# Premiere connexion : direction le hub (Skyloft)
execute as @e[type=player,tag=!sakuflemon.arrive] run function sakuflemon:hub/premiere_connexion
# Reapparition apres une mort sans lit : retour au hub
execute as @e[type=player,scores={sakuflemon.morts=1..}] run function sakuflemon:hub/reapparition
# Incarnam en mode Aventure (sauf tag sakuflemon.builder), Survie ailleurs
execute as @a[gamemode=survival,tag=!sakuflemon.builder] at @s if dimension sakuflemon:grand_incarnam run gamemode adventure @s
execute as @a[gamemode=survival,tag=!sakuflemon.builder] at @s if dimension sakuflemon:petit_incarnam_a run gamemode adventure @s
execute as @a[gamemode=survival,tag=!sakuflemon.builder] at @s if dimension sakuflemon:petit_incarnam_b run gamemode adventure @s
execute as @a[gamemode=survival,tag=!sakuflemon.builder] at @s if dimension sakuflemon:petit_incarnam_c run gamemode adventure @s
execute as @a[gamemode=adventure,tag=!sakuflemon.builder] at @s unless dimension sakuflemon:grand_incarnam unless dimension sakuflemon:petit_incarnam_a unless dimension sakuflemon:petit_incarnam_b unless dimension sakuflemon:petit_incarnam_c run gamemode survival @s
function sakuflemon:musique/tick
function sakuflemon:halo/tick
function sakuflemon:guide/tick
function sakuflemon:menu/tick
