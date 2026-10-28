"""Menus Sakuflemon (SkiesGUIs) dans le style Pokemon Noir et Blanc.

Genere en une fois :
  - les fonds (glyphes de la police sakuflemon:gui, ..) et l'objet
    invisible (paper, custom_model_data 7020) pour le resource pack sakuflemon-interface ;
  - les menus config/skiesguis/guis/{menu,boutique,cosmetiques,teleportation}.json.

Chaque carte est cliquable sur toutes ses cases : l'icone sur la premiere, l'objet
invisible sur les autres, avec les memes actions. Les achats reprennent les commandes
de la boutique v1 (sauvegarde/boutique_v1.json) : lp parent set + team join, crates key give.
Le glyphe  (boutique v1) reste inchange.

Usage : python3 generer.py <dossier assets/ du resource pack>
"""
import json
import os
import sys

from PIL import Image, ImageDraw

ICI = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ dessin
NUIT = (20, 28, 52, 255)
GRILLE = (28, 40, 70, 255)
CADRE = (70, 160, 235, 255)
CYAN = (90, 200, 245, 255)
ENCRE = (14, 26, 54, 255)
BLANC = (245, 245, 250, 255)
OMBRE = (8, 12, 26, 255)
CASE = (12, 18, 36, 255)
CASE_BORD = (55, 85, 145, 255)
TYPES = {  # couleurs facon types Pokemon
    "bleu": (70, 150, 235), "or": (230, 170, 50), "violet": (160, 90, 220), "vert": (80, 190, 90),
    "rouge": (220, 70, 60), "gris": (130, 135, 150), "cyan": (60, 200, 210), "rose": (235, 110, 175),
    "orange": (235, 130, 50),
}

P = {
    "A": ".###.#...######...##...#", "B": "####.#...#####.#...#####.",
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
    "6": ".####" "#...." "####." "#...#" ".###.", "7": "#####....#...#...#....#..",
    "8": ".###.#...#.###.#...#.###.", "9": ".###.#...#.####....#####.",
    " ": "." * 25, "?": ".###.#...#..##.......#...", "%": "##..###.#...#...#.###..##",
    "'": "..#....#.................", "!": "..#....#....#.........#..",
    "-": "..........###............", ":": ".......#.........#.......",
    "/": "....#...#...#...#...#....", "+": ".......#...###...#.......",
    ".": "......................#..", "<": "...#...#...#.....#.....#.",
    ">": ".#.....#.....#...#...#...",
}
P["A"] = ".###." "#...#" "#####" "#...#" "#...#"
ETROITS = "'!-:.I1"


def _larg(ch):
    return 3 if ch in "'!-:." else 5


def largeur(s, k=1):
    return (sum(_larg(c) + 1 for c in s) - 1) * k


def texte(im, x, y, s, coul=BLANC, k=1, ombre=True):
    if ombre:
        texte(im, x + k, y + k, s, OMBRE, k, False)
    for ch in s:
        g = P.get(ch, P[" "])
        dx = -1 if _larg(ch) == 3 else 0
        for i, c in enumerate(g[:25]):
            if c == "#":
                px, py = (i % 5 + dx) * k, (i // 5) * k
                for a in range(k):
                    for b in range(k):
                        im.putpixel((x + px + a, y + py + b), coul)
        x += (_larg(ch) + 1) * k
    return x


def melange(c, d, t):
    return tuple(int(c[i] * (1 - t) + d[i] * t) for i in range(3)) + (255,)


def boite(im, x0, y0, x1, y1, accent, r=3):
    """Carte arrondie : halo clair, bord couleur, degrade sombre, reflet en haut."""
    d = ImageDraw.Draw(im)
    a = TYPES[accent]
    d.rounded_rectangle((x0, y0, x1, y1), r, fill=melange(a, (255, 255, 255), 0.55))
    d.rounded_rectangle((x0 + 1, y0 + 1, x1 - 1, y1 - 1), r - 1, fill=a + (255,))
    for y in range(y0 + 2, y1 - 1):
        t = (y - y0) / max(1, y1 - y0)
        d.line((x0 + 2, y, x1 - 2, y), fill=melange(a, (10, 16, 40), 0.55 + 0.25 * t))
    d.line((x0 + 3, y0 + 2, x1 - 3, y0 + 2), fill=melange(a, (255, 255, 255), 0.25))


def case(c, r):
    return 7 + 18 * c, 17 + 18 * r


def carte(im, c0, c1, r0, r1, accent, titre, sous="", icone=True):
    x0, y0 = case(c0, r0)
    x1, y1 = case(c1 + 1, r1 + 1)
    boite(im, x0, y0 + 1, x1 - 1, y1 - 2, accent)
    if icone:  # pastille sombre derriere l'icone (1re case)
        ImageDraw.Draw(im).ellipse((x0 + 1, y0 + 1, x0 + 17, y0 + 17), fill=(8, 14, 34, 255),
                                   outline=melange(TYPES[accent], (255, 255, 255), 0.4))
    if not icone:
        assert largeur(titre) <= x1 - x0 - 6, titre
        texte(im, x0 + (x1 - x0 - largeur(titre)) // 2, y0 + (y1 - y0 - 5) // 2, titre)
        return
    tx = x0 + 21
    assert largeur(titre) <= x1 - tx - 3, titre
    if r1 > r0:  # carte haute : titre a cote de l'icone, sous-titre en dessous
        texte(im, tx, y0 + 7, titre)
        if sous:
            assert largeur(sous) <= x1 - x0 - 6, sous
            texte(im, x0 + 4, y0 + 25, sous, (255, 220, 110, 255))
    else:
        texte(im, tx, y0 + (3 if sous else 7), titre)
        if sous:
            assert largeur(sous) <= x1 - tx - 3, sous
            texte(im, tx, y0 + 10, sous, (255, 220, 110, 255))


def tuile(im, c, r, accent):
    x, y = case(c, r)
    boite(im, x, y, x + 17, y + 17, accent, 3)
    ImageDraw.Draw(im).rectangle((x + 2, y + 3, x + 15, y + 15), fill=(8, 14, 34, 255))


def etiquette(im, c0, c1, r, s, accent="bleu"):
    x0, y0 = case(c0, r)
    x1, _ = case(c1 + 1, r)
    boite(im, x0 + 2, y0 + 4, x1 - 3, y0 + 15, accent, 4)
    texte(im, x0 + (x1 - x0 - largeur(s)) // 2, y0 + 7, s)


def fond(rangees, titre):
    h = rangees * 18 + 114
    im = Image.new("RGBA", (176, h), NUIT)
    d = ImageDraw.Draw(im)
    for x in range(0, 176, 8):
        d.line((x, 0, x, h), fill=GRILLE)
    for y in range(0, h, 8):
        d.line((0, y, 176, y), fill=GRILLE)
    d.rounded_rectangle((0, 0, 175, h - 1), 4, outline=CADRE, width=2)
    # bandeau de titre facon "POKEMON INFO"
    fin = 14 + largeur(titre) + 10
    d.polygon([(3, 3), (fin + 8, 3), (fin, 14), (3, 14)], fill=CYAN)
    d.line((3, 15, fin, 15), fill=(40, 110, 170, 255))
    texte(im, 9, 6, titre, ENCRE, ombre=False)
    texte(im, 172 - largeur("SAKUFLEMON"), 6, "SAKUFLEMON", CYAN)
    # inventaire du joueur
    y0 = 18 + rangees * 18 + 13
    d.line((6, y0 - 4, 169, y0 - 4), fill=CASE_BORD)
    for r in range(4):
        for c in range(9):
            x, y = 7 + 18 * c, y0 + 18 * r + (4 if r == 3 else 0)
            d.rectangle((x, y, x + 17, y + 17), fill=CASE, outline=CASE_BORD)
    return im


# ------------------------------------------------------------------ menus JSON
SON_OK = "minecraft:ui.toast.challenge_complete"
SON_ACHAT = "minecraft:entity.experience_orb.pickup"
SON_NON = "minecraft:block.note_block.bass"
SON_CLIC = "minecraft:ui.button.click"
# structure_void : objet que ni Polymer ni Dex Cosmetics ne surchargent (paper = chapeaux Dex)
VIDE = {"item": "minecraft:structure_void", "custom_model_data": 7020}
CACHE = {"minecraft:hide_additional_tooltip": {}}
BRILLE = {"minecraft:hide_additional_tooltip": {}, "minecraft:enchantment_glint_override": True}


def court(n):
    return (f"{n // 1000}K" if n % 1000 == 0 else f"{n / 1000:.1f}K") + " CD" if n >= 1000 else f"{n} CD"


def prix(n):
    return f"{n:,}".replace(",", " ")


def base(glyphe, rangees, alias):
    return {"title": f"<white><font:sakuflemon:gui>{glyphe}</font>", "size": rangees,
            "alias_commands": alias,
            "open_actions": {"son": {"type": "PLAYSOUND", "sound": "cobblemon:pc.on"}},
            "close_actions": {"son": {"type": "PLAYSOUND", "sound": "cobblemon:pc.off"}},
            "items": {}}


def slots(c0, c1, r0, r1):
    return [r * 9 + c for r in range(r0, r1 + 1) for c in range(c0, c1 + 1)]


def poser(gui, nom, item, zone, **champs):
    """Icone sur la 1re case de la zone, objet invisible (memes actions) sur le reste."""
    cases = slots(*zone) if isinstance(zone, tuple) else [zone]
    icone = cases[0]  # en haut a gauche, sur la pastille sombre
    champs.setdefault("nbt", CACHE)
    gui["items"][nom] = dict({"item": item, "slots": [icone]}, **champs)
    reste = [s for s in cases if s != icone]
    if reste:
        gui["items"][nom + "_carte"] = dict(champs, **VIDE, slots=reste)


def ouvrir(g):
    return {"son": {"type": "PLAYSOUND", "sound": SON_CLIC}, "ouvrir": {"type": "OPEN_GUI", "id": g}}


def achat(montant, commandes, message, son=SON_ACHAT, conditions=None, refus=None, fin=None):
    req = {"argent": {"type": "CURRENCY", "currency": "", "amount": montant, "comparison": ">="}}
    req.update(conditions or {})
    actions = {"payer": {"type": "CURRENCY_WITHDRAW", "currency": "", "amount": montant},
               "donner": {"type": "COMMAND_CONSOLE", "commands": commandes},
               "msg": {"type": "MESSAGE", "message": [message]},
               "son": {"type": "PLAYSOUND", "sound": son}}
    actions.update(fin or {"refresh": {"type": "REFRESH_GUI"}})
    return {"click_requirements": {"requirements": req, "deny_actions": {
        "msg": {"type": "MESSAGE", "message": [refus or f"<red>Il te faut {prix(montant)} CobbleDollars."]},
        "son": {"type": "PLAYSOUND", "sound": SON_NON}}}, "click_actions": actions}


IMAGES, GUIS = {}, {}

# ---- Menu principal (4 rangees, 4 grandes cartes)
im, g = fond(4, "MENU"), base("", 4, ["menu", "m"])
MENU = [  # nom, item, zone (c0,c1,r0,r1), couleur, titre image, sous-titre, nom MiniMessage, lore, actions
    ("boutique", "minecraft:gold_ingot", (0, 3, 0, 1), "or", "BOUTIQUE", "GRADES/CLES",
     "<gold><b>Boutique", ["<gray>Grades et clés de caisses"], ouvrir("boutique")),
    ("cosmetiques", "minecraft:amethyst_shard", (5, 8, 0, 1), "violet", "STYLE", "COSMETIQUES",
     "<light_purple><b>Cosmétiques", ["<gray>Chapeaux, ailes, capes, effets"], ouvrir("cosmetiques")),
    ("teleportation", "minecraft:ender_pearl", (0, 3, 2, 3), "cyan", "VOYAGE", "TELEPORTS",
     "<aqua><b>Téléportation", ["<gray>Skyloft, arène, overworld…"], ouvrir("teleportation")),
    ("recompenses", "minecraft:chest", (5, 8, 2, 3), "vert", "KITS", "TOUTES 3H",
     "<green><b>Récompenses", ["<gray>Tes kits toutes les 3 heures"],
     {"son": {"type": "PLAYSOUND", "sound": SON_CLIC}, "kits": {"type": "COMMAND_PLAYER", "commands": ["kit"]}}),
]
for nom, item, z, coul, t, s, mm, lore, act in MENU:
    carte(im, z[0], z[1], z[2], z[3], coul, t, s)
    poser(g, nom, item, z, name=mm, lore=lore + ["", "<yellow>▶ Clic pour ouvrir"], click_actions=act)
tuile(im, 4, 3, "rouge")
poser(g, "fermer", "minecraft:barrier", 31, name="<red><b>Fermer", lore=[], click_actions={"f": {"type": "CLOSE_GUI"}})
IMAGES["menu"], GUIS["menu"] = im, g

# ---- Boutique (6 rangees)
im, g = fond(6, "BOUTIQUE"), base("", 6, ["boutique", "shop"])
etiquette(im, 0, 3, 0, "GRADES", "or")
etiquette(im, 5, 8, 0, "CLES", "cyan")
GRADES = [("dresseur", "cobblemon:great_ball", "vert", "green", "Dresseur", 5000),
          ("conseil4", "cobblemon:ultra_ball", "violet", "light_purple", "Conseil 4", 50000),
          ("champion", "cobblemon:master_ball", "or", "gold", "Champion", 250000)]
for i, (gid, item, coul, mm, nom, montant) in enumerate(GRADES):
    z = (0, 3, 1 + i, 1 + i)
    carte(im, *z, coul, nom.upper().replace(" ", ""), court(montant))
    poser(g, f"grade_{gid}_possede", item, z, priority=1, nbt=BRILLE,
          name=f"<{mm}><b>Grade {nom}", lore=[f"<gray>Débloque le kit {nom}", "", "<green>✔ Tu as ce grade"],
          view_requirements={"requirements": {"grade": {"type": "PERMISSION", "permission": f"group.{gid}"}}},
          click_actions={"son": {"type": "PLAYSOUND", "sound": SON_NON}})
    poser(g, f"grade_{gid}", item, z, priority=2, name=f"<{mm}><b>Grade {nom}",
          lore=[f"<gray>Débloque le kit {nom}", "<gray>Badge devant ton pseudo", "",
                f"<gray>Prix : <gold>{prix(montant)} CobbleDollars", "<yellow>▶ Clic pour acheter"],
          **achat(montant, [f"lp user %player% parent set {gid}", f"team join {gid} %player%"],
                  f"<green>Tu es maintenant <{mm}><b>{nom}</b><green> !", SON_OK,
                  {"pas_deja": {"type": "PERMISSION", "permission": f"group.{gid}", "comparison": "!="}},
                  f"<red>Il te faut {prix(montant)} CobbleDollars et ne pas déjà avoir ce grade (ou un grade supérieur).",
                  {"fermer": {"type": "CLOSE_GUI"}}))
CLES = [("cle_commune", "vert", "green", "Clé Commune", "COMMUNE", 500, 7001),
        ("cle_rare", "cyan", "aqua", "Clé Rare", "RARE", 2500, 7002),
        ("cle_legendaire", "or", "gold", "Clé Légendaire", "LEGENDE", 10000, 7003)]
for i, (cid, coul, mm, nom, court_nom, montant, cmd) in enumerate(CLES):
    z = (5, 8, 1 + i, 1 + i)
    carte(im, *z, coul, court_nom, court(montant))
    lot = montant * 9 // 2  # lot de 5 = -10 %
    req5 = {"argent": {"type": "CURRENCY", "currency": "", "amount": lot, "comparison": ">="}}
    act = achat(montant, [f"crates key give %player% {cid} 1"], f"<green>+1 {nom} !")
    for a in act["click_actions"].values():
        a["click"] = "LEFT_CLICK"
    act["click_actions"].update({
        "payer5": {"type": "CURRENCY_WITHDRAW", "currency": "", "amount": lot, "click": "RIGHT_CLICK", "requirements": {"requirements": req5}},
        "donner5": {"type": "COMMAND_CONSOLE", "commands": [f"crates key give %player% {cid} 5"], "click": "RIGHT_CLICK", "requirements": {"requirements": req5}},
        "msg5": {"type": "MESSAGE", "message": [f"<green>+5 {nom} !"], "click": "RIGHT_CLICK", "requirements": {"requirements": req5}},
        "son5": {"type": "PLAYSOUND", "sound": SON_ACHAT, "click": "RIGHT_CLICK"},
        "refresh5": {"type": "REFRESH_GUI", "click": "RIGHT_CLICK"}})
    poser(g, cid, "minecraft:tripwire_hook", z, custom_model_data=cmd, name=f"<{mm}><b>{nom}",
          lore=[f"<gray>Ouvre la {nom.replace('Clé', 'Caisse')}", f"<gray>Tu en as : <white>%skiescrates:keys {cid}%", "",
                f"<yellow>Clic gauche : <white>1 clé <gray>({prix(montant)} CD)",
                f"<yellow>Clic droit : <white>5 clés <gray>({prix(lot)} CD, <green>-10 %<gray>)"], **act)
etiquette(im, 0, 8, 4, "CLIC DROIT : 5 CLES -10%", "gris")
carte(im, 0, 2, 5, 5, "gris", "MENU")
poser(g, "retour", "minecraft:arrow", (0, 2, 5, 5), name="<gray><b>◀ Retour", lore=["<dark_gray>Revenir au menu"], click_actions=ouvrir("menu"))
tuile(im, 4, 5, "rouge")
poser(g, "fermer", "minecraft:barrier", 49, name="<red><b>Fermer", lore=[], click_actions={"f": {"type": "CLOSE_GUI"}})
carte(im, 6, 8, 5, 5, "violet", "STYLE")
poser(g, "vers_cosmetiques", "minecraft:amethyst_shard", (6, 8, 5, 5), name="<light_purple><b>Cosmétiques ▶",
      lore=["<gray>Voir les cosmétiques"], click_actions=ouvrir("cosmetiques"))
IMAGES["boutique_v2"], GUIS["boutique"] = im, g

# ---- Cosmetiques (6 rangees) : tuiles, achat puis /cosmetics pour equiper
im, g = fond(6, "COSMETIQUES"), base("", 6, ["cosmetiques", "cosmetique"])
COSMETIQUES = [  # id Dex Cosmetics (None = pas encore dessine), slot, icone, nom, description, prix, couleur
    (None, 11, "minecraft:red_dye", "Casquette de Dresseur", "", 0, "violet"),
    ("pikachu_hat", 12, "minecraft:yellow_dye", "Chapeau Pikachu", "Pika pika !", 4000, "violet"),
    (None, 13, "minecraft:carved_pumpkin", "Chapeau Citrouille", "", 0, "violet"),
    (None, 14, "minecraft:gold_ingot", "Couronne Céleste", "", 0, "violet"),
    (None, 15, "minecraft:black_dye", "Bandeau Team Rocket", "", 0, "violet"),
    (None, 28, "minecraft:red_banner", "Cape Sakuflemon", "", 0, "bleu"),
    ("giratina_arms", 29, "minecraft:obsidian", "Bras de Giratina", "La forme Originelle dans ton dos", 25000, "bleu"),
    (None, 30, "minecraft:feather", "Ailes Célestes", "", 0, "bleu"),
    ("effet_coeurs", 32, "minecraft:pink_dye", "Traînée de cœurs", "Des cœurs autour de toi", 5000, "rose"),
    ("effet_flammes", 33, "minecraft:blaze_powder", "Traînée de flammes", "Digne d'un Dracaufeu", 5000, "rose"),
    ("effet_notes", 34, "minecraft:note_block", "Notes de musique", "Ton thème de combat", 5000, "rose"),
    ("effet_etoiles", 41, "minecraft:nether_star", "Poussière d'étoiles", "Brille comme un shiny", 8000, "rose"),
    ("effet_eclairs", 42, "minecraft:lightning_rod", "Étincelles", "Électrique !", 8000, "rose"),
    ("glow_gold", 43, "minecraft:glowstone_dust", "Aura dorée", "Contour lumineux doré", 20000, "rose"),
]
etiquette(im, 0, 8, 0, "CHAPEAUX", "violet")
etiquette(im, 0, 3, 2, "DOS", "bleu")
etiquette(im, 5, 8, 2, "EFFETS", "rose")
for cid, slot, icone, nom, desc, montant, coul in COSMETIQUES:
    tuile(im, slot % 9, slot // 9, coul)
    if cid is None:
        poser(g, f"bientot_{slot}", icone, slot, name=f"<dark_gray><b>{nom}", lore=["<gray>Bientôt…"],
              click_actions={"son": {"type": "PLAYSOUND", "sound": SON_NON}})
        continue
    perm = f"sakuflemon.cosmetique.{cid}"
    poser(g, f"{cid}_possede", icone, slot, priority=1, nbt=BRILLE, name=f"<light_purple><b>{nom}",
          lore=[f"<gray>{desc}", "", "<green>✔ Possédé", "<yellow>▶ Clic pour l'équiper"],
          view_requirements={"requirements": {"possede": {"type": "PERMISSION", "permission": perm}}},
          click_actions={"son": {"type": "PLAYSOUND", "sound": SON_CLIC},
                         "equiper": {"type": "COMMAND_PLAYER", "commands": ["cosmetics"]}})
    poser(g, cid, icone, slot, priority=2, name=f"<light_purple><b>{nom}",
          lore=[f"<gray>{desc}", "", f"<gray>Prix : <gold>{prix(montant)} CobbleDollars", "<yellow>▶ Clic pour acheter"],
          **achat(montant, [f"cosmetics give %player% {cid}", f"lp user %player% permission set {perm} true"],
                  f"<green>Tu as débloqué <light_purple><b>{nom}</b><green> ! Équipe-le avec /cosmetics.", SON_OK))
carte(im, 0, 2, 5, 5, "gris", "MENU")
poser(g, "retour", "minecraft:arrow", (0, 2, 5, 5), name="<gray><b>◀ Retour", lore=["<dark_gray>Revenir au menu"], click_actions=ouvrir("menu"))
carte(im, 3, 5, 5, 5, "vert", "TENUE")
poser(g, "equiper", "minecraft:armor_stand", (3, 5, 5, 5), name="<green><b>Mes cosmétiques",
      lore=["<gray>Équiper ou retirer ce que tu possèdes", "", "<yellow>▶ Clic pour ouvrir"],
      click_actions={"son": {"type": "PLAYSOUND", "sound": SON_CLIC}, "o": {"type": "COMMAND_PLAYER", "commands": ["cosmetics"]}})
carte(im, 6, 8, 5, 5, "or", "SHOP")
poser(g, "vers_boutique", "minecraft:gold_ingot", (6, 8, 5, 5), name="<gold><b>Boutique ▶", lore=["<gray>Grades et clés"], click_actions=ouvrir("boutique"))
IMAGES["cosmetiques"], GUIS["cosmetiques"] = im, g

# ---- Teleportation (5 rangees)
im, g = fond(5, "TELEPORTATION"), base("", 5, ["tp", "teleportation", "warps"])


def tp(f):
    return {"tp": {"type": "COMMAND_CONSOLE", "commands": [f"execute as %player% run function sakuflemon:tp/{f}"]},
            "fermer": {"type": "CLOSE_GUI"}}


DEST = [("skyloft", "minecraft:white_wool", (0, 3, 0, 1), "cyan", "SKYLOFT", "LA CAPITALE",
         "<aqua><b>Skyloft", ["<gray>La capitale d'Incarnam"]),
        ("arene", "minecraft:bell", (5, 8, 0, 1), "or", "ARENE", "LE CHAMPION",
         "<gold><b>Arène Céleste", ["<gray>Défie le Champion Céleste"]),
        ("monde", "minecraft:grass_block", (0, 3, 2, 3), "vert", "PLONGEON", "OVERWORLD",
         "<green><b>Terre ferme", ["<gray>Plonge vers l'overworld", "<dark_gray>Débloqué par la quête des ailes"]),
        ("aleatoire", "minecraft:compass", (5, 8, 2, 3), "bleu", "EXPLORER", "AU HASARD",
         "<blue><b>Exploration", ["<gray>Un endroit au hasard dans l'overworld", "<dark_gray>Débloqué par la quête des ailes"])]
for f, item, z, coul, t, s, mm, lore in DEST:
    carte(im, *z, coul, t, s)
    poser(g, f, item, z, name=mm, lore=lore + ["", "<yellow>▶ Clic pour y aller"], click_actions=tp(f))
carte(im, 0, 2, 4, 4, "gris", "MENU")
poser(g, "retour", "minecraft:arrow", (0, 2, 4, 4), name="<gray><b>◀ Retour", lore=["<dark_gray>Revenir au menu"], click_actions=ouvrir("menu"))
for c, item, nom in [(5, "minecraft:netherrack", "Nether"), (6, "minecraft:end_stone", "End"), (7, "minecraft:tall_grass", "Zone Safari")]:
    tuile(im, c, 4, "gris")
    poser(g, nom.lower().replace(" ", "_"), item, 36 + c, name=f"<dark_gray><b>{nom}", lore=["<gray>Bientôt…"],
          click_actions={"son": {"type": "PLAYSOUND", "sound": SON_NON}})
IMAGES["teleportation"], GUIS["teleportation"] = im, g

GLYPHES = {"menu": "", "boutique_v2": "", "cosmetiques": "", "teleportation": ""}

if __name__ == "__main__":
    assets = sys.argv[1]
    s = os.path.join(assets, "sakuflemon")
    os.makedirs(os.path.join(s, "textures/font/gui"), exist_ok=True)
    providers = [{"type": "space", "advances": {"": -8, "": -177}},
                 {"type": "bitmap", "file": "sakuflemon:font/gui/boutique.png", "ascent": 13, "height": 204, "chars": [""]}]
    Image.open(os.path.join(ICI, "boutique_v1.png")).save(os.path.join(s, "textures/font/gui/boutique.png"))
    for nom, im in IMAGES.items():
        im.save(os.path.join(s, f"textures/font/gui/{nom}.png"))
        providers.append({"type": "bitmap", "file": f"sakuflemon:font/gui/{nom}.png", "ascent": 13,
                          "height": im.size[1], "chars": [GLYPHES[nom]]})
    os.makedirs(os.path.join(s, "font"), exist_ok=True)
    json.dump({"providers": providers}, open(os.path.join(s, "font/gui.json"), "w"))
    # objet invisible des cartes + icone de l'objet Menu
    os.makedirs(os.path.join(s, "textures/item"), exist_ok=True)
    os.makedirs(os.path.join(s, "models/item"), exist_ok=True)
    Image.new("RGBA", (16, 16), (0, 0, 0, 0)).save(os.path.join(s, "textures/item/vide.png"))
    json.dump({"parent": "minecraft:item/generated", "textures": {"layer0": "sakuflemon:item/vide"}},
              open(os.path.join(s, "models/item/vide.json"), "w"))
    m = os.path.join(assets, "minecraft/models/item")
    os.makedirs(m, exist_ok=True)
    json.dump({"parent": "minecraft:item/generated", "textures": {"layer0": "minecraft:item/structure_void"},
               "overrides": [{"predicate": {"custom_model_data": 7020}, "model": "sakuflemon:item/vide"}]},
              open(os.path.join(m, "structure_void.json"), "w"))
    json.dump({"parent": "minecraft:item/handheld_rod", "textures": {"layer0": "minecraft:item/carrot_on_a_stick"},
               "overrides": [{"predicate": {"custom_model_data": 7010}, "model": "sakuflemon:item/menu"}]},
              open(os.path.join(m, "carrot_on_a_stick.json"), "w"))
    json.dump({"parent": "minecraft:item/handheld", "textures": {"layer0": "sakuflemon:item/menu"}},
              open(os.path.join(s, "models/item/menu.json"), "w"))
    G = ["................", ".....######.....", "...##RRRRRR##...", "..#RRRRRRRRRR#..", "..#RRRYYRRRRR#..",
         ".#RRRYYYYRRRRR#.", ".#RRRRYYRRRRRR#.", ".######WW######.", ".#####W..W#####.", ".#WWWWW..WWWWW#.",
         ".#WWWWWWWWWWWW#.", "..#WWWWWWWWWW#..", "..#WWWWWWWWWW#..", "...##WWWWWW##...", ".....######.....", "................"]
    C = {"#": (30, 30, 35, 255), "R": (210, 45, 45, 255), "W": (240, 240, 245, 255), "Y": (255, 215, 80, 255), ".": (0, 0, 0, 0)}
    ic = Image.new("RGBA", (16, 16))
    for y, l in enumerate(G):
        for x, c in enumerate(l):
            ic.putpixel((x, y), C[c])
    ic.save(os.path.join(s, "textures/item/menu.png"))
    os.makedirs(os.path.join(ICI, "guis"), exist_ok=True)
    for nom, gui in GUIS.items():
        json.dump(gui, open(os.path.join(ICI, "guis", nom + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("ok", list(IMAGES), list(GUIS))
