function sakuflemon:admin/biome_macro with storage sakuflemon:admin
execute in sakuflemon:grand_incarnam run forceload remove all
gamerule commandModificationBlockLimit 32768
tellraw @a {"text":"Biome de l'île changé. Reconnectez-vous pour le voir.","color":"green"}
