# Toutes les secondes : on eteint les portails pres des joueurs de l'overworld et on retient leur position
scoreboard players add #t sakuflemon.portail_t 1
execute if score #t sakuflemon.portail_t matches 20.. run function sakuflemon_portails:seconde
