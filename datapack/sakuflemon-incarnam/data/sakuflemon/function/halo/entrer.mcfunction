# Debloque par une quete (tag sakuflemon.plongeon)
execute unless entity @s[tag=sakuflemon.plongeon] run function sakuflemon:halo/refus
execute if entity @s[tag=sakuflemon.plongeon] run function sakuflemon:halo/plonger
