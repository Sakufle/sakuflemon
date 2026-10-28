# Objet « Menu Sakuflemon » (carotte sur un baton) : clic droit = /menu
execute as @a[scores={sakuflemon.menu=1..}] run function sakuflemon:menu/clic
# Chaque joueur le recoit une fois
execute as @a[tag=!sakuflemon.menu_recu] run function sakuflemon:menu/donner
scoreboard players remove @a[scores={sakuflemon.tp_cd=1..}] sakuflemon.tp_cd 1
