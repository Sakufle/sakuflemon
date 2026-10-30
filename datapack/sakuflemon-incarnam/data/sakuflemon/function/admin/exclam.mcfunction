# Usage (op, à côté du PNJ) : /function sakuflemon:admin/exclam {hauteur:2.6}
# Pose un « ! » 3D doré au-dessus de l'entité la plus proche (6 blocs max). hauteur = blocs au-dessus de ses pieds
# (2.6 pour un humain, plus pour un gros Pokémon).
$execute as @e[type=!minecraft:player,type=!minecraft:marker,type=!minecraft:block_display,type=!minecraft:text_display,type=!minecraft:item,distance=..6,sort=nearest,limit=1] at @s positioned ~ ~$(hauteur) ~ run function sakuflemon:admin/exclam_bloc
