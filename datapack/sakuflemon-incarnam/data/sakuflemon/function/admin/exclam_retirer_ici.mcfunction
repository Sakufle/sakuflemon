kill @e[type=minecraft:block_display,tag=sakuflemon.exclam,distance=..0.5]
execute positioned ~ ~-0.5 ~ if block ~ ~ ~ minecraft:light run setblock ~ ~ ~ minecraft:air
tellraw @a[distance=..10] {"text":"« ! » retiré.","color":"gold"}
