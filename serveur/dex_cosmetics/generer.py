"""Cosmetiques Sakuflemon pour Dex Cosmetics (config/dex_cosmetics/ sur le serveur).

Genere dans ./config/ : cosmetics/<type>/<id>.json, model/hats/<id>.json et
textures/... (textures animees : PNG en bande verticale + .mcmeta).

Format repris des exemples du mod (pikachu_hat, giratina_arms, soul_aura) :
  - chapeau : y=0 = dessus de la tete, tete ~ x4..12 z3..11 y-8..0, devant = nord (z petit) ;
  - dos : display copie de giratina_arms (orientation a confirmer avec test_dos) ;
  - effet : icone textures/effects/<id>/gui/<id>.png (16x16 par image).

Usage : python3 generer.py   (ecrit ./config, a copier dans config/dex_cosmetics/)
"""
import json
import math
import os
import random
import shutil

from PIL import Image, ImageDraw

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "config")
shutil.rmtree(SORTIE, ignore_errors=True)


def ecrire(chemin, donnees):
    chemin = os.path.join(SORTIE, chemin)
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (255,)


def nuance(c, f):
    return tuple(max(0, min(255, int(v * f))) for v in c[:3]) + (255,)


# ------------------------------------------------------------------ texture en cases de 8x8
class Texture:
    """Texture 64x64 decoupee en cases 8x8 ; chaque case = une fonction de dessin (img, x, y, image_anim)."""

    def __init__(self, images=1, frametime=3):
        self.images, self.frametime, self.cases = images, frametime, {}

    def case(self, nom, dessin):
        n = len(self.cases)
        self.cases[nom] = ((n % 8) * 8, (n // 8) * 8, dessin)
        return nom

    def uv(self, nom):
        x, y, _ = self.cases[nom]
        return [x, y, x + 8, y + 8]

    def png(self):
        im = Image.new("RGBA", (64, 64 * self.images), (0, 0, 0, 0))
        for x, y, dessin in self.cases.values():
            for k in range(self.images):
                dessin(im, x, y + 64 * k, k)
        return im


def uni(c, bruit=0.08, bord=True, graine=1):
    """Couleur avec un leger grain et un bord plus sombre (style pixel art)."""
    def d(im, x, y, k):
        r = random.Random(graine)
        for j in range(8):
            for i in range(8):
                f = 1 + r.uniform(-bruit, bruit)
                if bord and (i in (0, 7) or j in (0, 7)):
                    f *= 0.82
                im.putpixel((x + i, y + j), nuance(c, f))
    return d


def motif(lignes, couleurs, anim=None):
    """Case dessinee a la main (8 lignes de 8 caracteres) ; anim(k) -> couleurs modifiees par image."""
    def d(im, x, y, k):
        pal = anim(k) if anim else couleurs
        for j, l in enumerate(lignes):
            for i, ch in enumerate(l):
                if ch in pal:
                    im.putpixel((x + i, y + j), pal[ch])
    return d


def pulse(c, k, n, amp=0.35):
    return nuance(c, 1 + amp * math.sin(2 * math.pi * k / n))


# ------------------------------------------------------------------ modeles
def cube(de, a, tex, faces, rotation=None):
    """faces : nom de case pour toutes les faces, ou dict {face: case} avec "*" par defaut."""
    if isinstance(faces, str):
        faces = {"*": faces}
    el = {"from": de, "to": a, "faces": {}}
    for f in ("north", "east", "south", "west", "up", "down"):
        el["faces"][f] = {"uv": tex.uv(faces.get(f, faces["*"])), "texture": "#0"}
    if rotation:
        el["rotation"] = rotation
    return el


def rot(axe, angle, origine):
    return {"angle": angle, "axis": axe, "origin": origine}


AFFICHAGE_CHAPEAU = {"gui": {"rotation": [-180, -18, -180], "translation": [0, 2.5, 0], "scale": [0.9, 0.9, 0.9]},
                     "head": {"translation": [0, 14, 1.5], "scale": [1.6, 1.6, 1.6]}}
AFFICHAGE_DOS = {"thirdperson_lefthand": {"rotation": [105, 0, 0], "translation": [2, -12.5, 18.25]},
                 "gui": {"rotation": [28, 145, 0], "translation": [-1.75, 4, 0], "scale": [0.5, 0.5, 0.5]},
                 "head": {"translation": [11.25, -50.25, 13.75], "scale": [1.6, 1.6, 1.6]}}

COSMETIQUES = []  # (type, id, nom MiniMessage, description)


def chapeau(cid, nom, desc, tex, elements, gui_y=2.5, type_="HAT", dossier="hats", affichage=None):
    aff = json.loads(json.dumps(affichage or AFFICHAGE_CHAPEAU))
    if type_ == "HAT":
        aff["gui"]["translation"][1] = gui_y
    ref = f"dex_cosmetics:{dossier}/{cid}/{cid}"
    ecrire(f"model/{dossier}/{cid}.json", {"credit": "Sakuflemon", "texture_size": [64, 64],
                                         "textures": {"0": ref, "particle": ref}, "elements": elements, "display": aff})
    chemin = os.path.join(SORTIE, f"textures/{dossier}/{cid}/{cid}.png")
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    tex.png().save(chemin)
    if tex.images > 1:
        json.dump({"animation": {"frametime": tex.frametime}}, open(chemin + ".mcmeta", "w"))
    c = {"id": cid, "type": type_, "display_name": nom, "description": [f"<gray>{desc}</gray>", "<dark_gray>Sakuflemon</dark_gray>"],
         "model": f"dex_cosmetics:{dossier}/{cid}", "texture": f"dex_cosmetics:{dossier}/{cid}"}
    c["transform"] = ({"offset_x": 0.0, "offset_y": 0.0, "offset_z": 0.0, "scale_x": 1.0, "scale_y": 1.0, "scale_z": 1.0}
                      if type_ == "HAT" else {"scale_x": 1.0, "scale_y": 1.0, "scale_z": 1.0})
    ecrire(f"cosmetics/{dossier}/{cid}.json", c)
    COSMETIQUES.append((type_, cid, nom, desc))


ROUGE, BLANC, NOIR = rgb("d6303a"), rgb("f2f2f2"), rgb("26262c")
OR, OR_F = rgb("f2c230"), rgb("b8860b")

# ---- Casquette de Dresseur
t = Texture()
t.case("rouge", uni(ROUGE))
t.case("rouge_f", uni(nuance(ROUGE, 0.75)))
t.case("logo", motif(["wwwwwwww", "wwwRRwww", "wwRRRRww", "wRRRRRRw", "wkkwwkkw", "wwwwwwww", "wwwwwwww", "rrrrrrrr"],
                     {"w": BLANC, "R": ROUGE, "k": NOIR, "r": nuance(ROUGE, 0.8)}))
chapeau("casquette_dresseur", "<b><gradient:#FF4B4B:#FFFFFF>Casquette de Dresseur</gradient></b>",
        "La casquette des futurs Maîtres.", t, [
            cube([3.5, 0, 2.5], [12.5, 4, 12], t, {"*": "rouge", "north": "logo"}),
            cube([4.5, 4, 3.5], [11.5, 5, 11], t, "rouge"),
            cube([7.5, 5, 7], [8.5, 5.5, 8], t, "rouge_f"),
            cube([4, 0, -2.5], [12, 0.8, 2.5], t, "rouge_f", rot("x", 0, [8, 0, 2.5])),
        ])

# ---- Chapeau Citrouille (visage qui vacille)
ORANGE = rgb("e8822a")
t = Texture(images=6, frametime=3)
t.case("orange", uni(ORANGE, 0.1))
t.case("tige", uni(rgb("5b7a2a")))
t.case("feuille", uni(rgb("6fb33a")))


def visage(k):
    lueur = pulse(rgb("ffd23f"), k, 6, 0.3)
    return {"o": ORANGE, "y": lueur, "d": nuance(ORANGE, 0.7)}


t.case("visage", motif(["oooooooo", "oyyooyyo", "oyyooyyo", "oooooooo", "oyooooyo", "ooyyyyoo", "ooodyooo", "oooooooo"], {}, visage))
chapeau("chapeau_citrouille", "<b><gradient:#FFB347:#FF6A00>Chapeau Citrouille</gradient></b>",
        "Souvenir de l'île Citrouille.", t, [
            cube([2.5, 0, 1.5], [13.5, 7, 12.5], t, {"*": "orange", "north": "visage"}),
            cube([7, 7, 6], [9, 9.5, 8], t, "tige"),
            cube([9, 7.2, 6.5], [12, 7.7, 8], t, "feuille", rot("z", -22.5, [9, 7.5, 7])),
        ], gui_y=1.5)

# ---- Couronne Celeste (gemmes scintillantes)
t = Texture(images=8, frametime=2)
t.case("or", uni(OR, 0.12))
t.case("or_f", uni(OR_F))


def gemme(k):
    c = rgb("4fd8ff")
    return {"g": pulse(c, k, 8, 0.4), "w": BLANC if k in (0, 1) else pulse(c, k + 2, 8, 0.4), "o": OR}


t.case("gemme", motif(["oooooooo", "oggggggo", "ogwgggggo"[:8], "oggggggo", "oggggggo", "oggggggo", "oggggggo", "oooooooo"], {}, gemme))
murs = [([3.5, 0, 2.5], [12.5, 2.5, 3.5]), ([3.5, 0, 10.5], [12.5, 2.5, 11.5]),
        ([3.5, 0, 3.5], [4.5, 2.5, 10.5]), ([11.5, 0, 3.5], [12.5, 2.5, 10.5])]
pointes = []
for z0 in (2.5, 10.5):
    pointes += [([4, 2.5, z0], [5, 4.5, z0 + 1]), ([7.5, 2.5, z0], [8.5, 5.5, z0 + 1]), ([11, 2.5, z0], [12, 4.5, z0 + 1])]
pointes += [([3.5, 2.5, 6.5], [4.5, 4.5, 7.5]), ([11.5, 2.5, 6.5], [12.5, 4.5, 7.5])]
chapeau("couronne_celeste", "<b><gradient:#FFE680:#4FD8FF>Couronne Céleste</gradient></b>",
        "Pour les rois du ciel d'Incarnam.", t,
        [cube(a, b, t, "or") for a, b in murs] + [cube(a, b, t, "or_f") for a, b in pointes] + [
            cube([7, 0.6, 2.2], [9, 2, 2.5], t, "gemme"), cube([7, 0.6, 11.5], [9, 2, 11.8], t, "gemme"),
            cube([3.2, 0.6, 6.25], [3.5, 2, 7.75], t, "gemme"), cube([12.5, 0.6, 6.25], [12.8, 2, 7.75], t, "gemme")])

# ---- Bandeau Team Rocket
t = Texture()
t.case("noir", uni(NOIR))
t.case("R", motif(["kkkkkkkk", "kRRRRRkk", "kRkkkkRk", "kRRRRRkk", "kRkkRkkk", "kRkkkRkk", "kRkkkkRk", "kkkkkkkk"],
                  {"k": NOIR, "R": rgb("e0242b")}))
chapeau("bandeau_rocket", "<b><gradient:#E0242B:#26262C>Bandeau Team Rocket</gradient></b>",
        "Prépare-toi à des ennuis...", t, [
            cube([3.7, -3.2, 2.7], [12.3, -1.2, 11.3], t, {"*": "noir", "north": "R"}),
            cube([7, -3.5, 11.3], [9, -1, 12.3], t, "noir"),
            cube([7.2, -6, 11.5], [8, -3.5, 12], t, "noir", rot("z", 22.5, [7.6, -3.5, 11.7])),
            cube([8.2, -5.5, 11.5], [9, -3.5, 12], t, "noir", rot("z", -22.5, [8.6, -3.5, 11.7])),
        ], gui_y=7)

# ---- Aureole (pulsation doree)
t = Texture(images=8, frametime=2)
t.case("halo", lambda im, x, y, k: [im.putpixel((x + i, y + j), pulse(rgb("ffe066"), k + (i + j) % 8, 8, 0.3))
                                    for i in range(8) for j in range(8)])
chapeau("aureole", "<b><gradient:#FFFFFF:#FFE066>Auréole</gradient></b>", "Un ange passe...", t, [
    cube([4, 3, 3], [12, 3.6, 4], t, "halo"), cube([4, 3, 10], [12, 3.6, 11], t, "halo"),
    cube([4, 3, 4], [5, 3.6, 10], t, "halo"), cube([11, 3, 4], [12, 3.6, 10], t, "halo")], gui_y=0)

# ---- Oreilles d'Evoli
MARRON, CREME = rgb("a8703c"), rgb("f3dfb0")
t = Texture()
t.case("marron", uni(MARRON))
t.case("interieur", motif(["mmmmmmmm", "mmccccmm", "mmccccmm", "mmccccmm", "mccccccm", "mccccccm", "mccccccm", "mmmmmmmm"],
                          {"m": MARRON, "c": CREME}))
chapeau("oreilles_evoli", "<b><gradient:#C98A4B:#F3DFB0>Oreilles d'Évoli</gradient></b>", "Évoli, l'évolution à portée de tête.", t, [
    cube([3.5, 0, 6], [6, 6, 7.5], t, {"*": "marron", "north": "interieur"}, rot("z", 22.5, [5, 0, 7])),
    cube([10, 0, 6], [12.5, 6, 7.5], t, {"*": "marron", "north": "interieur"}, rot("z", -22.5, [11, 0, 7])),
], gui_y=1)

# ---- Chapeau de sorciere
VIOLET = rgb("5b2a86")
t = Texture(images=6, frametime=4)
t.case("violet", uni(VIOLET, 0.1))
t.case("bande", lambda im, x, y, k: [im.putpixel((x + i, y + j), pulse(rgb("ff8c1a"), k + i // 2, 6, 0.25))
                                     for i in range(8) for j in range(8)])
t.case("boucle", motif(["oooooooo", "oggggggo", "oglllglo"[:8], "oglooglo", "oglooglo", "ogllllgo", "oggggggo", "oooooooo"],
                       {"o": rgb("ff8c1a"), "g": OR, "l": OR_F}))
chapeau("chapeau_sorciere", "<b><gradient:#9B5DE5:#FF8C1A>Chapeau de Sorcière</gradient></b>", "Abracadabra... Citrouille !", t, [
    cube([1.5, 0, 0.5], [14.5, 0.8, 13.5], t, "violet"),
    cube([4, 0.8, 3], [12, 4, 11], t, "violet"),
    cube([3.9, 0.8, 2.9], [12.1, 1.8, 11.1], t, {"*": "bande", "north": "boucle"}),
    cube([5, 4, 4], [11, 7, 10], t, "violet", rot("x", 0, [8, 4, 7])),
    cube([6, 7, 5], [10, 9.5, 9], t, "violet", rot("x", -22.5, [8, 7, 7])),
    cube([7, 9, 6.5], [9, 11.5, 8.5], t, "violet", rot("x", -22.5, [8, 7, 7])),
], gui_y=-1)

# ---- Couronne de fleurs
t = Texture()
t.case("feuilles", uni(rgb("4c9a3a")))
for n, c in [("rose", "ff7eb6"), ("jaune", "ffd84a"), ("bleu", "6ec6ff"), ("blanc", "ffffff")]:
    t.case(n, motif(["........", ".pp..pp.", ".pyyyyp."[:8], "..yccy..", "..ycy...", ".pyyyp..", ".pp..pp.", "........"],
                    {"p": rgb(c), "y": nuance(rgb(c), 0.85), "c": rgb("ffcc33")}))
anneau = [cube([3.6, -0.6, 2.6], [12.4, 0.4, 3.4], t, "feuilles"), cube([3.6, -0.6, 10.6], [12.4, 0.4, 11.4], t, "feuilles"),
          cube([3.6, -0.6, 3.4], [4.4, 0.4, 10.6], t, "feuilles"), cube([11.6, -0.6, 3.4], [12.4, 0.4, 10.6], t, "feuilles")]
fleurs, couleurs = [], ["rose", "jaune", "bleu", "blanc"]
for i, (x, z) in enumerate([(4, 2.3), (6.5, 2.3), (9, 2.3), (11.3, 2.3), (11.3, 5), (11.3, 8), (11.3, 10.6), (8.5, 10.6),
                            (5.8, 10.6), (3.3, 10.6), (3.3, 8), (3.3, 5)]):
    fleurs.append(cube([x - 0.7, -0.4, z - 0.7], [x + 0.7, 1, z + 0.7], t, couleurs[i % 4]))
chapeau("couronne_fleurs", "<b><gradient:#FF7EB6:#FFD84A>Couronne de fleurs</gradient></b>", "Le printemps toute l'année.", t,
        anneau + fleurs, gui_y=2)

# ---- Chapeau de paille
PAILLE = rgb("e9c46a")
t = Texture()
t.case("paille", motif(["abababab", "babababa"] * 4, {"a": PAILLE, "b": nuance(PAILLE, 0.88)}))
t.case("ruban", uni(rgb("c1272d")))
chapeau("chapeau_paille", "<b><gradient:#E9C46A:#C1272D>Chapeau de paille</gradient></b>", "Le futur Roi des Dresseurs !", t, [
    cube([1, 0, 0], [15, 0.6, 14], t, "paille"),
    cube([4, 0.6, 3], [12, 4, 11], t, "paille"),
    cube([3.9, 0.6, 2.9], [12.1, 1.6, 11.1], t, "ruban"),
], gui_y=2)

# ---- Lunettes d'aviateur (reflet anime)
t = Texture(images=8, frametime=2)
t.case("cuir", uni(rgb("6b4226")))


def verre(k):
    return {"o": OR_F, "c": rgb("7fd6ff"), "w": BLANC, "d": rgb("3a8fc0")}


def verre_d(im, x, y, k):
    for j in range(8):
        for i in range(8):
            if i in (0, 7) or j in (0, 7):
                c = OR_F
            elif i + j == k + 2 or i + j == k + 3:
                c = BLANC
            else:
                c = rgb("7fd6ff") if j < 4 else rgb("3a8fc0")
            im.putpixel((x + i, y + j), c)


t.case("verre", verre_d)
chapeau("lunettes_aviateur", "<b><gradient:#7FD6FF:#B8860B>Lunettes d'aviateur</gradient></b>", "Prêt pour le décollage sur Dracaufeu.", t, [
    cube([3.7, -3.8, 2.7], [12.3, -3, 11.3], t, "cuir"),
    cube([4.3, -5, 2.2], [7.5, -2, 2.8], t, {"*": "cuir", "north": "verre"}),
    cube([8.5, -5, 2.2], [11.7, -2, 2.8], t, {"*": "cuir", "north": "verre"}),
], gui_y=7)

# ---- Objet de dos de test : fleches rouge = +x, verte = +y, bleue = +z (pour caler les ailes et capes)
t = Texture()
for n, c in [("blanc", "ffffff"), ("x", "ff2020"), ("y", "20ff20"), ("z", "2060ff")]:
    t.case(n, uni(rgb(c), 0, False))
chapeau("test_dos", "<red><b>Test dos (admin)</b></red>", "Flèches : rouge +x, verte +y, bleue +z.", t, [
    cube([-1, -1, -1], [1, 1, 1], t, "blanc"),
    cube([1, -0.5, -0.5], [12, 0.5, 0.5], t, "x"), cube([-0.5, 1, -0.5], [0.5, 12, 0.5], t, "y"),
    cube([-0.5, -0.5, 1], [0.5, 0.5, 12], t, "z"),
], type_="BACK", dossier="back", affichage=AFFICHAGE_DOS)


# ------------------------------------------------------------------ effets de particules (icone animee)
def icone(cid, couleurs, forme="point", images=6):
    """Icone 16x16 animee : petites particules qui montent."""
    im = Image.new("RGBA", (16, 16 * images), (0, 0, 0, 0))
    r = random.Random(cid)
    pts = [(r.randrange(2, 13), r.randrange(0, 16), r.choice(couleurs)) for _ in range(7)]
    for k in range(images):
        d = ImageDraw.Draw(im)
        for x, y, c in pts:
            yy = (y - k * 16 // images) % 16 + 16 * k
            c = rgb(c)
            if forme == "coeur":
                for dx, dy in [(0, 0), (2, 0), (-1, 1), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (1, 3)]:
                    if 16 * k <= yy + dy < 16 * k + 16 and 0 <= x + dx < 16:
                        im.putpixel((x + dx, yy + dy), c)
            elif forme == "etoile":
                for dx, dy in [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]:
                    if 16 * k <= yy + dy < 16 * k + 16:
                        im.putpixel((x + dx, yy + dy), c)
            else:
                d.rectangle((x, yy, x + 1, min(yy + 1, 16 * k + 15)), fill=c)
    chemin = os.path.join(SORTIE, f"textures/effects/{cid}/gui/{cid}.png")
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    im.save(chemin)
    json.dump({"animation": {"frametime": 3}}, open(chemin + ".mcmeta", "w"))


EFFETS = [  # id, nom, description, intervalle, commandes, couleurs icone, forme
    ("effet_coeurs", "<b><gradient:#FF9AD5:#FF3B7A>Traînée de cœurs</gradient></b>", "Des cœurs autour de toi.", 10,
     ["particle heart ~ ~2.2 ~ 0.35 0.1 0.35 0 1"], ["ff3b7a", "ff9ad5"], "coeur"),
    ("effet_flammes", "<b><gradient:#FFD36B:#FF4A1C>Traînée de flammes</gradient></b>", "Digne d'un Dracaufeu.", 3,
     ["particle flame ~ ~0.1 ~ 0.25 0.05 0.25 0.01 3", "particle small_flame ~ ~0.5 ~ 0.3 0.3 0.3 0.01 1"], ["ff4a1c", "ffd36b", "ff8c1a"], "point"),
    ("effet_notes", "<b><gradient:#7CFFB2:#3BA7FF>Notes de musique</gradient></b>", "Ton thème de combat.", 8,
     ["particle note ~ ~2.3 ~ 0.45 0.1 0.45 1 1"], ["7cffb2", "3ba7ff", "ff6bd5"], "etoile"),
    ("effet_etoiles", "<b><gradient:#FFFFFF:#FFE66B>Poussière d'étoiles</gradient></b>", "Brille comme un shiny.", 4,
     ["particle end_rod ~ ~1 ~ 0.4 0.6 0.4 0.01 1", "particle wax_on ~ ~1.2 ~ 0.5 0.6 0.5 0 2"], ["ffffff", "ffe66b"], "etoile"),
    ("effet_eclairs", "<b><gradient:#FFF36B:#FFB000>Étincelles</gradient></b>", "Électrique !", 3,
     ["particle electric_spark ~ ~1 ~ 0.4 0.6 0.4 0.1 4"], ["fff36b", "ffb000", "ffffff"], "point"),
    ("effet_neige", "<b><gradient:#FFFFFF:#9BE7FF>Flocons</gradient></b>", "Un petit air de Givrali.", 4,
     ["particle snowflake ~ ~2.4 ~ 0.6 0.1 0.6 0.01 2"], ["ffffff", "9be7ff"], "etoile"),
    ("effet_cerisier", "<b><gradient:#FFC2E2:#FF7EB6>Pétales de cerisier</gradient></b>", "Les pétales dansent autour de toi.", 4,
     ["particle cherry_leaves ~ ~2.3 ~ 0.6 0.2 0.6 0 2"], ["ffc2e2", "ff7eb6"], "point"),
    ("effet_ames", "<b><gradient:#6BCBFF:#2B3A67>Âmes errantes</gradient></b>", "Pour les fans de Spectrum.", 4,
     ["particle soul ~ ~0.6 ~ 0.3 0.4 0.3 0.02 1", "particle sculk_soul ~ ~0.2 ~ 0.4 0.05 0.4 0.01 1"], ["6bcbff", "2b3a67", "aee9ff"], "point"),
    ("effet_arcenciel", "<b><gradient:#FF4B4B:#FFD84A:#4BFF7A:#4BB8FF:#B44BFF>Arc-en-ciel</gradient></b>", "Toutes les couleurs à tes pieds.", 3,
     ["particle dust{color:[1.0,0.3,0.3],scale:1} ~ ~0.2 ~ 0.4 0.05 0.4 0 1", "particle dust{color:[1.0,0.85,0.3],scale:1} ~ ~0.2 ~ 0.4 0.05 0.4 0 1",
      "particle dust{color:[0.3,1.0,0.5],scale:1} ~ ~0.2 ~ 0.4 0.05 0.4 0 1", "particle dust{color:[0.3,0.7,1.0],scale:1} ~ ~0.2 ~ 0.4 0.05 0.4 0 1",
      "particle dust{color:[0.7,0.3,1.0],scale:1} ~ ~0.2 ~ 0.4 0.05 0.4 0 1"], ["ff4b4b", "ffd84a", "4bff7a", "4bb8ff", "b44bff"], "point"),
    ("effet_enchant", "<b><gradient:#C8A2FF:#6B4BFF>Runes mystiques</gradient></b>", "Des runes d'Arceus tournoient.", 3,
     ["particle enchant ~ ~1.6 ~ 0.5 0.5 0.5 0.6 6"], ["c8a2ff", "6b4bff", "ffffff"], "etoile"),
    ("effet_totem", "<b><gradient:#FFE066:#4BFF7A>Aura du Totem</gradient></b>", "Tu as l'air invincible.", 4,
     ["particle totem_of_undying ~ ~1 ~ 0.3 0.5 0.3 0.1 2"], ["ffe066", "4bff7a"], "point"),
    ("effet_dragon", "<b><gradient:#E05BFF:#5B1A7A>Souffle draconique</gradient></b>", "Le souffle de Rayquaza.", 4,
     ["particle dragon_breath ~ ~0.2 ~ 0.35 0.05 0.35 0.01 2"], ["e05bff", "5b1a7a", "ff9cf0"], "point"),
    ("effet_bulles", "<b><gradient:#BFF3FF:#3BA7FF>Bulles</gradient></b>", "Comme un Tarsal sous l'eau.", 4,
     ["particle bubble_pop ~ ~1.2 ~ 0.4 0.5 0.4 0.02 2", "particle dripping_water ~ ~2.1 ~ 0.3 0.1 0.3 0 1"], ["bff3ff", "3ba7ff", "ffffff"], "point"),
]
for cid, nom, desc, iv, cmds, cols, forme in EFFETS:
    icone(cid, cols, forme)
    ecrire(f"cosmetics/effects/{cid}.json", {
        "id": cid, "type": "EFFECT", "display_name": nom, "description": [f"<gray>{desc}</gray>", "<dark_gray>Sakuflemon</dark_gray>"],
        "model": f"dex_cosmetics:effects/{cid}", "texture": f"dex_cosmetics:effects/{cid}/gui/{cid}",
        "effect": {"kind": "particle", "particle": {"interval_ticks": iv, "commands": cmds}}})
    COSMETIQUES.append(("EFFECT", cid, nom, desc))

if __name__ == "__main__":
    print(len(COSMETIQUES), "cosmétiques :", ", ".join(c[1] for c in COSMETIQUES))
