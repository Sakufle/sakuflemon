"""Fonds des menus SkiesGUIs (glyphes de la police sakuflemon:gui).

Genere assets/sakuflemon/textures/font/gui/<nom>.png + font/gui.json a partir
de boutique_v1.png (style d'origine : bandeau rouge, slots gris, bas = inventaire).
Le glyphe  (boutique v1) reste inchange pour ne pas casser la boutique en place.

Usage : python3 generer_gui.py <dossier_sortie_assets_sakuflemon>
"""
import json
import os
import sys

from PIL import Image

ICI = os.path.dirname(os.path.abspath(__file__))
V1 = Image.open(os.path.join(ICI, "boutique_v1.png")).convert("RGBA")

FOND = (198, 198, 198, 255)
ROUGE = (200, 40, 40, 255)
ROUGE_F = (160, 32, 32, 255)
BLANC = (236, 236, 240, 255)
NOIR = (25, 25, 30, 255)
SLOT = (139, 139, 139, 255)
OMBRE = (55, 55, 55, 255)
CLAIR = (255, 255, 255, 255)
COULEURS = {
    "or": (230, 170, 40, 255),
    "violet": (150, 70, 210, 255),
    "bleu": (60, 110, 220, 255),
    "vert": (60, 180, 90, 255),
    "rouge": (200, 40, 40, 255),
    "gris": (110, 110, 115, 255),
    "cyan": (40, 190, 200, 255),
    "rose": (230, 100, 170, 255),
}

# Police 5x5 (majuscules sans accents)
P = {
    "A": ".###.#...#######...##...#", "B": "####.#...#####.#...#####.",
    "C": ".#####....#....#.....####", "D": "####.#...##...##...#####.",
    "E": "######....####.#....#####", "F": "######....####.#....#....",
    "G": ".#####....#..###...#.####", "H": "#...##...#######...##...#",
    "I": "#####..#....#....#..#####", "J": "....#....#....##...#.###.",
    "K": "#...##..#.###..#..#.#...#", "L": "#....#....#....#....#####",
    "M": "#...###.###.#.##...##...#", "N": "#...###..##.#.##..###...#",
    "O": ".###.#...##...##...#.###.", "P": "####.#...#####.#....#....",
    "Q": ".###.#...##.#.##..#..##.#", "R": "####.#...#####.#..#.#...#",
    "S": ".#####.....###.....#####.", "T": "#####..#....#....#....#..",
    "U": "#...##...##...##...#.###.", "V": "#...##...#.#.#..#.#...#..",
    "W": "#...##...##.#.###.###...#", "X": "#...#.#.#...#...#.#.#...#",
    "Y": "#...#.#.#...#....#....#..", "Z": "#####...#...#...#...#####",
    "0": ".###.#..###.#.###..#.###.", "1": "..#...##....#....#...###.",
    "2": "####.....#.###.#....#####", "3": "####.....#.###.....#####.",
    "4": "#...##...#.####....#....#", "5": "######....####.....#####.",
    " ": "." * 25, "?": ".###.#...#..##.......#...",
    "&": ".##..#..#..##.##..#..##.#", "'": "..#....#.................",
    "!": "..#....#....#.........#..", "-": "..........###............",
}


def texte(im, x, y, s, coul=NOIR):
    for ch in s:
        g = P.get(ch, P[" "])
        w = 3 if ch in "'!-" else 5
        for i, c in enumerate(g[:25]):
            if c == "#":
                px, py = i % 5, i // 5
                if w == 3:
                    px -= 1
                im.putpixel((x + px, y + py), coul)
        x += w + 1
    return x


def largeur(s):
    return sum((3 if ch in "'!-" else 5) + 1 for ch in s) - 1


def bandeau(im, y, s, x0=8, x1=168):
    """Bandeau rouge avec etiquette blanche centree (comme GRADES / CLES)."""
    for yy in range(y + 2, y + 14):
        for xx in range(x0, x1):
            im.putpixel((xx, yy), ROUGE)
    w = largeur(s) + 6
    cx = (x0 + x1) // 2 - w // 2
    for yy in range(y + 3, y + 13):
        for xx in range(cx, cx + w):
            bord = yy in (y + 3, y + 12) or xx in (cx, cx + w - 1)
            im.putpixel((xx, yy), NOIR if bord else BLANC)
    texte(im, cx + 3, y + 5, s)


def slot(im, col, row, coul=None):
    x, y = 7 + 18 * col, 17 + 18 * row
    for yy in range(y, y + 18):
        for xx in range(x, x + 18):
            if coul:
                c = coul if (xx in (x, x + 17) or yy in (y, y + 17)) else (
                    OMBRE if (xx == x + 1 or yy == y + 1) else SLOT)
            else:
                c = OMBRE if (xx == x or yy == y) else (CLAIR if (xx == x + 17 or yy == y + 17) else SLOT)
            im.putpixel((xx, yy), c)


def fond(rows, titre):
    h = rows * 18 + 114
    im = Image.new("RGBA", (176, h), (0, 0, 0, 0))
    # haut (cadre + bandeau titre) et bas (inventaire) repris du v1
    haut = V1.crop((0, 0, 176, 17))
    im.paste(haut, (0, 0))
    for yy in range(17, 18 + rows * 18):
        for xx in range(176):
            im.putpixel((xx, yy), V1.getpixel((xx, 18)))
    im.paste(V1.crop((0, 108, 176, 204)), (0, 18 + rows * 18))
    # titre : on efface l'ancien texte et on ecrit le nouveau
    for yy in range(5, 14):
        for xx in range(30, 150):
            if im.getpixel((xx, yy))[3] and im.getpixel((xx, yy)) != ROUGE:
                im.putpixel((xx, yy), ROUGE)
    texte(im, 88 - largeur(titre) // 2, 6, titre, BLANC)
    return im


def nav(im, row, slots):
    for col, coul in slots:
        slot(im, col, row, COULEURS[coul])


MENUS = {}

# Menu principal (3 rangees)
m = fond(3, "MENU SAKUFLEMON")
bandeau(m, 17, "QUE VEUX-TU FAIRE ?")
for col, c in [(1, "or"), (3, "violet"), (5, "bleu"), (7, "vert")]:
    slot(m, col, 1, COULEURS[c])
slot(m, 4, 2, COULEURS["rouge"])
MENUS["menu"] = m

# Boutique v2 (6 rangees)
b = fond(6, "BOUTIQUE SAKUFLEMON")
bandeau(b, 17, "GRADES")
for col, c in [(2, "vert"), (4, "violet"), (6, "or")]:
    slot(b, col, 1, COULEURS[c])
bandeau(b, 53, "CLES DE CAISSES")
texte(b, 12, 80, "X1")
texte(b, 12, 98, "X5")
for row in (3, 4):
    for col, c in [(2, "vert"), (4, "cyan"), (6, "or")]:
        slot(b, col, row, COULEURS[c])
nav(b, 5, [(0, "gris"), (4, "rouge"), (8, "violet")])
MENUS["boutique"] = b

# Cosmetiques (6 rangees)
c = fond(6, "COSMETIQUES")
bandeau(c, 17, "CHAPEAUX")
for col in range(2, 7):
    slot(c, col, 1, COULEURS["violet"])
bandeau(c, 53, "DOS", 8, 86)
bandeau(c, 53, "EFFETS", 90, 168)
for col in range(1, 4):
    slot(c, col, 3, COULEURS["bleu"])
for col in range(5, 8):
    slot(c, col, 3, COULEURS["rose"])
    slot(c, col, 4, COULEURS["rose"])
nav(c, 5, [(0, "gris"), (4, "vert"), (8, "or")])
MENUS["cosmetiques"] = c

# Teleportation (4 rangees)
t = fond(4, "TELEPORTATION")
bandeau(t, 17, "DESTINATIONS")
for col, c2 in [(1, "cyan"), (3, "or"), (5, "vert"), (7, "bleu")]:
    slot(t, col, 1, COULEURS[c2])
for col in (2, 4, 6):
    slot(t, col, 2, COULEURS["gris"])
nav(t, 3, [(0, "gris")])
MENUS["teleportation"] = t

GLYPHES = {"boutique": "", "menu": "", "boutique_v2": "",
           "cosmetiques": "", "teleportation": ""}

if __name__ == "__main__":
    out = sys.argv[1]
    tex = os.path.join(out, "textures/font/gui")
    os.makedirs(tex, exist_ok=True)
    V1.save(os.path.join(tex, "boutique.png"))
    providers = [{"type": "space", "advances": {"": -8, "": -177}},
                 {"type": "bitmap", "file": "sakuflemon:font/gui/boutique.png",
                  "ascent": 13, "height": 204, "chars": [""]}]
    for nom, im in MENUS.items():
        fichier = "boutique_v2" if nom == "boutique" else nom
        im.save(os.path.join(tex, fichier + ".png"))
        providers.append({"type": "bitmap", "file": f"sakuflemon:font/gui/{fichier}.png",
                          "ascent": 13, "height": im.size[1], "chars": [GLYPHES[fichier]]})
    os.makedirs(os.path.join(out, "font"), exist_ok=True)
    with open(os.path.join(out, "font/gui.json"), "w") as f:
        json.dump({"providers": providers}, f)
    print("ok", list(MENUS))
