# A lancer une fois (op) : cree la salle cachee du vrai teleporteur dans l'overworld (0 250 0)
execute in minecraft:overworld run forceload add 0 0
execute in minecraft:overworld run fill -3 249 -3 3 254 3 minecraft:barrier hollow
execute in minecraft:overworld run setblock 0 250 0 cobblesafari:safari_teleporter
tellraw @s {"text":"Salle du téléporteur Safari créée en 0 250 0 (overworld). Pose un téléporteur Safari sur Skyloft.","color":"green"}
