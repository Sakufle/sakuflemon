"""Icone 16x16 de l'objet « Menu Sakuflemon » (carrot_on_a_stick, custom_model_data 7010)."""
import sys
from PIL import Image
G = [
    "................",
    ".....######.....",
    "...##RRRRRR##...",
    "..#RRRRRRRRRR#..",
    "..#RRRYYRRRRR#..",
    ".#RRRYYYYRRRRR#.",
    ".#RRRRYYRRRRRR#.",
    ".######WW######.",
    ".#####W..W#####.",
    ".#WWWWW..WWWWW#.",
    ".#WWWWWWWWWWWW#.",
    "..#WWWWWWWWWW#..",
    "..#WWWWWWWWWW#..",
    "...##WWWWWW##...",
    ".....######.....",
    "................",
]
C = {"#": (30, 30, 35, 255), "R": (210, 45, 45, 255), "W": (240, 240, 245, 255),
     "Y": (255, 215, 80, 255), ".": (0, 0, 0, 0)}
im = Image.new("RGBA", (16, 16))
for y, l in enumerate(G):
    for x, c in enumerate(l):
        im.putpixel((x, y), C[c])
im.save(sys.argv[1])
