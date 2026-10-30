"""Ajoute le tirage Pokémon de sakuflemon-loot aux coffres de nouveaux mods de structures.
Usage : python ajouter_loot.py sakuflemon-loot.zip sortie.zip mod1.jar [mod2.jar ...]
Mêmes règles de rang que serveur/loot/generer.py (branche claude/project-thread-19hwkg)."""
import json, re, sys, zipfile

BASE, OUT, JARS = sys.argv[1], sys.argv[2], sys.argv[3:]
SKIP = re.compile(r"maps/|pots/|spawner|keys/|special_items|artifact/|entity/|entities/|archaelogy|archeology|/mob/|banners|head_self|random_blocks|gameplay/|blocks/|dispenser|brushable|suspicious|equipment|barter|fishing|lucky_pool")
LEG = re.compile(r"treasure|tresure|vault|boss|pharaoh|heart_loot|king_statue|greater_loot|grand_library|bounty|throne|elytra")
RARE = re.compile(r"library|lab|temple|crypt|tomb|grave|fortress|mansion|castle|sanctum|reactor|citadel|shrine|end_|outstation|donjon|keep|armou?ry|hideout|fort|trident|toxic|witch|nether|monument|beacon|obsidian|worship|statue|secret|evoker|pyramid|bastion|stronghold|aviary|ceryneian|illager|mechanical|scorched|heavenly|kisegi|lighthouse|monastery|plague|thornborn|typhon|foundry|giant|aerial|airship|carrack|bandit")
LOW = re.compile(r"junk|food|kitchen|lumber|nuggets|waste|wardrobe|/pot$|storage|supply|barracks|farmer|butcher|low$|village|small|well")

def tier_of(rid):
    if LEG.search(rid):
        return "legendaire"
    return "rare" if RARE.search(rid) and not LOW.search(rid) else "commun"

def refs(d):
    return set(re.findall(r'"(?:value|name)": "([a-z0-9_.-]+:[a-z0-9_/.-]+)"', json.dumps(d)))

base = zipfile.ZipFile(BASE)
deja = set(base.namelist())
tables = {}
for jar in JARS:
    z = zipfile.ZipFile(jar)
    for n in z.namelist():
        m = re.match(r"data/([^/]+)/(loot_tables?)/(.+)\.json$", n)
        if not m:
            continue
        ns, folder, path = m.groups()
        rid = f"{ns}:{path}"
        try:
            d = json.loads(z.read(n))
        except ValueError:
            continue
        if n in deja or "cobblemon:" in json.dumps(d) or SKIP.search(rid):
            continue
        typ = d.get("type")
        if typ in ("minecraft:chest", "chest") or (typ is None and "chest" in path):
            tables[rid] = (n, d)
chosen = set(tables)
changed = True
while changed:  # une table qui en appelle une autre déjà enrichie ne reçoit rien (pas de double loot)
    changed = False
    for rid in list(chosen):
        if refs(tables[rid][1]) & (chosen - {rid}):
            chosen.discard(rid); changed = True
compte = {"commun": 0, "rare": 0, "legendaire": 0}
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as out:
    for n in base.namelist():
        out.writestr(n, base.read(n))
    for rid in sorted(chosen):
        n, d = tables[rid]
        t = tier_of(rid)
        compte[t] += 1
        d.setdefault("pools", []).append({"rolls": 1, "entries": [{"type": "minecraft:loot_table", "value": f"sakuflemon:coffres/{t}"}]})
        out.writestr(n, json.dumps(d, indent=2, ensure_ascii=False))
        print(t, rid)
print("Ajoutées :", len(chosen), compte, "| écartées (appellent une autre table) :", len(tables) - len(chosen))
