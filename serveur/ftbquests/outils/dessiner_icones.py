#!/usr/bin/env python3
"""Dessine les icônes 32x32 des chapitres (pixel art maison) dans ../icones/.
Elles vont dans le pack de ressources sakuflemon-interface : assets/sakuflemon/textures/quetes/<nom>.png"""
import math, os
from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(__file__), "..", "icones")
N = 32
OUTLINE = (24, 20, 36, 255)

def canvas():
    im = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    return im, ImageDraw.Draw(im)

def outline(im):
    """Ajoute un contour sombre d'un pixel autour de tout ce qui est opaque."""
    px = im.load(); src = im.copy().load()
    for y in range(N):
        for x in range(N):
            if src[x, y][3] == 0 and any(0 <= x+dx < N and 0 <= y+dy < N and src[x+dx, y+dy][3] > 0
                                         for dx, dy in ((1,0),(-1,0),(0,1),(0,-1))):
                px[x, y] = OUTLINE
    return im

def incarnam():
    im, d = canvas()
    d.ellipse((5, 6, 27, 14), fill=(250, 250, 255))                    # nuage / sol herbeux
    d.rectangle((5, 10, 27, 13), fill=(96, 184, 72)); d.rectangle((5, 10, 27, 10), fill=(140, 214, 96))
    d.polygon([(5, 14), (27, 14), (20, 24), (16, 29), (12, 24)], fill=(132, 96, 64))   # roche flottante
    d.polygon([(9, 14), (16, 14), (14, 22)], fill=(156, 118, 80))
    d.rectangle((14, 4, 18, 10), fill=(230, 226, 214)); d.polygon([(13, 4), (16, 0), (19, 4)], fill=(200, 64, 64))  # tour
    d.point((16, 6), fill=(70, 120, 200))
    for x, y in ((24, 26), (8, 25)): d.ellipse((x-2, y-1, x+2, y+1), fill=(240, 244, 255))  # nuages
    return outline(im)

def pokedex():
    im, d = canvas()
    d.rounded_rectangle((6, 3, 25, 28), 3, fill=(214, 44, 52))
    d.rectangle((6, 15, 25, 16), fill=(150, 24, 32))
    d.rectangle((9, 6, 22, 13), fill=(30, 36, 48)); d.rectangle((10, 7, 21, 12), fill=(120, 210, 240))
    d.rectangle((11, 8, 14, 9), fill=(220, 248, 255))
    d.ellipse((9, 19, 14, 24), fill=(70, 150, 230)); d.point((10, 20), fill=(200, 230, 255))
    d.rectangle((17, 20, 22, 21), fill=(250, 210, 60)); d.rectangle((17, 23, 22, 24), fill=(90, 200, 90))
    return outline(im)

TYPES = [(168,168,120),(240,128,48),(104,144,240),(120,200,80),(248,208,48),(152,216,216),
         (192,48,40),(160,64,160),(224,192,104),(168,144,240),(248,88,136),(168,184,32),
         (184,160,56),(112,88,152),(112,56,248),(112,88,72),(184,184,208),(238,153,172)]

def types():
    im, d = canvas()
    c, r = 15.5, 14
    for i, col in enumerate(TYPES):
        a0, a1 = 360 / 18 * i - 90, 360 / 18 * (i + 1) - 90
        d.pieslice((c - r, c - r, c + r, c + r), a0, a1, fill=col + (255,))
    d.ellipse((c - 6, c - 6, c + 6, c + 6), fill=(250, 248, 240))
    d.ellipse((c - 3, c - 3, c + 3, c + 3), fill=(240, 196, 64))
    return outline(im)

def shiny():
    im, d = canvas()
    def star(cx, cy, R, r, col):
        pts = [(cx + (R if k % 2 == 0 else r) * math.cos(math.pi / 4 * k - math.pi / 2),
                cy + (R if k % 2 == 0 else r) * math.sin(math.pi / 4 * k - math.pi / 2)) for k in range(8)]
        d.polygon(pts, fill=col)
    star(14, 16, 12, 3.5, (255, 214, 64)); star(14, 16, 6, 2, (255, 248, 196))
    star(25, 7, 5, 1.5, (130, 220, 255)); star(25, 25, 4, 1.2, (255, 150, 220))
    return outline(im)

def dresseur():
    im, d = canvas()
    d.pieslice((5, 6, 27, 28), 180, 360, fill=(214, 44, 52))          # casquette
    d.rectangle((5, 16, 27, 18), fill=(214, 44, 52))
    d.rectangle((14, 9, 17, 14), fill=(250, 250, 250)); d.rectangle((13, 10, 18, 13), fill=(250, 250, 250))  # logo
    d.rectangle((15, 11, 16, 12), fill=(40, 120, 220))
    d.polygon([(3, 19), (29, 19), (31, 23), (17, 22), (3, 21)], fill=(30, 36, 48))   # visière
    d.rectangle((5, 17, 27, 18), fill=(250, 250, 250))
    return outline(im)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for f in (incarnam, pokedex, types, shiny, dresseur):
        f().save(os.path.join(OUT, f.__name__ + ".png"))
        print(f.__name__)
