# Premiere connexion : direction le hub (Skyloft)
execute as @e[type=player,tag=!sakuflemon.arrive] run function sakuflemon:hub/premiere_connexion
# Reapparition apres une mort sans lit : retour au hub
execute as @e[type=player,scores={sakuflemon.morts=1..}] run function sakuflemon:hub/reapparition
