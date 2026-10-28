# Usage (op) : /function sakuflemon:admin/exclam_retirer : enlève le « ! » le plus proche (8 blocs max) et sa lumière
execute as @e[type=minecraft:block_display,tag=sakuflemon.exclam,distance=..8,sort=nearest,limit=1] at @s run function sakuflemon:admin/exclam_retirer_ici
