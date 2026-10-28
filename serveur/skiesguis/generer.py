"""Menus SkiesGUIs de Sakuflemon (config/skiesguis/guis/*.json sur le serveur).

Les achats reprennent a l'identique les commandes de la boutique v1
(lp parent set + team join, crates key give). Fonds : glyphes de la police
sakuflemon:gui (voir serveur/interface/generer_gui.py).

Usage : python3 generer.py  -> ecrit guis/menu.json, boutique.json, cosmetiques.json, teleportation.json
"""
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))
SON_OK = "minecraft:ui.toast.challenge_complete"
SON_ACHAT = "minecraft:entity.experience_orb.pickup"
SON_NON = "minecraft:block.note_block.bass"
SON_CLIC = "minecraft:ui.button.click"


def titre(glyphe):
    return f"<white><font:sakuflemon:gui>{glyphe}</font>"


def base(glyphe, rangees, alias):
    return {
        "title": titre(glyphe),
        "size": rangees,
        "alias_commands": alias,
        "open_actions": {"son": {"type": "PLAYSOUND", "sound": "cobblemon:pc.on"}},
        "close_actions": {"son": {"type": "PLAYSOUND", "sound": "cobblemon:pc.off"}},
        "items": {},
    }


def prix(n):
    return f"{n:,}".replace(",", " ")


def ouvrir(gui):
    return {"son": {"type": "PLAYSOUND", "sound": SON_CLIC},
            "ouvrir": {"type": "OPEN_GUI", "id": gui}}


def bouton(item, slot, nom, lore, actions, **extra):
    d = {"item": item, "slots": [slot], "name": nom, "lore": lore,
         "nbt": {"minecraft:hide_additional_tooltip": {}}, "click_actions": actions}
    d.update(extra)
    return d


def achat(slot, item, nom, lore, montant, commandes, message, son=SON_ACHAT,
          conditions=None, refus=None, fin=None, **extra):
    req = {"argent": {"type": "CURRENCY", "currency": "", "amount": montant, "comparison": ">="}}
    req.update(conditions or {})
    actions = {
        "payer": {"type": "CURRENCY_WITHDRAW", "currency": "", "amount": montant},
        "donner": {"type": "COMMAND_CONSOLE", "commands": commandes},
        "msg": {"type": "MESSAGE", "message": [message]},
        "son": {"type": "PLAYSOUND", "sound": son},
    }
    actions.update(fin or {"refresh": {"type": "REFRESH_GUI"}})
    d = {
        "item": item, "slots": [slot], "name": nom,
        "lore": lore + ["", f"<gray>Prix : <gold>{prix(montant)} CobbleDollars", "<yellow>▶ Clic pour acheter"],
        "nbt": {"minecraft:hide_additional_tooltip": {}},
        "click_requirements": {
            "requirements": req,
            "deny_actions": {
                "msg": {"type": "MESSAGE", "message": [refus or f"<red>Il te faut {prix(montant)} CobbleDollars."]},
                "son": {"type": "PLAYSOUND", "sound": SON_NON},
            },
        },
        "click_actions": actions,
    }
    d.update(extra)
    return d


def retour(slot, gui="menu"):
    return bouton("minecraft:arrow", slot, "<gray><b>◀ Retour", ["<dark_gray>Revenir au menu"], ouvrir(gui))


# ---------------------------------------------------------------- menu
menu = base("", 3, ["menu", "m"])
menu["items"] = {
    "boutique": bouton("minecraft:gold_ingot", 10, "<gold><b>Boutique",
                       ["<gray>Grades et clés de caisses", "", "<yellow>▶ Ouvrir"], ouvrir("boutique")),
    "cosmetiques": bouton("minecraft:amethyst_shard", 12, "<light_purple><b>Cosmétiques",
                          ["<gray>Chapeaux, ailes, capes, effets", "", "<yellow>▶ Ouvrir"], ouvrir("cosmetiques")),
    "teleportation": bouton("minecraft:ender_pearl", 14, "<aqua><b>Téléportation",
                            ["<gray>Skyloft, arène, overworld…", "", "<yellow>▶ Ouvrir"], ouvrir("teleportation")),
    "recompenses": bouton("minecraft:chest", 16, "<green><b>Récompenses",
                          ["<gray>Tes kits toutes les 3 h", "", "<yellow>▶ Ouvrir"],
                          {"son": {"type": "PLAYSOUND", "sound": SON_CLIC},
                           "kits": {"type": "COMMAND_PLAYER", "commands": ["kit"]}}),
    "fermer": bouton("minecraft:barrier", 22, "<red><b>Fermer", [], {"fermer": {"type": "CLOSE_GUI"}}),
}

# ---------------------------------------------------------------- boutique
boutique = base("", 6, ["boutique", "shop"])
it = boutique["items"]
GRADES = [  # id, slot, item, couleur, nom, prix
    ("dresseur", 11, "cobblemon:great_ball", "green", "Dresseur", 5000),
    ("conseil4", 13, "cobblemon:ultra_ball", "light_purple", "Conseil 4", 50000),
    ("champion", 15, "cobblemon:master_ball", "gold", "Champion", 250000),
]
for gid, slot, item, coul, nom, montant in GRADES:
    it[f"grade_{gid}_possede"] = bouton(
        item, slot, f"<{coul}><b>Grade {nom}", ["<gray>Débloque le kit " + nom, "", "<green>✔ Tu as ce grade"],
        {"son": {"type": "PLAYSOUND", "sound": SON_NON}}, priority=1,
        view_requirements={"requirements": {"grade": {"type": "PERMISSION", "permission": f"group.{gid}"}}},
        nbt={"minecraft:hide_additional_tooltip": {}, "minecraft:enchantment_glint_override": True})
    it[f"grade_{gid}"] = achat(
        slot, item, f"<{coul}><b>Grade {nom}", ["<gray>Débloque le kit " + nom, "<gray>Badge devant ton pseudo"],
        montant, [f"lp user %player% parent set {gid}", f"team join {gid} %player%"],
        f"<green>Tu es maintenant <{coul}><b>{nom}</b><green> !", son=SON_OK, priority=2,
        conditions={"pas_deja": {"type": "PERMISSION", "permission": f"group.{gid}", "comparison": "!="}},
        refus=f"<red>Il te faut {prix(montant)} CobbleDollars et ne pas déjà avoir ce grade (ou un grade supérieur).",
        fin={"fermer": {"type": "CLOSE_GUI"}})

CLES = [  # id, colonne, couleur, nom, prix, custom_model_data
    ("cle_commune", 2, "green", "Clé Commune", 500, 7001),
    ("cle_rare", 4, "aqua", "Clé Rare", 2500, 7002),
    ("cle_legendaire", 6, "gold", "Clé Légendaire", 10000, 7003),
]
for cid, col, coul, nom, montant, cmd in CLES:
    caisse = nom.replace("Clé", "Caisse")
    possede = f"<gray>Tu en as : <white>%skiescrates:keys {cid}%"
    for qte, rang, total in [(1, 3, montant), (5, 4, montant * 9 // 2)]:  # lot de 5 = -10 %
        lore = [f"<gray>Ouvre la {caisse}", possede]
        if qte == 5:
            lore.insert(1, "<green>Lot de 5 : -10 %")
        it[f"{cid}_x{qte}"] = achat(
            rang * 9 + col, "minecraft:tripwire_hook", f"<{coul}><b>{nom}" + (" x5" if qte == 5 else ""),
            lore, total, [f"crates key give %player% {cid} {qte}"], f"<green>+{qte} {nom} !",
            custom_model_data=cmd, amount=qte)
it["retour"] = retour(45)
it["fermer"] = bouton("minecraft:barrier", 49, "<red><b>Fermer", [], {"fermer": {"type": "CLOSE_GUI"}})
it["vers_cosmetiques"] = bouton("minecraft:amethyst_shard", 53, "<light_purple><b>Cosmétiques ▶",
                                ["<gray>Voir les cosmétiques"], ouvrir("cosmetiques"))

# ---------------------------------------------------------------- cosmetiques (Dex Cosmetics)
cosm = base("", 6, ["cosmetiques", "cosmetique"])
it = cosm["items"]
COSMETIQUES = [  # id Dex Cosmetics, slot, icone, nom, description, prix
    ("casquette_dresseur", 11, "minecraft:red_dye", "Casquette de Dresseur", "La casquette rouge et blanche", 3000),
    ("oreilles_pikachu", 12, "minecraft:yellow_dye", "Oreilles de Pikachu", "Pika pika !", 4000),
    ("chapeau_citrouille", 13, "minecraft:carved_pumpkin", "Chapeau Citrouille", "Souvenir de l'île Citrouille", 4000),
    ("couronne_celeste", 14, "minecraft:gold_ingot", "Couronne Céleste", "Pour les rois du ciel", 15000),
    ("bandeau_rocket", 15, "minecraft:black_dye", "Bandeau Team Rocket", "Prépare-toi à des ennuis…", 6000),
    ("cape_sakuflemon", 28, "minecraft:red_banner", "Cape Sakuflemon", "La cape officielle du serveur", 7500),
    ("sac_pokeball", 29, "cobblemon:poke_ball", "Sac Poké Ball", "Un sac en forme de Poké Ball", 7500),
    ("ailes_celestes", 30, "minecraft:feather", "Ailes Célestes", "Les ailes des habitants d'Incarnam", 25000),
    ("effet_coeurs", 32, "minecraft:pink_dye", "Traînée de cœurs", "Des cœurs autour de toi", 5000),
    ("effet_flammes", 33, "minecraft:blaze_powder", "Traînée de flammes", "Digne d'un Dracaufeu", 5000),
    ("effet_notes", 34, "minecraft:note_block", "Notes de musique", "Ton thème de combat", 5000),
    ("effet_etoiles", 41, "minecraft:nether_star", "Poussière d'étoiles", "Brille comme un shiny", 8000),
    ("effet_eclairs", 42, "minecraft:lightning_rod", "Étincelles", "Électrique !", 8000),
    ("aura_doree", 43, "minecraft:glowstone_dust", "Aura dorée", "Contour lumineux doré", 20000),
]
for cid, slot, icone, nom, desc, montant in COSMETIQUES:
    perm = f"sakuflemon.cosmetique.{cid}"
    it[f"{cid}_possede"] = bouton(
        icone, slot, f"<light_purple><b>{nom}", [f"<gray>{desc}", "", "<green>✔ Possédé", "<yellow>▶ Clic pour l'équiper"],
        {"son": {"type": "PLAYSOUND", "sound": SON_CLIC},
         "equiper": {"type": "COMMAND_PLAYER", "commands": ["cosmetics"]}}, priority=1,
        view_requirements={"requirements": {"possede": {"type": "PERMISSION", "permission": perm}}},
        nbt={"minecraft:hide_additional_tooltip": {}, "minecraft:enchantment_glint_override": True})
    it[cid] = achat(
        slot, icone, f"<light_purple><b>{nom}", [f"<gray>{desc}"], montant,
        [f"cosmetics give %player% {cid}", f"lp user %player% permission set {perm} true"],
        f"<green>Tu as débloqué <light_purple><b>{nom}</b><green> ! Équipe-le avec /cosmetics.", son=SON_OK, priority=2)
it["retour"] = retour(45)
it["equiper"] = bouton("minecraft:armor_stand", 49, "<green><b>Mes cosmétiques",
                       ["<gray>Équiper ou retirer", "<gray>ce que tu possèdes", "", "<yellow>▶ Ouvrir"],
                       {"son": {"type": "PLAYSOUND", "sound": SON_CLIC},
                        "ouvrir": {"type": "COMMAND_PLAYER", "commands": ["cosmetics"]}})
it["vers_boutique"] = bouton("minecraft:gold_ingot", 53, "<gold><b>Boutique ▶", ["<gray>Grades et clés"], ouvrir("boutique"))

# ---------------------------------------------------------------- teleportation
tp = base("", 4, ["tp", "teleportation", "warps"])
it = tp["items"]


def dest(slot, item, nom, lore, fonction):
    return bouton(item, slot, nom, lore + ["", "<yellow>▶ Clic pour y aller"],
                  {"tp": {"type": "COMMAND_CONSOLE", "commands": [f"execute as %player% run function sakuflemon:tp/{fonction}"]},
                   "fermer": {"type": "CLOSE_GUI"}})


it["skyloft"] = dest(10, "minecraft:white_wool", "<aqua><b>Skyloft", ["<gray>La capitale d'Incarnam", "<gray>(Grande Place)"], "skyloft")
it["arene"] = dest(12, "minecraft:bell", "<gold><b>Arène Céleste", ["<gray>Défie le Champion Céleste"], "arene")
it["overworld"] = dest(14, "minecraft:grass_block", "<green><b>Terre ferme",
                       ["<gray>Plonge vers l'overworld", "<dark_gray>Débloqué par la quête des ailes"], "monde")
it["aleatoire"] = dest(16, "minecraft:compass", "<blue><b>Exploration",
                       ["<gray>Un endroit au hasard", "<gray>dans l'overworld", "<dark_gray>Débloqué par la quête des ailes"], "aleatoire")
for slot, item, nom in [(20, "minecraft:netherrack", "Nether"), (22, "minecraft:end_stone", "End"),
                        (24, "minecraft:tall_grass", "Zone Safari")]:
    it[nom.lower().replace(" ", "_")] = bouton(item, slot, f"<dark_gray><b>{nom}", ["<gray>Bientôt…"],
                                                {"son": {"type": "PLAYSOUND", "sound": SON_NON}})
it["retour"] = retour(27)

if __name__ == "__main__":
    os.makedirs(os.path.join(ICI, "guis"), exist_ok=True)
    for nom, gui in [("menu", menu), ("boutique", boutique), ("cosmetiques", cosm), ("teleportation", tp)]:
        with open(os.path.join(ICI, "guis", nom + ".json"), "w", encoding="utf-8") as f:
            json.dump(gui, f, ensure_ascii=False, indent=2)
    print("ok")
