execute store result score @s sakuflemon.px run data get entity @s Pos[0]
execute store result score @s sakuflemon.py run data get entity @s Pos[1]
execute store result score @s sakuflemon.pz run data get entity @s Pos[2]
execute store success score #eteint sakuflemon.portail_t run fill ~-6 ~-6 ~-6 ~6 ~6 ~6 air replace minecraft:nether_portal
execute store success score #eteint_end sakuflemon.portail_t run fill ~-6 ~-3 ~-6 ~6 ~3 ~6 air replace minecraft:end_portal
execute if score #eteint sakuflemon.portail_t matches 1.. run function sakuflemon_portails:message
execute if score #eteint_end sakuflemon.portail_t matches 1.. run function sakuflemon_portails:message
