"""Ajoute des objets Mega Showdown (méga-gemmes, cristaux Z, objets de légendaires) aux tables Rare et Légendaire.
Usage : python ajouter_legendaires.py sakuflemon-loot-new.zip sortie.zip mega_showdown.jar
Ne garde que les identifiants qui ont un modèle d'item dans le jar (sinon la table entière ne chargerait pas)."""
import json, sys, zipfile

BASE, OUT, JAR = sys.argv[1:4]
jar = zipfile.ZipFile(JAR)
noms = set(jar.namelist())
def existe(i):
    return f"assets/mega_showdown/models/item/{i}.json" in noms or f"assets/mega_showdown/items/{i}.json" in noms

MEGA = """abomasite absolite aerodactylite aggronite alakazite altarianite ampharosite audinite banettite beedrillite
blastoisinite blazikenite cameruptite charizardite_x charizardite_y galladite garchompite gardevoirite gengarite glalitite
gyaradosite heracronite houndoominite kangaskhanite lopunnite lucarionite manectite mawilite medichamite metagrossite
pidgeotite pinsirite sablenite salamencite sceptilite scizorite sharpedonite slowbronite steelixite swampertite
tyranitarite venusaurite""".split()
Z = """buginium_z darkinium_z dragonium_z electrium_z fairium_z fightinium_z firium_z flyinium_z ghostium_z grassium_z
groundium_z icium_z normalium_z poisonium_z psychium_z rockium_z steelium_z waterium_z""".split()
LEGENDE = """adamant_orb lustrous_orb griseous_orb red_orb blue_orb rusted_sword rusted_shield dna_splicer n_solarizer
n_lunarizer reins_of_unity reveal_glass prison_bottle soul_dew zygarde_core cornerstone_mask hearthflame_mask
wellspring_mask latiasite latiosite mewtwonite_x mewtwonite_y diancite lunalium_z solganium_z ultranecrozium_z
marshadium_z mewnium_z tapunium_z""".split()
COLLECTION = [f"{t}_plate" for t in "draco dread earth fist flame icicle insect iron meadow mind pixie sky splash spooky stone toxic zap".split()] \
    + [f"{t}_memory" for t in "bug dark dragon electric fairy fighting fire flying ghost grass ground ice poison psychic rock steel water".split()] \
    + [f"{t}_drive" for t in "burn chill douse shock".split()]

def entries(ids, w):
    return [{"type": "minecraft:item", "name": f"mega_showdown:{i}", "weight": w} for i in ids if existe(i)]

manque = [i for i in MEGA + Z + LEGENDE + COLLECTION + ["zygarde_cell", "legend_plate"] if not existe(i)]
cell = entries(["zygarde_cell"], 1)
for e in cell:
    e["functions"] = [{"function": "minecraft:set_count", "count": {"type": "minecraft:uniform", "min": 1, "max": 3}}]
AJOUTS = {
    # Rare : 1 chance sur 4 d'avoir une méga-gemme classique ou un cristal Z
    "rare": {"rolls": 1, "entries": [{"type": "minecraft:empty", "weight": 180}] + entries(MEGA, 1) + entries(Z, 1)},
    # Légendaire : 1 chance sur 3 d'avoir un objet de légendaire (plaques, mémoires et cellules plus fréquentes)
    "legendaire": {"rolls": 1, "entries": [{"type": "minecraft:empty", "weight": 224}] + entries(LEGENDE, 1)
                   + entries(COLLECTION, 2) + entries(["legend_plate"], 1) + [dict(e, weight=6) for e in cell]},
}
base = zipfile.ZipFile(BASE)
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as out:
    for n in base.namelist():
        data = base.read(n)
        for tier, pool in AJOUTS.items():
            if n == f"data/sakuflemon/loot_table/coffres/{tier}.json":
                t = json.loads(data)
                t["pools"].append(pool)
                data = json.dumps(t, indent=2, ensure_ascii=False).encode()
                print(tier, len(pool["entries"]) - 1, "objets ajoutés")
        out.writestr(n, data)
print("Identifiants absents du jar (ignorés) :", manque or "aucun")
