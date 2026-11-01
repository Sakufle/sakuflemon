# -*- coding: utf-8 -*-
"""Génère les 12 chapitres de quêtes "mods" de Sakuflemon (FTB Quests 2101 + Cobblemon Quests Reloaded).
Usage : python quetes_mods.py <dossier quests existant> <dossier sortie>
Copie le dossier quests existant, ajoute les chapitres et fusionne lang/en_us.snbt.
Les ID FTB sont dérivés d'un hash de la clé de chaque quête : relancer le script garde la progression des joueurs."""
import hashlib, os, shutil, sys

TABLES = {"c": 8651459768004125577, "r": 4154057608299291355, "l": 7961691238798267049}
TABLE_NOM = {"c": "Butin commun", "r": "Butin rare", "l": "Butin légendaire"}

def hid(*parts):
    h = hashlib.sha1("/".join(parts).encode()).hexdigest()[:16].upper()
    return str(1 + int(h[0], 16) % 7) + h[1:]  # 1 à 7 : reste un long Java positif

# ---------- tâches ----------
COB_FIELDS = ["shiny", "pokemon", "pokemon_type", "form", "aspects", "biome", "dimension", "gender", "poke_ball_used",
              "region", "natures", "trainers", "moves", "held_items", "raid_tiers", "abilities", "dex_progress", "targetPlayer"]
def cob(action, n=1, **kw):
    return ("cob", action, n, kw)
def catch(n=1, **kw): return cob("catch", n, **kw)
def item(i, n=1, consume=False): return ("item", i, n, consume)
def struct(s): return ("structure", s)
def dim(d): return ("dimension", d)
def biome(b): return ("biome", b)
def adv(a): return ("advancement", a)
def kill(e, n=1): return ("kill", e, n)
def check(): return ("checkmark",)

def task_snbt(t, tid):
    k = t[0]
    if k == "cob":
        _, action, n, kw = t
        lines = [f'id: "{tid}"', 'type: "cobblemon_tasks:cobblemon_task"', f'action: "{action}"', f"amount: {n}L"]
        for f in COB_FIELDS:
            if f == "shiny":
                lines.append(f"shiny: {'true' if kw.get('shiny') else 'false'}")
            else:
                lines.append(f'{f}: "{kw.get(f, "")}"')
        lines += [f"min_level: {kw.get('min_level', 0)}", "max_level: 0", "max_turns: 0", f"time_min: {kw.get('time_min', 0)}L", f"time_max: {kw.get('time_max', 24000)}L"]
        return lines
    if k == "item":
        return [f'id: "{tid}"', 'type: "item"', f'item: {{ count: 1, id: "{t[1]}" }}', f"count: {t[2]}L", f"consume_items: {'true' if t[3] else 'false'}"]
    if k == "structure":
        return [f'id: "{tid}"', 'type: "structure"', f'structure: "{t[1]}"']
    if k == "dimension":
        return [f'id: "{tid}"', 'type: "dimension"', f'dimension: "{t[1]}"']
    if k == "biome":
        return [f'id: "{tid}"', 'type: "biome"', f'biome: "{t[1]}"']
    if k == "advancement":
        return [f'id: "{tid}"', 'type: "advancement"', f'advancement: "{t[1]}"', 'criterion: ""']
    if k == "kill":
        return [f'id: "{tid}"', 'type: "kill"', f'entity: "{t[1]}"', f"value: {t[2]}L"]
    return [f'id: "{tid}"', 'type: "checkmark"']

# ---------- récompenses ----------
def R(money=0, table=None, items=(), cmds=()):
    """money = CobbleDollars, table = c/r/l, items = [(id, n)], cmds = [(commande, titre, icone)]"""
    return (money, table, list(items), list(cmds))
def cle(kind, n=1):
    return (f"/crates key give {{p}} cle_{kind} {n}", f"{n} clé{'s' if n > 1 else ''} {kind}", "minecraft:tripwire_hook")

# ---------- quête ----------
class Q:
    def __init__(self, key, title, sub, desc, icon, tasks, reward, deps=None, shape=None, size=None, opt=False, repeat=0):
        self.key, self.title, self.sub, self.desc, self.icon = key, title, sub, desc, icon
        self.tasks, self.reward, self.deps, self.shape, self.size, self.opt, self.repeat = tasks, reward, deps, shape, size, opt, repeat

ITEMS_UTILISES = set()

def icon_snbt(icon):
    if icon.startswith("tex:"):
        return f'{{ id: "ftbquests:custom_icon", components: {{ "ftbquests:icon": "{icon[4:]}" }} }}'
    ITEMS_UTILISES.add(icon)
    return f'{{ id: "{icon}" }}'

def build_chapter(ch, order):
    cid = hid("chap", ch["file"])
    lang = [f'"chapter.{cid}.title": "{ch["title"]}"', f'"chapter.{cid}.chapter_subtitle": ["{ch["sub"]}"]']
    keymap, out = {}, []
    # positions : chaque rangée commence sous la précédente
    y = 0.0
    for row in ch["rows"]:
        x = 0.0
        prev = None
        for i, q in enumerate(row):
            q.x, q.y = x, y
            if q.deps is None:
                q.deps = [prev.key] if prev else ([ch["rows"][0][0].key] if q is not ch["rows"][0][0] else [])
            keymap[q.key] = hid(ch["file"], q.key)
            prev = q
            x += 1.5
        y += 1.5
    for row in ch["rows"]:
        for q in row:
            qid = keymap[q.key]
            deps = []
            for d in q.deps:
                deps.append(d if len(d) == 16 and d.isupper() else keymap[d])
            L = ["{", f'\tid: "{qid}"', f"\ticon: {icon_snbt(q.icon)}", f"\tx: {q.x}d", f"\ty: {q.y}d"]
            if q.shape: L.append(f'\tshape: "{q.shape}"')
            if q.size: L.append(f"\tsize: {q.size}d")
            if q.opt: L.append("\toptional: true")
            if q.repeat: L += ["\tcan_repeat: true", f"\trepeat_cooldown: {q.repeat}L"]
            if deps: L.append("\tdependencies: [" + ", ".join(f'"{d}"' for d in deps) + "]")
            L.append("\ttasks: [")
            for j, t in enumerate(q.tasks):
                tid = hid(ch["file"], q.key, "t", str(j))
                L.append("\t\t{"); L += ["\t\t\t" + s for s in task_snbt(t, tid)]; L.append("\t\t}")
                if t[0] == "item": ITEMS_UTILISES.add(t[1])
            L.append("\t]")
            money, table, items, cmds = q.reward
            rw = []
            if money:
                rid = hid(ch["file"], q.key, "r", "cd")
                rw.append([f'id: "{rid}"', 'type: "command"', f'command: "/cobbledollars give {{p}} {money}"', "player_command: false", "silent: true", 'icon: { id: "cobblemon:relic_coin" }'])
                lang.append(f'"reward.{rid}.title": "{money} CobbleDollars"')
            for j, (iid, n) in enumerate(items):
                rid = hid(ch["file"], q.key, "r", "i", str(j))
                rw.append([f'id: "{rid}"', 'type: "item"', f'item: {{ count: {n}, id: "{iid}" }}'])
                ITEMS_UTILISES.add(iid)
            for j, (cmd, title, ic) in enumerate(cmds):
                rid = hid(ch["file"], q.key, "r", "c", str(j))
                rw.append([f'id: "{rid}"', 'type: "command"', f'command: "{cmd}"', "player_command: false", "silent: true", f'icon: {{ id: "{ic}" }}'])
                lang.append(f'"reward.{rid}.title": "{title}"')
            if table:
                rid = hid(ch["file"], q.key, "r", "t")
                rw.append([f'id: "{rid}"', 'type: "random"', f"table_id: {TABLES[table]}L"])
            L.append("\trewards: [")
            for r in rw:
                L.append("\t\t{"); L += ["\t\t\t" + s for s in r]; L.append("\t\t}")
            L.append("\t]")
            L.append("}")
            out.append("\n".join("\t\t" + s for s in L))
            lang.append(f'"quest.{qid}.title": "{q.title}"')
            if q.sub: lang.append(f'"quest.{qid}.quest_subtitle": "{q.sub}"')
            if q.desc:
                lines = ", ".join('"' + s.replace('"', '\\"') + '"' for s in q.desc.split("|"))
                lang.append(f'"quest.{qid}.quest_desc": [{lines}]')
    head = ["{", f'\tid: "{cid}"', '\tgroup: ""', f"\torder_index: {order}", f'\tfilename: "{ch["file"]}"',
            f"\ticon: {icon_snbt(ch['icon'])}", '\tdefault_quest_shape: ""', "\tdefault_hide_dependency_lines: false", "\tquests: ["]
    txt = "\n".join(head) + "\n" + "\n".join(out) + "\n\t]\n}\n"
    n = sum(len(r) for r in ch["rows"])
    return txt, lang, n

def main():
    import quetes_mods
    from chapitres import CHAPITRES
    global ITEMS_UTILISES
    ITEMS_UTILISES = quetes_mods.ITEMS_UTILISES
    build = quetes_mods.build_chapter
    src, dst = sys.argv[1], sys.argv[2]
    if os.path.exists(dst): shutil.rmtree(dst)
    shutil.copytree(src, dst)
    base_order = 5
    all_lang, total = [], 0
    for i, ch in enumerate(CHAPITRES):
        txt, lang, n = build(ch, base_order + i)
        open(os.path.join(dst, "chapters", ch["file"] + ".snbt"), "w", encoding="utf-8").write(txt)
        all_lang += lang; total += n
        print(f"{ch['file']:<14} {n:>3} quêtes")
    # FTB Quests 2101 lit "icon" comme un objet { id: ... } : une chaîne est ignorée
    import re, glob
    for f in glob.glob(os.path.join(dst, "chapters", "*.snbt")) + glob.glob(os.path.join(dst, "reward_tables", "*.snbt")):
        s = open(f, encoding="utf-8").read()
        s2 = re.sub(r'(\bicon: )"([a-z0-9_.-]+:[a-z0-9_./-]+)"', r'\1{ id: "\2" }', s)
        if s2 != s: open(f, "w", encoding="utf-8").write(s2)
    lp = os.path.join(dst, "lang", "en_us.snbt")
    t = open(lp, encoding="utf-8").read().rstrip()
    assert t.endswith("}")
    t = t[:-1].rstrip() + "\n" + "\n".join("\t" + s for s in all_lang) + "\n}\n"
    t = t.replace(" & ", " et ")  # & = code couleur pour FTB Quests
    open(lp, "w", encoding="utf-8").write(t)
    open(os.path.join(dst, "lang", "fr_fr.snbt"), "w", encoding="utf-8").write(t)
    open(os.path.join(dst, "..", "items_utilises.txt"), "w").write("\n".join(sorted(ITEMS_UTILISES)))
    print("TOTAL", total, "quêtes ;", len(ITEMS_UTILISES), "items utilisés")

if __name__ == "__main__":
    main()
