# Pose l'Autel de la Victoire là où tu te tiens (construis le décor autour, ex. un feu de camp au centre)
kill @e[type=interaction,tag=sakuflemon.autel]
kill @e[type=text_display,tag=sakuflemon.autel]
summon interaction ~ ~ ~ {Tags:["sakuflemon.autel"],width:1.5f,height:1.5f,response:1b}
summon text_display ~ ~2 ~ {Tags:["sakuflemon.autel"],billboard:"center",text:'{"text":"Autel de la Victoire","color":"gold","bold":true}'}
forceload add ~ ~
tellraw @s {"text":"Autel de la Victoire posé ici.","color":"green"}
