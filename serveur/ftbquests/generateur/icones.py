# -*- coding: utf-8 -*-
"""Dessine les 12 icônes de chapitre (32x32, pixel art, contour sombre comme les 5 existantes).
Usage : python icones.py <dossier sortie>"""
import math, os, sys
from PIL import Image, ImageDraw

OUT = sys.argv[1] if len(sys.argv) > 1 else "icones"
os.makedirs(OUT, exist_ok=True)
OUTLINE = (40, 28, 40, 255)

def new():
    im = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    return im, ImageDraw.Draw(im)

def outline(im):
    px = im.load(); w, h = im.size
    solid = {(x, y) for x in range(w) for y in range(h) if px[x, y][3] > 0}
    for x, y in [(x, y) for x in range(w) for y in range(h)]:
        if (x, y) in solid: continue
        if any((x + dx, y + dy) in solid for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
            px[x, y] = OUTLINE
    return im

def shade_circle(d, cx, cy, r, base, light, dark):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=base)
    d.ellipse([cx - r + 1, cy - r + 1, cx + r - 3, cy + r - 3], fill=base)
    d.pieslice([cx - r, cy - r, cx + r, cy + r], 30, 150, fill=dark)
    d.ellipse([cx - r + 3, cy - r + 3, cx - r + 7, cy - r + 7], fill=light)

def save(im, name):
    outline(im).save(os.path.join(OUT, name + ".png"))

# Méga : Pierre Clé (sphère à double hélice)
im, d = new()
shade_circle(d, 15, 15, 12, (235, 225, 240, 255), (255, 255, 255, 255), (190, 175, 205, 255))
for t in range(0, 360, 3):
    a = math.radians(t)
    x = 15 + 9 * math.sin(a * 1.0); y = 15 + 10 * math.cos(a)
    x2 = 15 - 9 * math.sin(a * 1.0)
    d.point((round(x), round(y)), fill=(245, 120, 40, 255))
    d.point((round(x2), round(y)), fill=(60, 140, 230, 255))
for k in range(-2, 3):
    d.line([(15 - 4 + k, 13 + k), (15 + 4 + k, 17 + k)], fill=(250, 200, 60, 255))
save(im, "mega")

# Raids : colonne de lumière sur une tanière
im, d = new()
d.rectangle([12, 1, 19, 22], fill=(200, 80, 220, 255)); d.rectangle([14, 1, 17, 22], fill=(250, 190, 255, 255))
d.ellipse([3, 19, 28, 30], fill=(110, 95, 85, 255)); d.ellipse([7, 21, 24, 27], fill=(60, 45, 60, 255))
d.ellipse([10, 22, 21, 26], fill=(220, 120, 240, 255))
for (x, y) in [(6, 6), (25, 9), (8, 14), (24, 16)]:
    d.point((x, y), fill=(255, 230, 255, 255)); d.point((x + 1, y), fill=(255, 230, 255, 255))
save(im, "raids")

# Éleveur : œuf
im, d = new()
d.ellipse([7, 3, 24, 29], fill=(250, 244, 220, 255)); d.ellipse([16, 5, 24, 28], fill=(232, 222, 190, 255)); d.ellipse([8, 4, 22, 27], fill=(250, 244, 220, 255))
for (x, y, r) in [(12, 10, 3), (19, 17, 3), (11, 21, 2), (18, 8, 2)]:
    d.ellipse([x - r, y - r, x + r, y + r], fill=(110, 190, 90, 255))
d.rectangle([10, 6, 11, 8], fill=(255, 255, 255, 255))
save(im, "eleveur")

# Safari : Safari Ball
im, d = new()
d.ellipse([3, 3, 28, 28], fill=(240, 240, 230, 255))
d.pieslice([3, 3, 28, 28], 180, 360, fill=(120, 160, 60, 255))
for (x, y) in [(8, 9), (14, 6), (20, 9), (11, 13), (23, 13), (17, 12)]:
    d.ellipse([x - 2, y - 1, x + 2, y + 1], fill=(70, 110, 40, 255))
d.rectangle([3, 15, 28, 16], fill=OUTLINE)
d.ellipse([12, 12, 19, 19], fill=OUTLINE); d.ellipse([13, 13, 18, 18], fill=(250, 250, 250, 255))
d.rectangle([7, 6, 8, 7], fill=(200, 230, 140, 255))
save(im, "safari")

# Montures : selle
im, d = new()
d.polygon([(4, 14), (10, 9), (22, 9), (28, 14), (26, 20), (6, 20)], fill=(150, 85, 45, 255))
d.polygon([(7, 13), (11, 10), (21, 10), (25, 13)], fill=(185, 115, 65, 255))
d.rectangle([4, 20, 27, 22], fill=(110, 60, 30, 255))
d.rectangle([14, 22, 17, 27], fill=(110, 60, 30, 255)); d.rectangle([12, 27, 19, 29], fill=(200, 200, 210, 255))
d.ellipse([20, 6, 24, 10], fill=(185, 115, 65, 255))
save(im, "montures")

# Explorateur : boussole
im, d = new()
d.ellipse([3, 3, 28, 28], fill=(200, 150, 60, 255)); d.ellipse([6, 6, 25, 25], fill=(245, 235, 210, 255))
d.polygon([(15, 7), (18, 15), (13, 15)], fill=(220, 50, 50, 255)); d.polygon([(15, 24), (18, 16), (13, 16)], fill=(90, 90, 110, 255))
d.rectangle([15, 15, 16, 16], fill=(250, 220, 90, 255))
d.rectangle([14, 0, 17, 3], fill=(200, 150, 60, 255))
save(im, "explorateur")

# Arènes : badge (octogone gris) avec étoile
im, d = new()
d.regular_polygon((15.5, 15.5, 13), 8, rotation=22.5, fill=(170, 175, 190, 255))
d.regular_polygon((15.5, 15.5, 9), 8, rotation=22.5, fill=(205, 210, 220, 255))
d.regular_polygon((15.5, 15.5, 5), 4, rotation=45, fill=(240, 200, 60, 255))
d.rectangle([8, 7, 10, 8], fill=(255, 255, 255, 255))
save(im, "arenes")

# Légendes : Master Ball
im, d = new()
d.ellipse([3, 3, 28, 28], fill=(240, 240, 245, 255)); d.pieslice([3, 3, 28, 28], 180, 360, fill=(120, 60, 170, 255))
d.ellipse([5, 6, 10, 11], fill=(235, 90, 160, 255)); d.ellipse([21, 6, 26, 11], fill=(235, 90, 160, 255))
d.text((12, 4), "M", fill=(255, 255, 255, 255))
d.rectangle([3, 15, 28, 16], fill=OUTLINE)
d.ellipse([12, 12, 19, 19], fill=OUTLINE); d.ellipse([13, 13, 18, 18], fill=(250, 250, 250, 255))
save(im, "legendes")

# Artisan : Noigrume rouge
im, d = new()
d.ellipse([5, 8, 27, 29], fill=(215, 50, 50, 255)); d.ellipse([7, 9, 22, 25], fill=(235, 80, 70, 255))
d.rectangle([9, 12, 11, 14], fill=(255, 170, 160, 255))
d.rectangle([15, 3, 16, 9], fill=(110, 75, 40, 255))
d.polygon([(17, 5), (25, 2), (23, 8)], fill=(90, 170, 70, 255))
save(im, "artisan")

# Économie : pile de pièces
im, d = new()
for i, y in enumerate([24, 20, 16, 12]):
    d.ellipse([6, y - 3, 25, y + 4], fill=(205, 150, 30, 255)); d.ellipse([6, y - 4, 25, y + 2], fill=(250, 205, 60, 255))
d.ellipse([11, 7, 20, 11], fill=(255, 235, 140, 255))
d.text((13, 5), "$", fill=(180, 120, 20, 255))
save(im, "economie")

# Nether & End : moitié Nether, moitié End, œil au centre
im, d = new()
d.ellipse([3, 3, 28, 28], fill=(150, 40, 40, 255)); d.pieslice([3, 3, 28, 28], 270, 90, fill=(225, 222, 160, 255))
for (x, y) in [(7, 12), (9, 20), (12, 8)]: d.rectangle([x, y, x + 1, y + 1], fill=(230, 100, 40, 255))
for (x, y) in [(21, 10), (23, 19), (19, 23)]: d.rectangle([x, y, x + 1, y + 1], fill=(180, 175, 120, 255))
d.ellipse([11, 11, 20, 20], fill=(40, 120, 100, 255)); d.ellipse([13, 13, 18, 18], fill=(90, 210, 170, 255)); d.rectangle([15, 14, 16, 17], fill=(20, 40, 35, 255))
save(im, "nether_end")

# Gadgets : smartphone
im, d = new()
d.rounded_rectangle([9, 2, 22, 29], 2, fill=(230, 60, 60, 255))
d.rectangle([11, 5, 20, 22], fill=(120, 200, 235, 255)); d.rectangle([12, 6, 14, 8], fill=(220, 245, 255, 255))
d.ellipse([14, 24, 17, 27], fill=(250, 250, 250, 255))
save(im, "gadgets")

# planche d'aperçu (x4)
names = ["mega", "raids", "eleveur", "safari", "montures", "explorateur", "arenes", "legendes", "artisan", "economie", "nether_end", "gadgets"]
sheet = Image.new("RGBA", (6 * 136, 2 * 136), (60, 60, 60, 255))
for i, n in enumerate(names):
    ic = Image.open(os.path.join(OUT, n + ".png")).resize((128, 128), Image.NEAREST)
    sheet.paste(ic, ((i % 6) * 136 + 4, (i // 6) * 136 + 4), ic)
sheet.save(os.path.join(OUT, "_apercu.png"))
