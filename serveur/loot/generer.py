"""Génère le datapack sakuflemon-loot : 3 tables Pokémon + ajout d'un pool dans les coffres vanilla."""
import json, os, shutil, sys

VANILLA, IDS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
MODS = sys.argv[4] if len(sys.argv) > 4 else None  # dossier des jars de structures dézippés (data/*/loot_table)
ids = set(open(IDS).read().split())

def e(item, w, lo=1, hi=1):
    assert item in ids, item
    d = {"type": "minecraft:item", "name": f"cobblemon:{item}", "weight": w}
    if hi > 1:
        d["functions"] = [{"function": "minecraft:set_count", "count": {"type": "minecraft:uniform", "min": lo, "max": hi}}]
    return d

BERRIES = ["oran_berry", "sitrus_berry", "pecha_berry", "cheri_berry", "chesto_berry", "rawst_berry", "aspear_berry",
           "persim_berry", "leppa_berry", "lum_berry"]
APRICORNS = [f"{c}_apricorn" for c in ["red", "yellow", "green", "blue", "pink", "black", "white"]]
STONES = ["fire_stone", "water_stone", "thunder_stone", "leaf_stone", "moon_stone", "sun_stone", "ice_stone",
          "shiny_stone", "dusk_stone", "dawn_stone"]
SPECIAL_BALLS = ["dusk_ball", "quick_ball", "timer_ball", "heal_ball", "net_ball", "dive_ball", "nest_ball",
                 "luxury_ball", "repeat_ball", "friend_ball", "level_ball", "lure_ball", "moon_ball", "love_ball",
                 "fast_ball", "heavy_ball"]
VITAMINS = ["hp_up", "protein", "iron", "calcium", "zinc", "carbos"]
MINTS = ["adamant_mint", "jolly_mint", "modest_mint", "timid_mint", "bold_mint", "calm_mint", "careful_mint",
         "impish_mint", "brave_mint", "quiet_mint"]
HELD = ["leftovers", "exp_share", "lucky_egg", "soothe_bell", "shell_bell", "everstone", "focus_band",
        "black_belt", "charcoal_stick", "mystic_water", "miracle_seed", "magnet", "twisted_spoon", "spell_tag"]
FOSSILS = ["helix_fossil", "dome_fossil", "old_amber_fossil", "root_fossil", "claw_fossil", "skull_fossil",
           "armor_fossil", "cover_fossil", "plume_fossil", "jaw_fossil", "sail_fossil"]

TIERS = {
    "commun": [{"rolls": {"type": "minecraft:uniform", "min": 2, "max": 4}, "entries":
        [e("poke_ball", 30, 2, 6), e("potion", 25, 1, 3), e("great_ball", 10, 1, 3), e("super_potion", 10, 1, 2),
         e("full_heal", 6), e("burn_heal", 4), e("ice_heal", 4), e("paralyze_heal", 4), e("revive", 5),
         e("ether", 4), e("exp_candy_xs", 10, 1, 3), e("exp_candy_s", 6, 1, 2)]
        + [e(b, 3, 1, 4) for b in BERRIES] + [e(a, 3, 1, 3) for a in APRICORNS]}],
    "rare": [{"rolls": {"type": "minecraft:uniform", "min": 3, "max": 5}, "entries":
        [e("great_ball", 20, 2, 5), e("ultra_ball", 12, 1, 3), e("super_potion", 15, 1, 3), e("hyper_potion", 10, 1, 2),
         e("revive", 10, 1, 2), e("rare_candy", 6), e("exp_candy_m", 10, 1, 2), e("exp_candy_l", 4), e("pp_up", 3),
         e("elixir", 4)]
        + [e(s, 3) for s in STONES] + [e(b, 2, 1, 4) for b in SPECIAL_BALLS] + [e(v, 2) for v in VITAMINS]
        + [e(m, 1) for m in MINTS] + [e(h, 1) for h in HELD] + [e(f, 1) for f in FOSSILS]}],
    "legendaire": [{"rolls": {"type": "minecraft:uniform", "min": 4, "max": 6}, "entries":
        [e("ultra_ball", 20, 3, 8), e("max_potion", 10, 1, 3), e("full_restore", 8, 1, 2), e("max_revive", 8, 1, 2),
         e("rare_candy", 10, 1, 3), e("exp_candy_xl", 6), e("max_elixir", 4), e("ability_capsule", 4),
         e("ability_patch", 1), e("choice_band", 2), e("choice_scarf", 2), e("choice_specs", 2), e("life_orb", 2),
         e("assault_vest", 2), e("focus_sash", 2), e("weakness_policy", 2), e("eviolite", 2), e("relic_coin", 3, 1, 3),
         e("scroll_of_darkness", 1), e("scroll_of_waters", 1), e("dream_ball", 2), e("beast_ball", 1),
         e("master_ball", 1)]
        + [e(s, 2) for s in ["shiny_stone", "dusk_stone", "dawn_stone"]] + [e(m, 1) for m in MINTS]}],
}

COMMUN = ["abandoned_mineshaft", "igloo_chest", "ruined_portal", "shipwreck_supply", "simple_dungeon",
          "stronghold_corridor", "stronghold_crossing", "underwater_ruin_small"]
RARE = ["buried_treasure", "desert_pyramid", "jungle_temple", "nether_bridge", "pillager_outpost", "shipwreck_treasure",
        "stronghold_library", "underwater_ruin_big", "woodland_mansion", "ancient_city_ice_box", "bastion_bridge",
        "bastion_hoglin_stable", "bastion_other"]
LEGENDAIRE = ["ancient_city", "bastion_treasure", "end_city_treasure"]

if os.path.exists(OUT):
    shutil.rmtree(OUT)
def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(data, open(path, "w"), indent=2, ensure_ascii=False)

write(f"{OUT}/pack.mcmeta", {"pack": {"pack_format": 48, "description": "Sakuflemon : loot Pokémon dans les coffres"}})
for tier, pools in TIERS.items():
    write(f"{OUT}/data/sakuflemon/loot_table/coffres/{tier}.json", {"type": "minecraft:chest", "pools": pools})

mapping = {t: "commun" for t in COMMUN} | {t: "rare" for t in RARE} | {t: "legendaire" for t in LEGENDAIRE}
for root, _, files in os.walk(VANILLA):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), VANILLA)[:-5]
        tier = "commun" if rel.startswith("village/") else mapping.get(rel)
        if not tier:
            continue
        table = json.load(open(os.path.join(root, f)))
        table["pools"].append({"rolls": 1, "entries": [{"type": "minecraft:loot_table", "value": f"sakuflemon:coffres/{tier}"}]})
        write(f"{OUT}/data/minecraft/loot_table/chests/{rel}.json", table)
        print(tier, rel)

# --- Coffres des mods de structures ---
import glob, re
SKIP = re.compile(r"maps/|pots/|spawner|keys/|special_items|tavern_quest|artifact/|entity/|entities/|archaelogy|archeology|/mob/|castle/base/|castle/blacksmith/|castle/stand/|pipeline/base/|ghastling|hovering_inferno|banners|head_self|random_blocks")
UNTYPED_OK = re.compile(r"^(ctov:chests/|kaisyn:village/|nova_structures:chests/|incendium:(castle/barrel/|castle/treasure/|cvill/(low|medium|blacksmith|butcher|farmer|lumberjack)$|lab/|pipeline/|reactor/|sanctum/(common_loot|lower_loot|tax_collector|coffin|brewery|potions)$|quartz_flats/kitchen))")
LEG = re.compile(r"treasure|tresure|vault|boss|pharaoh|heart_loot|king_statue|greater_loot|grand_library")
RARE = re.compile(r"library|lab|temple|crypt|tomb|grave|fortress|betterfortresses|mansion|castle|sanctum|reactor|citadel|shrine|end_|outstation|donjon|keep|armou?ry|hideout|stray_fort|trident|toxic|witch|incendium|nether|monument|beacon|obsidian|worship|statue|secret|evoker")

LOW = re.compile(r"junk|food|kitchen|lumber|nuggets|waste|wardrobe|/pot$|storage|supply|barracks|farmer|butcher|low$")

def tier_of(rid):
    if LEG.search(rid):
        return "legendaire"
    return "rare" if RARE.search(rid) and not LOW.search(rid) else "commun"

if MODS:
    tables = {}
    for f in glob.glob(f"{MODS}/*/data/*/loot_table*/**/*.json", recursive=True):
        m = re.match(r".*/data/([^/]+)/(loot_tables?)/(.+)\.json$", f)
        ns, folder, path = m.groups()
        rid = f"{ns}:{path}"
        try:
            d = json.load(open(f))
        except ValueError:
            continue
        typ = d.get("type")
        if "cobblemon:" in json.dumps(d) or SKIP.search(rid):
            continue  # déjà du loot Pokémon, ou pas un coffre
        if typ in ("minecraft:chest", "chest") or (typ is None and UNTYPED_OK.search(rid)):
            tables[rid] = (ns, folder, path, d)
    # une table qui en appelle une autre déjà enrichie ne reçoit pas de pool en plus (pas de double loot)
    def refs(d):
        return set(re.findall(r'"(?:value|name)": "([a-z0-9_.-]+:[a-z0-9_/.-]+)"', json.dumps(d)))
    chosen = set(tables)
    changed = True
    while changed:
        changed = False
        for rid in list(chosen):
            if refs(tables[rid][3]) & (chosen - {rid}):
                chosen.discard(rid); changed = True
    for rid in sorted(chosen):
        ns, folder, path, d = tables[rid]
        tier = tier_of(rid)
        d.setdefault("pools", []).append({"rolls": 1, "entries": [{"type": "minecraft:loot_table", "value": f"sakuflemon:coffres/{tier}"}]})
        write(f"{OUT}/data/{ns}/{folder}/{path}.json", d)
        print(tier, rid)
