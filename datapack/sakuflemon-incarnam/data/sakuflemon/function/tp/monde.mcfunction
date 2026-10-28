# Menu /tp : plongeon vers l'overworld, seulement si le halo est debloque (meme regle que le halo)
execute unless entity @s[tag=sakuflemon.plongeon] run return run function sakuflemon:tp/verrouille
function sakuflemon:halo/plonger
