# Musique de l'ile (Grand Incarnam) : coupe la musique Minecraft et joue la notre en boucle
execute as @a at @s if dimension sakuflemon:grand_incarnam run function sakuflemon:musique/sur_ile
execute as @a[scores={sakuflemon.musique=1..}] at @s unless dimension sakuflemon:grand_incarnam run function sakuflemon:musique/quitter
