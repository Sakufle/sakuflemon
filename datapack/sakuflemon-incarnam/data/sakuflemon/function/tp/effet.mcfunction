$title @s actionbar {"text":"✦ $(nom) ✦","color":"aqua","bold":true}
execute at @s run playsound minecraft:entity.enderman.teleport player @s ~ ~ ~ 1 1.2
execute at @s run particle minecraft:portal ~ ~1 ~ 0.4 0.8 0.4 0.5 60
