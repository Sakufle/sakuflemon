#!/usr/bin/env python3
"""Génère les chapitres « Aventure » (Pokédex, 18 types, Shiny, Dresseur) et les
tables de récompenses. À lancer depuis serveur/ftbquests : python3 outils/generer_aventure.py
Les IDs sont dérivés d'un nom (stables entre deux générations) et restent < 0x8000000000000000
(FTB Quests refuse sinon les IDs en commande)."""
import hashlib, os, re

Q = os.path.join(os.path.dirname(__file__), "..", "quests")
FIN_INCARNAM = "0305BC51DE70A11D"
lang = {}

def nid(name):
    return "%016X" % (int(hashlib.sha1(name.encode()).hexdigest()[:16], 16) & 0x7FFFFFFFFFFFFFFF)

def s(v):
    return '"' + v.replace('\\', '\\\\').replace('"', '\\"') + '"'

def ctask(key, action, amount, **kw):
    f = dict(pokemon="", pokemon_type="", form="", aspects="", biome="", dimension="", gender="",
             poke_ball_used="", region="", natures="", trainers="", moves="", held_items="",
             raid_tiers="", abilities="", dex_progress="", targetPlayer="")
    f.update({k: v for k, v in kw.items() if k in f})
    shiny = kw.get("shiny", False)
    lines = [f'id: "{nid(key)}"', 'type: "cobblemon_quests:cobblemon_task"', f'action: "{action}"',
             f"amount: {amount}L", f"shiny: {'true' if shiny else 'false'}"]
    lines += [f"{k}: {s(v)}" for k, v in f.items()]
    lines += ["min_level: 0", "max_level: 0", "max_turns: 0", "time_min: 0L", "time_max: 0L"]
    return lines

def r_cmd(key, cmd, title, icon="cobblemon:relic_coin"):
    lang[f"reward.{nid(key)}.title"] = title
    return [f'id: "{nid(key)}"', 'type: "command"', f"command: {s(cmd)}", "player_command: false",
            "silent: true", f'icon: "{icon}"']

def r_cd(key, n):
    return r_cmd(key, f"/cobbledollars give {{p}} {n}", f"{n} CobbleDollars")

def r_key(key, cle, nom, n=1):
    return r_cmd(key, f"/crates key give {{p}} {cle} {n}", f"{n} {nom}", "minecraft:tripwire_hook")

def r_item(key, item, count):
    return [f'id: "{nid(key)}"', 'type: "item"', f'item: {{ count: {count}, id: "{item}" }}', "count: 1"]

def r_rand(key, table):
    return [f'id: "{nid(key)}"', 'type: "random"', f"table_id: {int(nid(table), 16)}L"]

def block(lines, ind):
    t = "\t" * ind
    return t + "{\n" + "".join(t + "\t" + l + "\n" for l in lines) + t + "}"

def icone(icon):
    """tera:<type> = icône de type Mega Showdown ; sk:<nom> = icône maison du pack sakuflemon-interface."""
    if icon.startswith("tera:"):
        tex = f"mega_showdown:textures/gui/summary/tera_types/{icon[5:]}.png"
    elif icon.startswith("sk:"):
        tex = f"sakuflemon:textures/quetes/{icon[3:]}.png"
    else:
        return f'"{icon}"'
    return '{ id: "ftbquests:custom_icon", components: { "ftbquests:icon": "%s" } }' % tex

def quest(key, x, y, icon, title, sub, desc, tasks, rewards, deps=(), shape="circle", size=None):
    qid = nid(key)
    lang[f"quest.{qid}.title"] = title
    if sub: lang[f"quest.{qid}.quest_subtitle"] = sub
    if desc: lang[f"quest.{qid}.quest_desc"] = desc
    ic = icone(icon)
    out = [f'id: "{qid}"', f"icon: {ic}", f"x: {x:.1f}d", f"y: {y:.1f}d", f'shape: "{shape}"']
    if size: out.append(f"size: {size:.1f}d")
    out.append("dependencies: [" + " ".join(f'"{d}"' for d in deps) + "]")
    body = "\n".join(out) + "\n"
    tl = []
    for tkey, ttitle, tlines in tasks:
        lang[f"task.{nid(tkey)}.title"] = ttitle
        tl.append(block(tlines, 4))
    rl = [block(r, 4) for r in rewards]
    return (out, tl, rl)

def write_chapter(fname, key, order, icon, title, sub, quests):
    cid = nid(key)
    lang[f"chapter.{cid}.title"] = title
    lang[f"chapter.{cid}.chapter_subtitle"] = [sub]
    parts = []
    for out, tl, rl in quests:
        q = "\t\t{\n" + "".join(f"\t\t\t{l}\n" for l in out)
        q += "\t\t\ttasks: [\n" + "\n".join(tl) + "\n\t\t\t]\n"
        q += "\t\t\trewards: [\n" + "\n".join(rl) + "\n\t\t\t]\n\t\t}"
        parts.append(q)
    txt = ("{\n" f'\tid: "{cid}"\n\tgroup: ""\n\torder_index: {order}\n\tfilename: "{fname}"\n'
           f'\ticon: {icone(icon)}\n\tdefault_quest_shape: ""\n\tdefault_hide_dependency_lines: false\n'
           "\tquests: [\n" + "\n".join(parts) + "\n\t]\n}\n")
    open(os.path.join(Q, "chapters", fname + ".snbt"), "w").write(txt)

# ---------- Tables de récompenses ----------
def table(key, title, order, entries):
    tid = nid(key)
    lang[f"reward_table.{tid}.title"] = title
    rs = []
    for i, (w, r) in enumerate(entries):
        rs.append(block(r + [f"weight: {w:.1f}f"], 2))
    txt = "{\n" f'\tid: "{tid}"\n\tloot_size: 1\n\torder_index: {order}\n\trewards: [\n' + "\n".join(rs) + "\n\t]\n}\n"
    os.makedirs(os.path.join(Q, "reward_tables"), exist_ok=True)
    open(os.path.join(Q, "reward_tables", tid + ".snbt"), "w").write(txt)

table("table_commune", "Butin commun", 0, [
    (30, r_item("tc1", "cobblemon:great_ball", 5)), (25, r_item("tc2", "cobblemon:super_potion", 4)),
    (20, r_item("tc3", "cobblemon:rare_candy", 1)), (15, r_cd("tc4", 300)),
    (10, r_key("tc5", "cle_commune", "Clé commune"))])
table("table_rare", "Butin rare", 1, [
    (30, r_item("tr1", "cobblemon:ultra_ball", 5)), (25, r_item("tr2", "cobblemon:rare_candy", 3)),
    (20, r_item("tr3", "cobblemon:hyper_potion", 5)), (15, r_key("tr4", "cle_commune", "Clés communes", 2)),
    (10, r_key("tr5", "cle_rare", "Clé rare"))])
table("table_legendaire", "Butin légendaire", 2, [
    (35, r_key("tl1", "cle_rare", "Clés rares", 2)), (30, r_item("tl2", "cobblemon:ability_capsule", 1)),
    (25, r_key("tl3", "cle_legendaire", "Clé légendaire")), (10, r_item("tl4", "cobblemon:master_ball", 1))])
T_COM, T_RARE, T_LEG = "table_commune", "table_rare", "table_legendaire"

# ---------- Chapitre Pokédex ----------
qs, prev = [], [FIN_INCARNAM]
paliers = [(10, 300, T_COM), (25, 600, T_COM), (50, 1000, T_RARE), (100, 2000, T_RARE),
           (200, 4000, T_LEG), (400, 8000, T_LEG)]
for i, (n, cd, tb) in enumerate(paliers):
    k = f"dex_{n}"
    dex = ["red", "yellow", "green", "blue", "pink", "black"][i]
    qs.append(quest(k, i * 2, 0, f"cobblemon:pokedex_{dex}", f"{n} espèces", "Complète ton Pokédex",
        [f"Capture {n} espèces différentes.", "Chaque espèce ne compte qu'une fois, peu importe sa forme."],
        [(k + "_t", f"Avoir capturé {n} espèces", ctask(k + "_t", "have_registered", n, dex_progress="caught"))],
        [r_cd(k + "_cd", cd), r_rand(k + "_r", tb)], deps=prev, size=1.5 if n >= 200 else None))
    prev = [nid(k)]
write_chapter("pokedex", "chap_pokedex", 1, "sk:pokedex", "Pokédex", "Deviens un vrai collectionneur", qs)

# ---------- Chapitre 18 types ----------
TYPES = [("normal", "Normal", "cobblemon:silk_scarf"), ("fire", "Feu", "cobblemon:fire_stone"),
 ("water", "Eau", "cobblemon:water_stone"), ("grass", "Plante", "cobblemon:leaf_stone"),
 ("electric", "Électrik", "cobblemon:thunder_stone"), ("ice", "Glace", "cobblemon:ice_stone"),
 ("fighting", "Combat", "cobblemon:muscle_band"), ("poison", "Poison", "cobblemon:poison_barb"),
 ("ground", "Sol", "cobblemon:soft_sand"), ("flying", "Vol", "cobblemon:sharp_beak"),
 ("psychic", "Psy", "cobblemon:twisted_spoon"), ("bug", "Insecte", "cobblemon:silver_powder"),
 ("rock", "Roche", "cobblemon:hard_stone"), ("ghost", "Spectre", "cobblemon:spell_tag"),
 ("dragon", "Dragon", "cobblemon:dragon_fang"), ("dark", "Ténèbres", "cobblemon:black_glasses"),
 ("steel", "Acier", "cobblemon:metal_coat"), ("fairy", "Fée", "minecraft:pink_dye")]
qs, ids = [], []
for i, (t, fr, icon) in enumerate(TYPES):
    k = f"type_{t}"
    qs.append(quest(k, (i % 6) * 1.5, (i // 6) * 1.5, f"tera:{t}", f"Type {fr}", None,
        [f"Capture 5 Pokémon de type {fr}."],
        [(k + "_t", f"Capturer 5 Pokémon {fr}", ctask(k + "_t", "catch", 5, pokemon_type=t))],
        [r_cd(k + "_cd", 250)], deps=[FIN_INCARNAM]))
    ids.append(nid(k))
qs.append(quest("type_maitre", 3.75, 5.0, "cobblemon:master_ball", "Maître des types", "Les 18 types",
    ["Tu as dompté les 18 types. Arceus, le Pokémon aux mille plaques, te salue."],
    [("type_maitre_t", "Terminer les 18 types", ["id: \"%s\"" % nid("type_maitre_t"), 'type: "checkmark"'])],
    [r_cd("type_maitre_cd", 5000), r_key("type_maitre_k", "cle_legendaire", "Clé légendaire")],
    deps=ids, shape="hexagon", size=2.0))
write_chapter("dix_huit_types", "chap_types", 2, "sk:types", "Les 18 types", "Capture-les tous, type par type", qs)

# ---------- Chapitre Shiny ----------
qs, prev = [], [FIN_INCARNAM]
for i, (n, rewards) in enumerate([
        (1, lambda k: [r_cd(k + "_cd", 1000), r_key(k + "_k", "cle_commune", "Clé commune")]),
        (5, lambda k: [r_cd(k + "_cd", 3000), r_key(k + "_k", "cle_rare", "Clé rare")]),
        (10, lambda k: [r_cd(k + "_cd", 6000), r_rand(k + "_r", T_LEG)]),
        (25, lambda k: [r_cd(k + "_cd", 15000), r_key(k + "_k", "cle_legendaire", "Clés légendaires", 2)]),
        (50, lambda k: [r_cd(k + "_cd", 30000), r_item(k + "_mb", "cobblemon:master_ball", 1)])]):
    k = f"shiny_{n}"
    qs.append(quest(k, i * 2, 0, "minecraft:nether_star", f"{n} shiny" if n > 1 else "Premier shiny",
        "Chasseur de chromatiques", [f"Capture {n} Pokémon chromatique{'s' if n > 1 else ''}."],
        [(k + "_t", f"Capturer {n} shiny", ctask(k + "_t", "catch", n, shiny=True))],
        rewards(k), deps=prev, size=1.5 if n >= 25 else None))
    prev = [nid(k)]
write_chapter("shiny", "chap_shiny", 3, "sk:shiny", "Chasseur de shiny", "Les Pokémon aux couleurs rares", qs)

# ---------- Chapitre Dresseur ----------
LIGNES = [
 ("combat", "cobblemon:muscle_band", "Combats sauvages", "Mettre K.O. {n} Pokémon sauvages", "defeat", [(25, 300, T_COM), (100, 1000, T_RARE), (500, 4000, T_LEG)]),
 ("dresseurs", "cobblemon:black_belt", "Duels de dresseurs", "Battre {n} dresseurs PNJ", "defeat_npc", [(5, 500, T_COM), (20, 2000, T_RARE), (50, 5000, T_LEG)]),
 ("evolution", "cobblemon:everstone", "Évolutions", "Faire évoluer {n} Pokémon", "evolve", [(5, 400, T_COM), (25, 1500, T_RARE), (100, 5000, T_LEG)]),
 ("peche", "cobblemon:poke_rod", "Pêche", "Pêcher {n} Pokémon", "reel", [(10, 300, T_COM), (50, 1500, T_RARE), (200, 4000, T_LEG)]),
 ("fossile", "cobblemon:fossil_analyzer", "Paléontologue", "Ressusciter {n} fossiles", "revive_fossil", [(1, 500, T_COM), (5, 2000, T_RARE), (15, 5000, T_LEG)]),
]
qs = []
for row, (code, icon, nom, txt, action, steps) in enumerate(LIGNES):
    prev = [FIN_INCARNAM]
    for col, (n, cd, tb) in enumerate(steps):
        k = f"{code}_{n}"
        qs.append(quest(k, col * 2, row * 1.5, icon, f"{nom} {['I','II','III'][col]}", None,
            [txt.format(n=n) + "."],
            [(k + "_t", txt.format(n=n), ctask(k + "_t", action, n))],
            [r_cd(k + "_cd", cd), r_rand(k + "_r", tb)], deps=prev))
        prev = [nid(k)]
write_chapter("dresseur", "chap_dresseur", 4, "sk:dresseur", "Carrière de dresseur", "Combats, évolutions, pêche et fossiles", qs)

# ---------- Lang : remplace le bloc généré dans en_us.snbt ----------
p = os.path.join(Q, "lang", "en_us.snbt")
t = open(p).read()
# retire les anciennes entrées générées (mêmes clés), sans commentaire : le SNBT n'en accepte pas
entries = re.findall(r'\t"[^"]+": (?:\[\n(?:\t\t.*\n)*?\t\]|.*)\n', t)
gen = set(lang)
kept = [e for e in entries if re.match(r'\t"([^"]+)"', e).group(1) not in gen]
lines = []
for k, v in lang.items():
    if isinstance(v, list):
        lines.append(f"\t{s(k)}: [\n" + "".join(f"\t\t{s(x)}\n" for x in v) + "\t]\n")
    else:
        lines.append(f"\t{s(k)}: {s(v)}\n")
t = "{\n" + "".join(kept) + "".join(lines) + "}\n"
open(p, "w").write(t)
print(len(lang), "textes")
