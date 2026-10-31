# -*- coding: utf-8 -*-
"""Chapitres des 3 séries de dresseurs RCT (Radical Red / BDSP / Unbound).
Chaque dresseur clé est une quête, dans l'ordre exact de la chaîne RCT (req=)."""
from quetes_mods import Q, R, cle, cob, item



LIEUX = {
    "grotte": "grottes, plateaux, montagnes ou collines",
    "aride": "souterrains, badlands, terres désolées ou savanes",
    "plaine": "plaines ou zones clairsemées",
    "rare": "plaines, biomes rares ou ville de l'End",
    "eau": "près de l'eau : rivières, plages, océans",
    "dense": "forêts denses ou luxuriantes",
    "spooky": "biomes sombres ou clairsemés",
    "marais": "marais ou jungles",
    "chaud": "biomes chauds",
    "sommet": "montagnes et sommets",
    "froid": "biomes froids",
    "fin": "ville de l'End ou biomes rares",
    "nether": "le Nether, badlands, terres désolées ou savanes",
    "foret": "forêts, forêts denses ou marais",
    "colline": "collines, montagnes ou sommets",
    "jungle": "forêts, jungles ou forêts denses",
    "ruines": "Cité antique, pyramide, ville de l'End, temple de la jungle ou forteresse du Nether",
    "antique": "Cité antique ou ville de l'End",
    "partout": "n'importe où sur ta route",
}

def chef(lvl):
    return "l" if lvl >= 75 else ("r" if lvl >= 30 else "c")

def D(serie, key, nom, role, lvl, ids, lieu, icon, kind="dresseur"):
    """Une quête 'bats ce dresseur clé'. ids = un ou plusieurs ID RCT (variantes)."""
    money = 200 + lvl * 40
    shape = {"champion": "hexagon", "e4": "diamond", "maitre": "gear", "boss": "square"}.get(kind)
    cmds = [cle("legendaire", 2)] if kind == "maitre" else ([cle("rare")] if kind in ("champion", "e4") else [])
    desc = f"Dresseur clé de la série, niveau {lvl}.|On le croise : {LIEUX[lieu]}.|Il n'apparaît que si ton Pokémon le plus fort n'est pas trop loin de son niveau."
    return Q(f"{serie}_{key}", nom, role, desc, icon, [cob("defeat_trainer", 1, trainers=",".join(ids))],
             R(money, chef(lvl), cmds=cmds), shape=shape, size=1.5 if kind == "maitre" else None)

def debut(serie, nom):
    return Q(f"{serie}_debut", f"Série {nom}", "S'inscrire à l'Association des Dresseurs",
             f"Trouve l'Association des Dresseurs (près des villages) et choisis la série {nom}.|Récupère ta Carte de Dresseur.|Attention : commencer une autre série remet la tienne à zéro.",
             "rctmod:trainer_card", [item("rctmod:trainer_card")], R(300, "c"), size=1.5, deps=[])

def rangées(qs, n=8):
    for a, b in zip(qs, qs[1:]):
        if b.deps is None: b.deps = [a.key]
    return [qs[i:i + n] for i in range(0, len(qs), n)]

# ---------------------------------------------------------------- Kanto (Radical Red)
k = "kanto"
KANTO = [debut(k, "Kanto (Radical Red)"),
    D(k, "pierre", "Pierre", "Champion d'Argenta", 14, ["leader_brock_019e"], "grotte", "minecraft:cobblestone", "champion"),
    D(k, "archer1", "Archer", "Admin de la Team Rocket", 21, ["rocket_admin_archer_002e"], "aride", "minecraft:red_banner", "boss"),
    D(k, "terry1", "Terry", "Ton rival", 21, ["rival_terry_014c", "rival_terry_014d", "rival_terry_014e"], "rare", "cobblemon:poke_ball"),
    D(k, "ondine", "Ondine", "Championne d'Azuria", 27, ["leader_misty_019f"], "eau", "minecraft:water_bucket", "champion"),
    D(k, "brendan1", "Brendan", "Dresseur de Hoenn", 29, ["trainer_brendan_0032"], "partout", "cobblemon:great_ball"),
    D(k, "major_bob", "Major Bob", "Champion de Carmin-sur-Mer", 34, ["leader_lt_surge_01a0"], "plaine", "cobblemon:thunder_stone", "champion"),
    D(k, "erika", "Érika", "Championne de Céladopole", 44, ["leader_erika_01a1"], "dense", "cobblemon:leaf_stone", "champion"),
    D(k, "giovanni1", "Giovanni", "Chef de la Team Rocket", 46, ["boss_giovanni_015c"], "partout", "minecraft:netherite_ingot", "boss"),
    D(k, "terry2", "Terry", "Ton rival, encore", 55, ["rival_terry_01b0", "rival_terry_01b1", "rival_terry_01b2"], "rare", "cobblemon:great_ball"),
    D(k, "archer_ariane", "Archer et Ariane", "Duo d'admins Rocket", 55, ["rocket_admin_archer_ariana_m000"], "nether", "minecraft:red_banner", "boss"),
    D(k, "giovanni2", "Giovanni", "La revanche", 56, ["boss_giovanni_015d"], "partout", "minecraft:netherite_ingot", "boss"),
    D(k, "morgane", "Morgane", "Championne de Safrania", 59, ["leader_sabrina_01a4"], "spooky", "cobblemon:twisted_spoon", "champion"),
    D(k, "brendan2", "Brendan", "Il a progressé", 63, ["trainer_brendan_0039"], "partout", "cobblemon:ultra_ball"),
    D(k, "koga", "Koga", "Champion de Parmanie", 68, ["leader_koga_01a2"], "marais", "cobblemon:poison_barb", "champion"),
    D(k, "may", "May", "Dresseuse de Hoenn", 73, ["trainer_may_003d"], "partout", "cobblemon:ultra_ball"),
    D(k, "auguste", "Auguste", "Champion de Cramois'Île", 76, ["leader_blaine_01a3"], "chaud", "cobblemon:fire_stone", "champion"),
    D(k, "archer3", "Archer", "Dernier assaut Rocket", 79, ["rocket_admin_archer_0043"], "partout", "minecraft:red_banner", "boss"),
    D(k, "ariane", "Ariane", "Admin de la Team Rocket", 79, ["rocket_admin_ariana_0044"], "partout", "minecraft:red_banner", "boss"),
    D(k, "giovanni3", "Giovanni", "Champion de Jadielle", 80, ["boss_giovanni_0045"], "partout", "minecraft:netherite_ingot", "champion"),
    D(k, "sandra", "Sandra", "La dresseuse de dragons", 81, ["leader_clair_004a"], "sommet", "cobblemon:dragon_fang", "champion"),
    D(k, "terry3", "Terry", "Avant la Ligue", 81, ["rival_terry_01b3", "rival_terry_01b4", "rival_terry_01b5"], "rare", "cobblemon:ultra_ball"),
    D(k, "brendan3", "Brendan", "Le dernier duel", 82, ["trainer_brendan_001a"], "partout", "cobblemon:ultra_ball"),
]
# Conseil 4 : les quatre dépendent de Brendan 3, le Maître dépend des quatre
k4 = [D(k, "olga", "Olga", "Conseil 4 – Glace", 85, ["elite_four_lorelei_004d", "elite_four_lorelei_004e"], "froid", "cobblemon:never_melt_ice", "e4"),
      D(k, "agatha", "Agatha", "Conseil 4 – Spectre", 85, ["elite_four_agatha_0053", "elite_four_agatha_0054"], "marais", "cobblemon:spell_tag", "e4"),
      D(k, "aldo", "Aldo", "Conseil 4 – Combat", 85, ["elite_four_bruno_0050", "elite_four_bruno_0051"], "grotte", "cobblemon:black_belt", "e4"),
      D(k, "peter", "Peter", "Conseil 4 – Dragon", 85, ["elite_four_lance_0056", "elite_four_lance_0057"], "sommet", "cobblemon:dragon_scale", "e4")]
for q in k4: q.deps = [f"{k}_brendan3"]
k_maitre = D(k, "maitre", "Maître Terry", "Le sommet de Kanto", 85, ["champion_terry_01b6", "champion_terry_01b7", "champion_terry_01b8"], "fin", "minecraft:gold_block", "maitre")
k_maitre.deps = [q.key for q in k4]
k_red = Q(f"{k}_red", "Red", "Le dresseur silencieux", "Un défi facultatif au niveau 100, après la Ligue.|On dit qu'il attend au sommet d'une montagne.", "cobblemon:master_ball",
          [cob("defeat_trainer", 1, trainers="trainer_red_0003")], R(10000, "l", cmds=[cle("legendaire", 3)]), shape="gear", size=1.5, opt=True, deps=[k_maitre.key])
serie_kanto = dict(file="serie_kanto", title="Série Kanto", sub="Radical Red : les badges de Kanto", icon="cobblemon:poke_ball",
                   rows=rangées(KANTO) + [k4 + [k_maitre, k_red]])

# ---------------------------------------------------------------- Sinnoh (BDSP)
s = "sinnoh"
SINNOH = [debut(s, "Sinnoh (BDSP)"),
    D(s, "pierrick", "Pierrick", "Champion de Charbourg", 14, ["gym_leader_roark_0395"], "grotte", "minecraft:coal", "champion"),
    D(s, "mars1", "Mars", "Commandante Galaxie", 16, ["commander_mars_03c2"], "partout", "minecraft:light_blue_banner", "boss"),
    D(s, "jupiter1", "Jupiter", "Commandante Galaxie", 20, ["commander_jupiter_041d"], "partout", "minecraft:light_blue_banner", "boss"),
    D(s, "flo", "Flo", "Championne de Vestigion", 22, ["gym_leader_gardenia_03d6"], "dense", "cobblemon:leaf_stone", "champion"),
    D(s, "cedric1", "Cédric", "Ton rival", 21, ["pokemon_trainer_cedric_0445", "pokemon_trainer_cedric_0446", "pokemon_trainer_cedric_0447"], "partout", "cobblemon:poke_ball"),
    D(s, "melina", "Mélina", "Championne de Voilaroc", 30, ["gym_leader_maylene_03d8"], "colline", "cobblemon:black_belt", "champion"),
    D(s, "lovis", "Lovis", "Champion de Verchamps", 30, ["gym_leader_wake_03d7"], "eau", "minecraft:water_bucket", "champion"),
    D(s, "cedric2", "Cédric", "Il ne lâche rien", 31, ["pokemon_trainer_cedric_0448", "pokemon_trainer_cedric_0449", "pokemon_trainer_cedric_044a"], "partout", "cobblemon:great_ball"),
    D(s, "kimera", "Kiméra", "Championne de Unionpolis", 36, ["gym_leader_fantina_03d9"], "spooky", "cobblemon:spell_tag", "champion"),
    D(s, "cedric3", "Cédric", "Encore lui", 37, ["pokemon_trainer_cedric_044b", "pokemon_trainer_cedric_044c", "pokemon_trainer_cedric_044d"], "partout", "cobblemon:great_ball"),
    D(s, "charles", "Charles", "Champion de Joliberges", 39, ["gym_leader_byron_0399"], "grotte", "minecraft:iron_block", "champion"),
    D(s, "saturne1", "Saturne", "Commandant Galaxie", 37, ["commander_saturn_041f"], "partout", "minecraft:light_blue_banner", "boss"),
    D(s, "mars2", "Mars", "La revanche", 39, ["commander_mars_041c"], "partout", "minecraft:light_blue_banner", "boss"),
    D(s, "gladys", "Gladys", "Championne de Frimapic", 42, ["gym_leader_candice_03da"], "froid", "cobblemon:never_melt_ice", "champion"),
    D(s, "helio1", "Hélio", "Chef de la Team Galaxie", 43, ["team_galactic_boss_cyrus_041a"], "partout", "minecraft:ender_eye", "boss"),
    D(s, "saturne2", "Saturne", "Il protège le lac", 40, ["commander_saturn_0420"], "partout", "minecraft:light_blue_banner", "boss"),
    D(s, "mars_jupiter", "Mars et Jupiter", "Duo de commandantes", 41, ["commander_mars_jupiter_m009"], "partout", "minecraft:light_blue_banner", "boss"),
    D(s, "helio2", "Hélio", "Au Mont Couronné", 48, ["team_galactic_boss_cyrus_041b"], "partout", "minecraft:ender_eye", "boss"),
    D(s, "tanguy", "Tanguy", "Champion de Rivamar", 49, ["gym_leader_volkner_03db"], "plaine", "cobblemon:thunder_stone", "champion"),
    D(s, "cedric4", "Cédric", "Avant la Ligue", 55, ["pokemon_trainer_cedric_044e", "pokemon_trainer_cedric_044f", "pokemon_trainer_cedric_0450"], "partout", "cobblemon:ultra_ball"),
    D(s, "aaron", "Aaron", "Conseil 4 – Insecte", 57, ["elite_four_aaron_039f"], "foret", "cobblemon:silver_powder", "e4"),
    D(s, "terry", "Terry", "Conseil 4 – Sol", 59, ["elite_four_bertha_03a0"], "partout", "cobblemon:soft_sand", "e4"),
    D(s, "adrien", "Adrien", "Conseil 4 – Feu", 61, ["elite_four_flint_03a1"], "chaud", "minecraft:blaze_powder", "e4"),
    D(s, "lucio", "Lucio", "Conseil 4 – Psy", 63, ["elite_four_lucian_03a2"], "partout", "cobblemon:twisted_spoon", "e4"),
    D(s, "cynthia", "Cynthia", "Maîtresse de Sinnoh", 66, ["champion_cynthia_03a5"], "fin", "minecraft:gold_block", "maitre"),
]
serie_sinnoh = dict(file="serie_sinnoh", title="Série Sinnoh", sub="BDSP : la Team Galaxie et Cynthia", icon="cobblemon:dawn_stone", rows=rangées(SINNOH))

# ---------------------------------------------------------------- Unbound
u = "unbound"
RIVAL = lambda n, *h: [f"rival_{n}_player_chose_{p}_{x}" for p, x in zip(("gible", "beldum", "larvitar"), h)]
UNBOUND = [debut(u, "Unbound"),
    D(u, "rival2", "Le rival", "Premier vrai duel", 19, RIVAL(2, "0609", "060a", "060b"), "partout", "cobblemon:poke_ball"),
    D(u, "mirskle", "Mirskle", "Championne – Plante", 21, ["leader_mirskle_05aa"], "foret", "cobblemon:leaf_stone", "champion"),
    D(u, "marlon1", "Marlon", "Admin de l'Ombre", 28, ["shadow_admin_marlon_grunt_m00e"], "partout", "minecraft:black_banner", "boss"),
    D(u, "vega", "Vega", "Champion – Spectre", 27, ["leader_vega_05ab"], "nether", "cobblemon:spell_tag", "champion"),
    D(u, "ivory1", "Ivory", "Admin de l'Ombre", 34, ["shadow_admin_ivory_1_05ba"], "partout", "minecraft:black_banner", "boss"),
    D(u, "zeph1", "Zeph", "Chef de l'Ombre", 33, ["boss_zeph_1_05bb"], "partout", "minecraft:wither_skeleton_skull", "boss"),
    D(u, "rival3", "Le rival", "Il s'est entraîné", 33, RIVAL(3, "05fa", "05fb", "05fc"), "partout", "cobblemon:great_ball"),
    D(u, "alice", "Alice", "Championne – Vol", 33, ["leader_alice_05ac"], "colline", "minecraft:feather", "champion"),
    D(u, "mel", "Mel", "Champion – Normal", 37, ["leader_mel_05ad"], "plaine", "cobblemon:silk_scarf", "champion"),
    D(u, "ivory2", "Ivory", "Encore l'Ombre", 38, ["shadow_admin_ivory_grunt_m00f"], "partout", "minecraft:black_banner", "boss"),
    D(u, "maxima", "Maxima", "Héritière – Combat", 41, ["sucessor_maxima_05ae"], "partout", "cobblemon:black_belt", "champion"),
    D(u, "marlon2", "Marlon", "La revanche", 41, ["shadow_admin_marlon_2_05be"], "partout", "minecraft:black_banner", "boss"),
    D(u, "rival4", "Le rival", "Un duel serré", 47, RIVAL(4, "05fd", "05fe", "05ff"), "partout", "cobblemon:great_ball"),
    D(u, "galavan", "Galavan", "Champion – Électrik", 46, ["leader_galavan_05af"], "partout", "cobblemon:thunder_stone", "champion"),
    D(u, "vega_ruine", "Vega", "La Lumière de la Ruine", 47, ["light_of_ruin_vega_05c1"], "ruines", "minecraft:soul_lantern", "boss"),
    D(u, "zeph2", "Zeph", "La revanche", 46, ["boss_zeph_2_05bf"], "partout", "minecraft:wither_skeleton_skull", "boss"),
    D(u, "aklove1", "Aklove", "Lumière de la Ruine", 53, ["light_of_ruin_aklove_1_05c2"], "partout", "minecraft:soul_lantern", "boss"),
    D(u, "big_mo", "Big Mo", "Champion – Combat", 53, ["leader_big_mo_05b0"], "partout", "cobblemon:muscle_band", "champion"),
    D(u, "tessy", "Tessy", "Championne – Eau", 58, ["leader_tessy_05b1"], "eau", "minecraft:water_bucket", "champion"),
    D(u, "rival5", "Le rival", "Avant la Ligue", 65, RIVAL(5, "0600", "0601", "0602"), "partout", "cobblemon:ultra_ball"),
    D(u, "ivory3", "Ivory", "Lumière de la Ruine", 62, ["light_of_ruin_admin_ivory_3_05c3"], "partout", "minecraft:soul_lantern", "boss"),
    D(u, "aklove2", "Aklove", "Seconde rencontre", 62, ["light_of_ruin_aklove_2_05c4"], "partout", "minecraft:soul_lantern", "boss"),
    D(u, "marlon3", "Marlon", "Dernier assaut", 62, ["shadow_admin_marlon_3_05c0"], "partout", "minecraft:black_banner", "boss"),
    D(u, "benjamin", "Benjamin", "Champion – Insecte", 62, ["leader_benjamin_05b2"], "jungle", "cobblemon:silver_powder", "champion"),
]
u4 = [D(u, "moleman", "Moleman", "Conseil 4", 76, ["elite_four_moleman_05b3"], "partout", "cobblemon:soft_sand", "e4"),
      D(u, "elias", "Elias", "Conseil 4", 76, ["elite_four_elias_05b4"], "partout", "cobblemon:twisted_spoon", "e4"),
      D(u, "arabella", "Arabella", "Conseil 4", 76, ["elite_four_arabella_05b5"], "partout", "cobblemon:spell_tag", "e4"),
      D(u, "penny", "Penny", "Conseil 4", 76, ["elite_four_penny_05b6"], "partout", "minecraft:pink_dye", "e4")]
for q in u4: q.deps = [f"{u}_benjamin"]
u_maitre = D(u, "jax", "Maître Jax", "Le sommet de Borrius", 76, ["champion_jax_05b7"], "fin", "minecraft:gold_block", "maitre")
u_maitre.deps = [q.key for q in u4]
u_fin = D(u, "aklove3", "Aklove", "Le dernier secret", 84, ["light_of_ruin_aklove_3_05c5"], "antique", "minecraft:echo_shard", "boss")
u_fin.deps = [u_maitre.key]
serie_unbound = dict(file="serie_unbound", title="Série Unbound", sub="Borrius : l'Ombre et la Lumière de la Ruine", icon="cobblemon:dusk_stone",
                     rows=rangées(UNBOUND) + [u4 + [u_maitre, u_fin]])

SERIES = [serie_kanto, serie_sinnoh, serie_unbound]
