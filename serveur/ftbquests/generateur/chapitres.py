# -*- coding: utf-8 -*-
"""Contenu des 12 chapitres "mods". Textes en français (affichés via lang/en_us.snbt)."""
from quetes_mods import Q, R, cle, cob, catch, item, struct, dim, biome, adv, kill, check

T = lambda n: f"tex:sakuflemon:textures/quetes/{n}.png"
MS = "mega_showdown:"
RAID = "cobblemonraiddens:"

# ============================================================ 1. Méga-Évolution & Cristaux Z
mega = dict(file="mega", title="Méga & Cristaux Z", sub="Les pouvoirs oubliés des anciens dresseurs", icon=T("mega"), rows=[
    [Q("pierre_cle", "La Pierre Clé", "Un éclat qui répond aux Pokémon", "Les Pierres Clés poussent dans les grottes, dans des minerais qui scintillent.|Mine un minerai de Pierre Clé et récupère la pierre.", MS + "keystone", [item(MS + "keystone")], R(300, "c"), size=1.5),
     Q("bracelet", "Méga-Bracelet", "Fabrique ton bracelet", "Assemble la Pierre Clé sur un bracelet pour pouvoir méga-évoluer en combat.", MS + "mega_bracelet", [item(MS + "mega_bracelet")], R(400, "c")),
     Q("site_mega", "Le site méga", "Là où dorment les gemmes", "Les méga-gemmes se cachent dans des sites anciens, dans le monde.|Trouve une pierre méga brute.", MS + "mega_stone", [item(MS + "mega_stone")], R(400, "c")),
     Q("premiere_mega", "Première Méga-Évolution", "La puissance du lien", "Équipe un Pokémon de sa méga-gemme, puis méga-évolue-le en combat.", MS + "lucarionite", [cob("mega_evolve", 1)], R(500, "r")),
     Q("mega_starters", "Méga-Starters", "Les trois de Kanto", "Réunis les méga-gemmes des starters de Kanto.", MS + "charizardite_x", [item(MS + "venusaurite"), item(MS + "charizardite_x"), item(MS + "charizardite_y"), item(MS + "blastoisinite")], R(1500, "r")),
     Q("mega_hoenn", "Méga-Hoenn", "Les starters de Hoenn", "Réunis les méga-gemmes de Jungko, Braségali et Laggron.", MS + "blazikenite", [item(MS + "sceptilite"), item(MS + "blazikenite"), item(MS + "swampertite")], R(1500, "r")),
     Q("mega_pseudo", "Méga des pseudo-légendaires", "Les plus redoutables", "Tyranocif, Drattak, Métalosse et Carchacrok.", MS + "garchompite", [item(MS + "tyranitarite"), item(MS + "salamencite"), item(MS + "metagrossite"), item(MS + "garchompite")], R(2500, "l")),
     Q("mega_legende", "Méga-Légendes", "Mewtwo et les Éons", "Les méga-gemmes des légendaires sont les plus rares de toutes.", MS + "mewtwonite_x", [item(MS + "mewtwonite_x"), item(MS + "latiasite"), item(MS + "latiosite")], R(5000, "l"), shape="gear", size=1.5),
     Q("zamega", "Les gemmes de Navas", "Méga-Évolutions inédites", "Le mod Zamega ajoute des méga-gemmes inédites, comme celle de Zeraora.|Trouve-en une.", "zamega:zeraorite", [item("zamega:zeraorite")], R(2000, "r"), opt=True)],
    [Q("blank_z", "Cristal Z vierge", "Un cristal sans pouvoir", "Le Cristal Z vierge se trouve dans les coffres rares. Il permet de fabriquer les cristaux de type.", MS + "blank_z", [item(MS + "blank_z")], R(400, "c"), deps=["pierre_cle"]),
     Q("z_ring", "Bracelet Z", "Pour libérer la puissance Z", "Fabrique le Bracelet Z.", MS + "z_ring", [item(MS + "z_ring")], R(400, "c")),
     Q("z_starters", "Z élémentaires", "Feu, Eau, Plante", "Fabrique ou trouve les trois cristaux de base.", MS + "firium_z", [item(MS + "firium_z"), item(MS + "waterium_z"), item(MS + "grassium_z")], R(800, "c")),
     Q("premiere_capz", "Première capacité Z", "Un coup unique par combat", "Utilise une capacité Z en combat.", MS + "normalium_z", [cob("use_z_move", 1)], R(500, "r")),
     Q("z_collection", "Collection Z", "Neuf cristaux de type", "Réunis neuf autres cristaux de type.", MS + "dragonium_z", [item(MS + t + "_z") for t in ["electrium", "icium", "fightinium", "poisonium", "groundium", "flyinium", "psychium", "buginium", "rockium"]], R(2000, "r")),
     Q("z_complete", "Maître des cristaux", "Les 18 types", "Termine la collection avec les six derniers cristaux de type.", MS + "fairium_z", [item(MS + t + "_z") for t in ["ghostium", "dragonium", "darkinium", "steelium", "fairium", "normalium"]], R(3000, "l"), shape="gear"),
     Q("z_legende", "Z des légendes", "Solgaleo, Lunala, Necrozma", "Les cristaux Z des légendaires d'Alola.", MS + "ultranecrozium_z", [item(MS + "solganium_z"), item(MS + "lunalium_z"), item(MS + "ultranecrozium_z")], R(5000, "l"))],
    [Q("dynamax", "Poignet Dynamax", "Devenir géant", "Fabrique le Poignet Dynamax pour pouvoir dynamaxer tes Pokémon.", MS + "dynamax_band", [item(MS + "dynamax_band")], R(500, "c"), deps=["pierre_cle"]),
     Q("voeu", "Étoile Vœu", "Une étoile tombée du ciel", "Une Étoile Vœu donne son énergie au Poignet Dynamax.", MS + "wishing_star", [item(MS + "wishing_star")], R(600, "r")),
     Q("gigamax", "Gigamax", "La Maxi-Soupe", "Prépare une Maxi-Soupe avec des Maxi-Champis pour débloquer le Gigamax.", MS + "max_mushroom", [item(MS + "max_mushroom", 3)], R(1000, "r")),
     Q("premier_dynamax", "Premier Dynamax", "Trois tours de puissance", "Dynamaxe un Pokémon en combat.", MS + "dynamax_band", [cob("dynamax", 1)], R(500, "r"))],
    [Q("tera_orb", "Orbe Téracristal", "Le joyau de Paldea", "Trouve l'Orbe Téracristal.", MS + "tera_orb", [item(MS + "tera_orb")], R(500, "c"), deps=["pierre_cle"]),
     Q("tera_eclats", "Téra-Éclats", "Change le type Téra", "Réunis 50 Téra-Éclats d'un même type pour changer le type Téra d'un Pokémon.", MS + "fire_tera_shard", [item(MS + "fire_tera_shard", 50)], R(800, "r")),
     Q("premier_tera", "Première Téracristallisation", "Un Pokémon de cristal", "Téracristallise un Pokémon en combat.", MS + "tera_orb", [cob("terastallize", 1)], R(500, "r")),
     Q("stellaire", "Type Stellaire", "Le type légendaire de Terapagos", "Obtiens un Téra-Éclat Stellaire.", MS + "stellar_tera_shard", [item(MS + "stellar_tera_shard")], R(3000, "l"))],
    [Q("formes", "Objets de forme", "Changer l'apparence d'un légendaire", "Certains légendaires changent de forme avec un objet. Trouves-en un.", MS + "reveal_glass", [item(MS + "reveal_glass")], R(800, "r"), deps=["pierre_cle"]),
     Q("rouille", "Épée et Bouclier rouillés", "Les héros de Galar", "Réunis l'Épée rouillée et le Bouclier rouillé.", MS + "rusted_sword", [item(MS + "rusted_sword"), item(MS + "rusted_shield")], R(2000, "l")),
     Q("zygarde", "Cellules de Zygarde", "Rassemble l'ordre", "Récupère 10 cellules de Zygarde et un noyau.", MS + "zygarde_cell", [item(MS + "zygarde_cell", 10), item(MS + "zygarde_core")], R(2500, "l")),
     Q("necrozma", "Fusion lumineuse", "Le Pointeur Solaire et le Pointeur Lunaire", "Obtiens les deux objets qui fusionnent Necrozma.", MS + "n_solarizer", [item(MS + "n_solarizer"), item(MS + "n_lunarizer")], R(3000, "l")),
     Q("orbes", "Orbes et Globes", "Le Temps, l'Espace, l'Antimatière", "Réunis l'Orbe Adamant, l'Orbe Perlé et l'Orbe Platiné.", MS + "griseous_orb", [item(MS + "adamant_orb"), item(MS + "lustrous_orb"), item(MS + "griseous_orb")], R(4000, "l"), shape="gear")],
])

# ============================================================ 2. Raids
raids = dict(file="raids", title="Raids", sub="Unis contre les Pokémon géants", icon=T("raids"), rows=[
    [Q("tanieres", "Tanière lumineuse", "Une colonne de lumière", "Les tanières de raid brillent dans le monde. Trouves-en une et rejoins un raid.", RAID + "raid_crystal_block", [cob("join_raid", 1)], R(200, "c"), size=1.5),
     Q("raid1", "Raid 1 étoile", "Ton premier raid", "Gagne un raid 1 étoile.", "minecraft:nether_star", [cob("win_raid", 1, raid_tiers="1")], R(300, "c")),
     Q("raid2", "Raid 2 étoiles", "Ça se corse", "Gagne un raid 2 étoiles.", "minecraft:nether_star", [cob("win_raid", 1, raid_tiers="2")], R(500, "c")),
     Q("raid3", "Raid 3 étoiles", "Viens avec des amis", "Gagne un raid 3 étoiles.", "minecraft:nether_star", [cob("win_raid", 1, raid_tiers="3")], R(800, "r")),
     Q("raid4", "Raid 4 étoiles", "Une vraie équipe", "Gagne un raid 4 étoiles.", "minecraft:nether_star", [cob("win_raid", 1, raid_tiers="4")], R(1200, "r")),
     Q("raid5", "Raid 5 étoiles", "Les plus puissants", "Gagne un raid 5 étoiles.", "minecraft:nether_star", [cob("win_raid", 1, raid_tiers="5")], R(2000, "l")),
     Q("raid6", "Habitué des 5 étoiles", "Cinq victoires", "Gagne 5 raids 5 étoiles.", "minecraft:nether_star", [cob("win_raid", 5, raid_tiers="5")], R(3000, "l"), shape="gear"),
     Q("raid7", "Maître des raids", "Vingt victoires 5 étoiles", "Gagne 20 raids 5 étoiles. Seuls les meilleurs y arrivent.", "minecraft:nether_star", [cob("win_raid", 20, raid_tiers="5")], R(5000, "l"), shape="gear", size=1.5)],
    [Q("raid_capture", "Bourse de raid", "Le butin des vainqueurs", "Ouvre une bourse de raid gagnée en raid.", RAID + "raid_pouch", [cob("open_raid_pouch", 1)], R(400, "c"), deps=["raid1"]),
     Q("raid_10", "Habitué des raids", "10 victoires", "Gagne 10 raids, toutes étoiles confondues.", "minecraft:nether_star", [cob("win_raid", 10)], R(1000, "r")),
     Q("raid_50", "Chasseur de géants", "50 victoires", "Gagne 50 raids.", "minecraft:nether_star", [cob("win_raid", 50)], R(3000, "l")),
     Q("raid_shiny", "Raid chromatique", "Une lueur rare", "Gagne un raid contre un Pokémon chromatique.", "cobblemon:shiny_stone", [cob("win_raid", 1, shiny=True)], R(4000, "l"), opt=True)],
])

# ============================================================ 3. Éleveur
eleveur = dict(file="eleveur", title="Éleveur", sub="Œufs, IVs et pensions", icon=T("eleveur"), rows=[
    [Q("pension", "La pension", "Deux Pokémon dans un enclos", "Fabrique un Enclos (Pasture) et mets-y deux Pokémon compatibles.", "cobblemon:pasture", [item("cobblemon:pasture")], R(200, "c"), size=1.5),
     Q("premier_oeuf", "Premier œuf", "Une surprise dans l'herbe", "Récupère un œuf de Pokémon à l'enclos.", "cobbreeding:pokemon_egg", [cob("collect_egg", 1)], R(300, "c")),
     Q("eclosion", "Éclosion", "Marche, marche, marche…", "Fais éclore un œuf en le gardant dans ton inventaire pendant que tu te déplaces.", "cobbreeding:pokemon_egg", [cob("hatch_egg", 1)], R(400, "c")),
     Q("eclosion_10", "Couveuse", "10 éclosions", "Fais éclore 10 œufs.", "cobbreeding:pokemon_egg", [cob("hatch_egg", 10)], R(1000, "r")),
     Q("eclosion_50", "Éleveur chevronné", "50 éclosions", "Fais éclore 50 œufs.", "cobbreeding:pokemon_egg", [cob("hatch_egg", 50)], R(2500, "l")),
     Q("oeuf_shiny", "Éclosion chromatique", "La méthode Masuda ?", "Fais éclore un Pokémon chromatique.", "cobblemon:shiny_stone", [cob("hatch_egg", 1, shiny=True)], R(5000, "l"), shape="gear", size=1.5)],
    [Q("ditto", "Le Métamorph", "Le partenaire universel", "Attrape un Métamorph : il peut faire des œufs avec presque tout le monde.", "cobblemon:poke_ball", [catch(1, pokemon="ditto")], R(500, "c"), deps=["pension"]),
     Q("noeud", "Nœud Destin", "Transmettre les IVs", "Le Nœud Destin transmet 5 IVs des parents à l'œuf.", "cobblemon:destiny_knot", [item("cobblemon:destiny_knot")], R(800, "r")),
     Q("pierre_stase", "Pierre Stase", "Transmettre la nature", "La Pierre Stase transmet la nature du parent qui la tient.", "cobblemon:everstone", [item("cobblemon:everstone")], R(400, "c")),
     Q("menthes", "Menthes", "Changer de nature sans élevage", "Cultive ou trouve 3 menthes différentes.", "cobblemon:jolly_mint", [item("cobblemon:jolly_mint"), item("cobblemon:adamant_mint"), item("cobblemon:modest_mint")], R(600, "c")),
     Q("bonbons_ev", "Entraînement EV", "Protéine, Fer, Calcium…", "Réunis les vitamines d'entraînement.", "cobblemon:protein", [item("cobblemon:protein"), item("cobblemon:iron"), item("cobblemon:calcium"), item("cobblemon:zinc"), item("cobblemon:carbos"), item("cobblemon:hp_up")], R(1000, "r")),
     Q("capsule_talent", "Talent caché", "Le Patch Talent", "Obtiens un Patch Talent pour débloquer un talent caché.", "cobblemon:ability_patch", [item("cobblemon:ability_patch")], R(2000, "l"))],
    [Q("oeufs_types", "Œufs typés", "Chaque œuf a sa couleur", "Les œufs de Cobbreeding prennent la couleur des types du Pokémon. Fais éclore 5 Pokémon de types différents.", "cobbreeding:fire_pokemon_egg", [cob("hatch_egg", 1, pokemon_type=t) for t in ["fire", "water", "grass", "electric", "dragon"]], R(1500, "r"), deps=["eclosion"]),
     Q("manaphy", "L'œuf de Manaphy", "Un œuf légendaire", "On dit qu'un œuf bleu repose au fond des mers. Obtiens l'œuf de Manaphy.", "cobbreeding:manaphy_egg", [item("cobbreeding:manaphy_egg")], R(4000, "l"), opt=True)],
])

# ============================================================ 4. Safari
SAF = "cobblesafari:"
safari = dict(file="safari", title="Zone Safari", sub="La réserve des Pokémon rares", icon=T("safari"), rows=[
    [Q("garde_safari", "Le Garde du Safari", "Au Carrefour des mondes", "Le Garde du Safari t'attend au Carrefour des mondes, à Incarnam.|Paie l'entrée et entre dans la Zone Safari.", "cobblemon:safari_ball", [dim(SAF + "domedimension")], R(200, "c"), size=1.5),
     Q("safari_balls", "Safari Balls", "La seule Ball autorisée", "Dans le Safari, on ne capture qu'avec des Safari Balls.", "cobblemon:safari_ball", [item("cobblemon:safari_ball", 10)], R(200, "c")),
     Q("safari_capture", "Première capture Safari", "Attention, ils fuient !", "Attrape un Pokémon avec une Safari Ball.", "cobblemon:safari_ball", [catch(1, poke_ball_used="cobblemon:safari_ball")], R(400, "c")),
     Q("safari_10", "Photographe du Safari", "10 captures", "Attrape 10 Pokémon dans la Zone Safari.", "cobblemon:safari_ball", [catch(10, poke_ball_used="cobblemon:safari_ball")], R(1000, "r")),
     Q("safari_rares", "Les raretés du Safari", "Tauros, Kangourex, Leveinard", "Attrape ces trois Pokémon avec une Safari Ball.", "cobblemon:safari_ball", [catch(1, pokemon=p, poke_ball_used="cobblemon:safari_ball") for p in ["tauros", "kangaskhan", "chansey"]], R(2000, "r")),
     Q("safari_shiny", "Safari chromatique", "Le Graal du Safari", "Attrape un Pokémon chromatique dans la Zone Safari.", "cobblemon:shiny_stone", [catch(1, shiny=True, poke_ball_used="cobblemon:safari_ball")], R(4000, "l"), shape="gear")],
    [Q("nid", "Les nids", "Un œuf sauvage", "Fais un clic droit sur un nid sauvage pour récupérer un œuf.", SAF + "safari_egg_nest", [cob("collect_egg", 1, dimension=SAF + "domedimension")], R(300, "c"), deps=["garde_safari"]),
     Q("incubateur", "L'Incubateur", "Pour faire éclore les œufs sauvages", "Fabrique un Incubateur. Il accélère aussi les œufs de pension.", SAF + "incubator", [item(SAF + "incubator")], R(600, "r")),
     Q("parfum", "Parfums et encens", "Attirer certains Pokémon", "Fabrique ou trouve un parfum ou un encens.", SAF + "shinyincense", [item(SAF + "perfume")], R(400, "c")),
     Q("ballon", "Ballon à récompenses", "Il flotte là-haut…", "Trouve un ballon à récompenses et fais un clic droit dessus.", "minecraft:red_wool", [check()], R(500, "r"))],
    [Q("hoopa", "Portail de Hoopa", "Un anneau dans les airs", "Des portails de Hoopa apparaissent parfois. Traverses-en un avant qu'il se referme.", SAF + "hoopa_ring_portal", [check()], R(500, "c"), deps=["garde_safari"]),
     Q("souterrain", "Le Souterrain", "Creuser les murs", "Va dans le Souterrain de Sinnoh par un portail de Hoopa.", "minecraft:iron_pickaxe", [dim(SAF + "dungeon_underground")], R(600, "r")),
     Q("fouilles", "Fouilles", "Sphères et fossiles", "Fais le mini-jeu de fouille et déterre un trésor.", SAF + "sphere_red_s", [item(SAF + "sphere_red_s")], R(800, "r")),
     Q("base_secrete", "Base secrète", "Vole un drapeau", "Trouve une base secrète et récupère son drapeau.", SAF + "underground_flag_regular", [item(SAF + "underground_flag_regular")], R(1000, "r")),
     Q("distorsion", "Monde Distorsion", "Là où la gravité ment", "Va dans le Monde Distorsion par un portail de Hoopa.", "minecraft:crying_obsidian", [dim(SAF + "dungeon_distortion")], R(1500, "l")),
     Q("fragments", "Fragments de chaîne rouge", "Les Pokémon distordus", "Bats des Pokémon distordus et récupère 5 fragments de chaîne rouge.", SAF + "redchain_fragment", [item(SAF + "redchain_fragment", 5)], R(2500, "l"), shape="gear")],
])

# ============================================================ 5. Montures
montures = dict(file="montures", title="Montures", sub="Voyager sur le dos de ses Pokémon", icon=T("montures"), rows=[
    [Q("selle", "En selle !", "Ton premier trajet", "Certains Pokémon se laissent monter. Monte sur un Pokémon terrestre (Ponyta, Galopa, Tauros…) et valide.", "minecraft:saddle", [check()], R(300, "c"), size=1.5),
     Q("ponyta", "Cavalier", "Un compagnon rapide", "Attrape un Ponyta ou un Tauros pour tes trajets.", "minecraft:saddle", [catch(1, pokemon="ponyta")], R(300, "c")),
     Q("rapide", "Galop", "Plus vite que le vent", "Fais évoluer Ponyta en Galopa.", "cobblemon:fire_stone", [cob("evolve_into", 1, pokemon="rapidash")], R(600, "c")),
     Q("vol", "Vol", "Le ciel est à toi", "Attrape un Pokémon capable de voler avec toi (Dracaufeu, Roucarnage, Corvaillus…) et vole avec !", "minecraft:elytra", [catch(1, pokemon_type="flying", min_level=36), check()], R(1000, "r")),
     Q("surf", "Surf", "Traverser les océans", "Monte sur un Pokémon aquatique (Lokhlass, Wailmer…) et traverse une mer.", "minecraft:heart_of_the_sea", [catch(1, pokemon="lapras"), check()], R(1000, "r")),
     Q("plongee", "Plongée", "Sous la surface", "Plonge sous l'eau sur le dos d'un Pokémon et atteins un monument sous-marin.", "minecraft:prismarine_shard", [struct("betteroceanmonuments:ocean_monument")], R(1500, "r")),
     Q("dragon", "Chevaucheur de dragons", "Le rêve de tout dresseur", "Attrape un Dracolosse ou un Drattak et vole sur son dos.", "cobblemon:dragon_fang", [cob("obtain", 1, pokemon="dragonite"), check()], R(3000, "l"), shape="gear")],
])

# ============================================================ 6. Explorateur
explorateur = dict(file="explorateur", title="Explorateur", sub="Le monde d'en bas s'est réveillé", icon=T("explorateur"), rows=[
    [Q("descente", "La descente", "Quitter Incarnam", "Passe le halo d'Incarnam et pose le pied dans le monde d'en bas.", "minecraft:grass_block", [dim("minecraft:overworld")], R(200, "c"), size=1.5),
     Q("village", "Un village habité", "Les humains d'en bas", "Trouve un village (les villages ont été rénovés par CTOV).", "minecraft:bell", [struct("#minecraft:village")], R(300, "c")),
     Q("ctov_3", "Villages du monde", "Désert, neige, jungle", "Visite trois villages de climats différents.", "minecraft:emerald", [struct("#ctov:village_desert"), struct("#ctov:village_snowy"), struct("#ctov:village_jungle")], R(1000, "r")),
     Q("ctov_rare", "Villages rares", "Champignons et Noël", "Trouve un village champignon et un village de Noël.", "minecraft:red_mushroom_block", [struct("#ctov:village_mushroom"), struct("#ctov:village_christmas")], R(2000, "l")),
     Q("towns", "Villes et tours", "Towns and Towers", "Trouve une ville de Towns and Towers.", "minecraft:white_banner", [struct("#towns_and_towers:town")], R(800, "r")),
     Q("taverne", "Une pinte à la taverne", "Dungeons and Taverns", "Entre dans une taverne.", "minecraft:honey_bottle", [struct("#nova_structures:taverns")], R(500, "c"))],
    [Q("waystone", "Pierre de téléportation", "Ne plus jamais se perdre", "Active une Waystone dans le monde.", "waystones:waystone", [check()], R(300, "c"), deps=["descente"]),
     Q("waystone_craft", "Ta propre Waystone", "Pose-la chez toi", "Fabrique une Waystone.", "waystones:waystone", [item("waystones:waystone")], R(800, "r")),
     Q("parchemin", "Parchemin de retour", "Rentrer en un clic", "Fabrique un Parchemin de retour.", "waystones:return_scroll", [item("waystones:return_scroll")], R(400, "c")),
     Q("biomes", "Les biomes oubliés", "Oh The Biomes We've Gone", "Visite trois biomes du monde d'en bas.", "minecraft:oak_sapling", [biome("biomeswevegone:cypress_swamplands"), biome("biomeswevegone:sakura_grove"), biome("biomeswevegone:red_rock_valley")], R(1000, "r")),
     Q("biomes_rare", "Paysages de rêve", "Encore plus loin", "Visite la Prairie et l'Enchevêtrement enchanté.", "minecraft:pink_petals", [biome("biomeswevegone:prairie"), biome("biomeswevegone:enchanted_tangle")], R(1500, "r"), opt=True)],
    [Q("lootr", "Coffres partagés", "Un butin pour chacun", "Les coffres des structures (Lootr) ont un butin différent pour chaque joueur. Ouvre-en un.", "lootr:lootr_chest", [check()], R(200, "c"), deps=["descente"]),
     Q("donjon", "Le donjon", "YUNG's Better Dungeons", "Trouve un donjon amélioré.", "minecraft:spawner", [struct("#betterdungeons:better_dungeons")], R(600, "c")),
     Q("desert", "Temple du désert", "Gare aux pièges", "Explore un temple du désert amélioré.", "minecraft:sandstone", [struct("betterdeserttemples:desert_temple")], R(800, "r")),
     Q("jungle", "Temple de la jungle", "Sous les lianes", "Explore un temple de la jungle amélioré.", "minecraft:mossy_cobblestone", [struct("betterjungletemples:jungle_temple")], R(800, "r")),
     Q("sorciere", "La cabane de la sorcière", "Dans les marais", "Trouve une cabane de sorcière.", "minecraft:cauldron", [struct("betterwitchhuts:witch_hut")], R(600, "c")),
     Q("forteresse_stray", "Forteresse glacée", "Le fort des Vagabonds", "Trouve un fort des Vagabonds.", "minecraft:blue_ice", [struct("#nova_structures:stray_fort")], R(1000, "r")),
     Q("citadelle", "La citadelle solitaire", "Tout là-haut", "Trouve la citadelle solitaire.", "minecraft:deepslate_bricks", [struct("#nova_structures:lone_citadel")], R(1500, "r")),
     Q("ancienne_cite", "La Cité antique", "Silence…", "Trouve une Cité antique dans les profondeurs.", "minecraft:sculk_shrieker", [struct("#minecraft:ancient_city")], R(2500, "l"), shape="gear")],
    [Q("ruines", "Ruines", "Ce qui reste d'avant", "Trouve des ruines (Dungeons and Taverns).", "minecraft:cracked_stone_bricks", [struct("#nova_structures:remnants")], R(500, "c"), deps=["descente"]),
     Q("crypte", "La crypte", "Les morts ne dorment pas", "Explore une crypte des morts-vivants.", "minecraft:skeleton_skull", [struct("#nova_structures:undead_crypt")], R(1000, "r")),
     Q("manoir", "Le manoir des Illageois", "Une maison hostile", "Explore un manoir des Illageois.", "minecraft:totem_of_undying", [struct("#nova_structures:illager_manor")], R(1500, "r")),
     Q("sanctuaire", "Sanctuaire de combat", "Cinq épreuves", "Trouve un sanctuaire de combat.", "minecraft:iron_sword", [struct("#nova_structures:shrine")], R(1500, "r")),
     Q("explorateur_fin", "Grand explorateur", "Le monde n'a plus de secret", "Visite un village, une ville, une taverne, une crypte et une Cité antique. Valide quand tu as tout.", "minecraft:filled_map", [struct("#minecraft:village"), struct("#towns_and_towers:town"), struct("#nova_structures:taverns"), struct("#nova_structures:undead_crypt"), struct("#minecraft:ancient_city")], R(5000, "l", cmds=[cle("legendaire")]), shape="gear", size=1.5)],
])

# ============================================================ 7. Arènes & Dresseurs (les dresseurs clés sont dans les chapitres Série)
arenes = dict(file="arenes", title="Arènes & Dresseurs", sub="La route vers la Ligue", icon=T("arenes"), rows=[
    [Q("centre", "Le Centre Pokémon", "Soigner ses Pokémon", "Trouve un Centre Pokémon dans le monde et soigne ton équipe.", "cobblemon:healing_machine", [struct("cobblestructures:pokecenter")], R(200, "c"), size=1.5),
     Q("boutique", "La Boutique Pokémon", "Faire ses courses", "Trouve une Boutique Pokémon.", "cobblemon:poke_ball", [struct("cobblestructures:pokemart")], R(200, "c")),
     Q("badgebox", "Boîte à badges", "Pour ranger ta collection", "Fabrique une boîte à badges pour exposer tes futurs badges.", "badgebox:badgesbox", [item("badgebox:badgesbox")], R(400, "c")),
     Q("dresseurs_10", "Duels de route", "10 dresseurs battus", "Bats 10 dresseurs dans le monde.", "cobblemon:muscle_band", [cob("defeat_npc", 10)], R(800, "c")),
     Q("dresseurs_50", "Vétéran des routes", "50 dresseurs battus", "Bats 50 dresseurs.", "cobblemon:black_belt", [cob("defeat_npc", 50)], R(2500, "r")),
     Q("dresseurs_200", "Légende des routes", "200 dresseurs battus", "Bats 200 dresseurs.", "cobblemon:expert_belt", [cob("defeat_npc", 200)], R(6000, "l"), shape="gear")],
    [Q("stade", "Les stades de légende", "Cynthia, Peter, Pierre Rochard…", "Trouve un des grands stades Pokémon.", "minecraft:gold_ingot", [struct("cobblemonopponents:pokemon_stadium_cynthia")], R(1500, "r"), deps=["centre"]),
     Q("cynthia", "Cynthia", "La championne de Sinnoh", "Bats Cynthia dans son stade.", "cobblemon:spell_tag", [cob("defeat_npc", 1, trainers="Cynthia")], R(4000, "l")),
     Q("n_stade", "Le stade de N", "Celui qui a tout changé", "Trouve le stade de N… et affronte-le.", "minecraft:golden_helmet", [struct("cobblemonopponents:pokemon_stadium_n"), cob("defeat_npc", 1, trainers="N")], R(5000, "l"), shape="gear"),
     Q("temples", "Les quatre temples", "Sable, Neige, Orage, Soleil", "Trouve les quatre temples gardés.", "minecraft:sand", [struct("cobblemonopponents:sand_temple"), struct("cobblemonopponents:snow_temple"), struct("cobblemonopponents:storm_temple"), struct("cobblemonopponents:sun_temple")], R(4000, "l")),
     Q("manoir_hante", "Le manoir hanté", "Des voix dans les murs", "Trouve le manoir hanté.", "cobblemon:reaper_cloth", [struct("cobblemonopponents:haunted_mansion")], R(1500, "r")),
     Q("repaire_aqua", "Le repaire Aqua", "Sous la mer", "Trouve le repaire de la Team Aqua.", "minecraft:nautilus_shell", [struct("cobblemonopponents:aqua_hideout")], R(2000, "r"))],
])

# ============================================================ 8. Légendes
def leg(key, nom, poke, sub, icon, cd=5000, shape="gear"):
    return Q(key, nom, sub, f"Attrape {nom}.", icon, [catch(1, pokemon=poke)], R(cd, "l"), shape=shape)
legendes = dict(file="legendes", title="Légendes", sub="Ceux qu'Arceus a laissés derrière lui", icon=T("legendes"), rows=[
    [Q("premiere_legende", "Une présence immense", "Ton premier légendaire", "Attrape n'importe quel Pokémon légendaire.", "cobblemon:master_ball", [catch(1, form="legendary")], R(3000, "l"), size=1.5),
     Q("oiseaux", "Les oiseaux de Kanto", "Artikodin, Électhor, Sulfura", "Attrape les trois oiseaux légendaires de Kanto.", "minecraft:feather", [catch(1, pokemon=p) for p in ["articuno", "zapdos", "moltres"]], R(6000, "l"), shape="gear"),
     leg("mewtwo", "Mewtwo", "mewtwo", "Le Pokémon créé par l'homme", "cobblemon:twisted_spoon"),
     leg("lugia", "Lugia", "lugia", "Le gardien des mers", "cobblemon:mystic_water"),
     Q("lugia_obscur", "Lugia Obscur", "Une ombre dans la tempête", "Une forme obscure de Lugia rôde dans les océans pendant les orages. Attrape-la.", "minecraft:black_dye", [catch(1, pokemon="lugia", aspects="shadow")], R(8000, "l"), shape="gear", size=1.5),
     leg("hooh", "Ho-Oh", "hooh", "L'arc-en-ciel sacré", "cobblemon:fire_stone"),
     leg("rayquaza", "Rayquaza", "rayquaza", "Le seigneur du ciel", "cobblemon:dragon_scale")],
    [Q("victini", "Victini", "La Flamme de la Victoire", "Tu as allumé la flamme à Incarnam ? Attrape Victini à l'autel.", "cobblemon:fire_stone", [catch(1, pokemon="victini")], R(3000, "l"), deps=["premiere_legende"]),
     leg("reshiram", "Reshiram", "reshiram", "La Vérité", "minecraft:white_dye", 8000),
     leg("zekrom", "Zekrom", "zekrom", "L'Idéal", "minecraft:black_dye", 8000),
     Q("kyurem", "Kyurem", "La Voix…", "La Voix d'Incarnam, c'était lui. Trouve Kyurem et attrape-le.", "minecraft:blue_ice", [catch(1, pokemon="kyurem")], R(10000, "l", cmds=[cle("legendaire", 3)]), shape="gear", size=1.5),
     Q("adn", "Le Pointeur ADN", "Fusionner la glace et le feu", "Fusionne Kyurem avec Reshiram ou Zekrom grâce au Pointeur ADN.", "mega_showdown:dna_splicer", [item("mega_showdown:dna_splicer")], R(5000, "l"))],
    [Q("fabuleux", "Fabuleux", "Plus rares que les légendaires", "Attrape un Pokémon fabuleux (Mew, Celebi, Jirachi…).", "cobblemon:cherish_ball", [catch(1, form="mythical")], R(5000, "l"), deps=["premiere_legende"]),
     leg("mew", "Mew", "mew", "L'ancêtre de tous", "cobblemon:pink_apricorn"),
     leg("ultra", "Une Ultra-Chimère", "nihilego", "Venues d'ailleurs", "cobblemon:beast_ball", 4000, None),
     Q("ultra_3", "Chasseur d'Ultra-Chimères", "La Beast Ball", "Attrape 3 Ultra-Chimères avec des Beast Balls.", "cobblemon:beast_ball", [catch(3, form="ultra_beast", poke_ball_used="cobblemon:beast_ball")], R(6000, "l"), shape="gear"),
     Q("paradoxe", "Pokémon Paradoxe", "Du passé ou du futur", "Attrape un Pokémon Paradoxe.", "cobblemon:ancient_poke_ball", [catch(1, form="paradox")], R(3000, "l"))],
    [Q("fakemon", "Fakemon d'Alatias", "Des espèces inconnues", "Le monde d'en bas abrite des Pokémon que personne n'a jamais vus. Attrapes-en 3.", "cobblemon:poke_ball", [catch(3, form="fakemon")], R(1500, "r"), deps=["premiere_legende"]),
     Q("formes_caf", "Formes régionales", "Alola, Galar, Hisui, Paldea", "Attrape 4 Pokémon de forme régionale.", "cobblemon:poke_ball", [catch(1, aspects=a) for a in ["alolan", "galarian", "hisuian", "paldean"]], R(2000, "r"))],
])

# ============================================================ 9. Artisan
artisan = dict(file="artisan", title="Artisan", sub="Crafter, cuisiner, cultiver", icon=T("artisan"), rows=[
    [Q("noigrumes", "Noigrumes", "Le fruit des Poké Balls", "Récolte 10 Noigrumes de couleurs différentes.", "cobblemon:red_apricorn", [item(f"cobblemon:{c}_apricorn", 2) for c in ["red", "yellow", "green", "blue", "pink"]], R(300, "c"), size=1.5),
     Q("verger", "Le verger", "Planter les Noigrumes", "Plante des graines de Noigrume de toutes les couleurs.", "cobblemon:black_apricorn_sapling", [item(f"cobblemon:{c}_apricorn_seed") for c in ["red", "yellow", "green", "blue", "pink", "black", "white"]], R(800, "r")),
     Q("balls_speciales", "Balls spéciales", "Une Ball pour chaque situation", "Fabrique une Rapide Ball, une Sombre Ball, une Faiblo Ball et une Bis Ball.", "cobblemon:quick_ball", [item("cobblemon:" + b) for b in ["quick_ball", "dusk_ball", "nest_ball", "repeat_ball"]], R(800, "c")),
     Q("balls_kurt", "Les Balls de Kurt", "Faites main", "Fabrique une Lune Ball, une Love Ball, une Niveau Ball, une Masse Ball et une Speed Ball.", "cobblemon:moon_ball", [item("cobblemon:" + b) for b in ["moon_ball", "love_ball", "level_ball", "heavy_ball", "fast_ball"]], R(1500, "r")),
     Q("balls_anciennes", "Balls anciennes", "La technique de Hisui", "Fabrique 3 Balls anciennes : Ball Plume, Ball Jet et Ball Gigamasse.", "cobblemon:ancient_jet_ball", [item("cobblemon:ancient_feather_ball"), item("cobblemon:ancient_jet_ball"), item("cobblemon:ancient_gigaton_ball")], R(2000, "r"))],
    [Q("baies", "Baies", "La cueillette", "Récolte des baies Oran et Ceriz.", "cobblemon:oran_berry", [item("cobblemon:oran_berry", 5), item("cobblemon:cheri_berry", 5)], R(200, "c"), deps=["noigrumes"]),
     Q("marmite", "La marmite", "Cuisiner pour ses Pokémon", "Fabrique une marmite de feu de camp.", "cobblemon:campfire_pot_red", [item("cobblemon:campfire_pot_red")], R(300, "c")),
     Q("poke_snack", "Poké Snack", "Attirer les Pokémon", "Cuisine un Poké Snack et pose-le pour attirer des Pokémon.", "cobblemon:poke_snack", [item("cobblemon:poke_snack")], R(500, "c")),
     Q("poke_puff", "Poké Fête", "Les délices de Kalos", "Cuisine un Poké Puff, une Poké Cake et un Poké Appât.", "cobblemon:poke_puff", [item("cobblemon:poke_puff"), item("cobblemon:poke_cake"), item("cobblemon:poke_bait")], R(800, "r")),
     Q("aprijus", "Aprijus", "Le jus de Noigrume", "Prépare 3 Aprijus de couleurs différentes.", "cobblemon:aprijuice_red", [item("cobblemon:aprijuice_red"), item("cobblemon:aprijuice_blue"), item("cobblemon:aprijuice_yellow")], R(800, "r")),
     Q("pokeblocks", "Poképeluche", "Un doudou Évoli", "Trouve ou fabrique une Poképeluche Évoli pour décorer ta chambre.", "pokeblocks:pokedoll_eevee", [item("pokeblocks:pokedoll_eevee")], R(600, "c")),
     Q("malasada", "La Grosse Malasada", "Spécialité d'Alola", "Cuisine une Grosse Malasada.", "cobblemon:big_malasada", [item("cobblemon:big_malasada")], R(800, "r"))],
    [Q("ct_machine", "La machine à CT", "Apprendre de nouvelles capacités", "Fabrique une machine à CT.", "cobblemon:tm_machine", [item("cobblemon:tm_machine")], R(500, "c"), deps=["noigrumes"]),
     Q("ct_vierge", "CT vierges", "Prêtes à graver", "Fabrique 5 CT vierges.", "cobblemon:blank_tm", [item("cobblemon:blank_tm", 5)], R(500, "c")),
     Q("ct_gravee", "Ta première CT", "Grave une capacité", "Grave une capacité sur une CT.", "cobblemon:technical_machine", [item("cobblemon:technical_machine")], R(800, "r")),
     Q("tmcraft", "TMcraft", "Encore plus de CT", "Fabrique un disque vierge en cuivre de TMcraft : il sert à graver des CT.", "tmcraft:copper_blank_disc", [item("tmcraft:copper_blank_disc")], R(800, "r")),
     Q("gemmes", "Gemmes de type", "Pour forger des objets", "Récupère 3 gemmes de types différents.", "cobblemon:fire_gem", [item("cobblemon:fire_gem"), item("cobblemon:water_gem"), item("cobblemon:grass_gem")], R(800, "r")),
     Q("objets_combat", "Équipement de combat", "Restes, Mouchoir Choix, Orbe Vie", "Réunis trois objets tenus puissants.", "cobblemon:life_orb", [item("cobblemon:leftovers"), item("cobblemon:choice_scarf"), item("cobblemon:life_orb")], R(2500, "l"), shape="gear")],
    [Q("fossile", "Fossiles", "Le passé dans la roche", "Trouve un fossile.", "cobblemon:helix_fossil", [item("cobblemon:helix_fossil")], R(300, "c"), deps=["noigrumes"]),
     Q("analyseur", "Le labo des fossiles", "Analyseur et cuve", "Fabrique l'analyseur de fossiles et la cuve de restauration.", "cobblemon:fossil_analyzer", [item("cobblemon:fossil_analyzer"), item("cobblemon:restoration_tank")], R(800, "r")),
     Q("resurrection", "Résurrection", "Il revient à la vie", "Ressuscite un Pokémon fossile.", "cobblemon:dome_fossil", [cob("revive_fossil", 1)], R(1000, "r")),
     Q("cobbleloots", "Trésors cachés", "CobbleLoots", "Trouve un trésor de CobbleLoots dans le monde (Poké Ball abandonnée).", "cobblemon:poke_ball", [check()], R(500, "c"))],
    [Q("meubles", "Décorateur", "Une maison digne d'un dresseur", "Fabrique une table, une chaise et une étagère Handcrafted.", "handcrafted:oak_table", [item("handcrafted:oak_table"), item("handcrafted:oak_chair"), item("handcrafted:oak_shelf")], R(500, "c"), deps=["noigrumes"]),
     Q("cobblefurnies", "Mobilier Pokémon", "CobbleFurnies", "Fabrique un canapé et une lampe CobbleFurnies.", "cobblefurnies:red_sofa", [item("cobblefurnies:red_sofa"), item("cobblefurnies:red_lamp")], R(500, "c")),
     Q("pc_maison", "Un PC à la maison", "Comme au Centre", "Fabrique un PC et une machine de soin pour ta maison.", "cobblemon:pc", [item("cobblemon:pc"), item("cobblemon:healing_machine")], R(1000, "r")),
     Q("vitrine", "La vitrine", "Expose tes trésors", "Fabrique une vitrine pour exposer un objet rare.", "cobblemon:display_case", [item("cobblemon:display_case")], R(500, "c"))],
])

# ============================================================ 10. Économie
economie = dict(file="economie", title="Économie", sub="CobbleDollars, boutique et caisses", icon=T("economie"), rows=[
    [Q("premiers_cd", "Premiers CobbleDollars", "Ça s'empile vite", "Gagne de l'argent en battant des Pokémon et des dresseurs. Ouvre ton porte-monnaie avec /cobbledollars.", "cobblemon:relic_coin", [check()], R(200, "c"), size=1.5),
     Q("marchand", "Le marchand", "Le Quartier marchand d'Incarnam", "Achète un objet chez un marchand d'Incarnam.", "cobbledollars:cobble_merchant_spawn_egg", [check()], R(200, "c")),
     Q("boutique_srv", "La boutique du serveur", "/boutique", "Ouvre la boutique du serveur avec /boutique et regarde les grades et les clés.", "minecraft:emerald", [check()], R(200, "c")),
     Q("caisse", "Première caisse", "Le Sanctuaire des récompenses", "Ouvre une caisse commune au Sanctuaire des récompenses.", "minecraft:tripwire_hook", [check()], R(0, None, cmds=[cle("commune", 2)])),
     Q("caisse_rare", "Caisse rare", "Ça brille plus", "Ouvre une caisse rare.", "minecraft:tripwire_hook", [check()], R(0, None, cmds=[cle("rare")])),
     Q("caisse_leg", "Caisse légendaire", "Le jackpot", "Ouvre une caisse légendaire.", "minecraft:tripwire_hook", [check()], R(0, None, cmds=[cle("legendaire")]), shape="gear")],
    [Q("objets_chance", "Œuf Chance", "WantedItems", "Trouve un Œuf Chance rouge, vert ou bleu (WantedItems).", "wanteditems:red_lucky_egg", [item("wanteditems:red_lucky_egg")], R(500, "c"), deps=["premiers_cd"]),
     Q("capsule", "Capsule d'argent", "Entraînement ultime", "Obtiens une Capsule d'argent pour maximiser un IV.", "wanteditems:bottle_cap", [item("wanteditems:bottle_cap")], R(1000, "r")),
     Q("capsule_or", "Capsule d'or", "Tous les IVs au maximum", "Obtiens une Capsule d'or.", "wanteditems:gold_bottle_cap", [item("wanteditems:gold_bottle_cap")], R(3000, "l")),
     Q("boite_chance", "Boîte surprise", "Qu'y a-t-il dedans ?", "Ouvre une Boîte Chance Cobblemon.", "wanteditems:cobblemon_lucky_box", [item("wanteditems:cobblemon_lucky_box")], R(800, "r")),
     Q("echangeur_shiny", "Échangeur chromatique", "L'objet le plus convoité", "Obtiens un Échangeur chromatique.", "wanteditems:shiny_swapper", [item("wanteditems:shiny_swapper")], R(5000, "l"), shape="gear")],
    [Q("riche_10k", "Économe", "10 000 CobbleDollars", "Possède 10 000 CobbleDollars en même temps, puis valide (on te fait confiance !).", "cobblemon:relic_coin_pouch", [check()], R(0, "r"), deps=["premiers_cd"]),
     Q("grade_dresseur", "Grade Dresseur", "Monte en grade", "Achète le grade Dresseur à la boutique.", "minecraft:iron_ingot", [check()], R(0, "r")),
     Q("echange", "Échange entre joueurs", "Le commerce, c'est l'amitié", "Échange un Pokémon avec un autre joueur.", "cobblemon:link_cable", [cob("trade_away", 1)], R(500, "c")),
     Q("riche_100k", "Magnat", "100 000 CobbleDollars", "Possède 100 000 CobbleDollars en même temps, puis valide.", "cobblemon:relic_coin_sack", [check()], R(0, "l", cmds=[cle("legendaire")]), shape="gear")],
])

# ============================================================ 11. Nether & End
nether_end = dict(file="nether_end", title="Nether & End", sub="Au-delà des halos", icon=T("nether_end"), rows=[
    [Q("halo_nether", "Le halo de feu", "Depuis Incarnam", "Le Nether ne s'ouvre que depuis Incarnam. Traverse le halo de feu.", "minecraft:netherrack", [dim("minecraft:the_nether")], R(1000, "r"), size=1.5),
     Q("nether_pokemon", "Pokémon du Nether", "Ils aiment la chaleur", "Attrape 5 Pokémon dans le Nether.", "cobblemon:fire_stone", [catch(5, dimension="minecraft:the_nether")], R(800, "c")),
     Q("forteresse", "La forteresse", "YUNG's Better Nether Fortresses", "Trouve une forteresse du Nether.", "minecraft:nether_bricks", [struct("betterfortresses:fortress")], R(1000, "r")),
     Q("bastion", "Bastion", "Les Piglins gardent l'or", "Trouve un bastion.", "minecraft:gilded_blackstone", [struct("minecraft:bastion_remnant")], R(1000, "r")),
     Q("incendium_village", "Le village Piglin", "Incendium", "Trouve un village Piglin.", "minecraft:gold_ingot", [struct("incendium:piglin_village")], R(1500, "r")),
     Q("chateau_interdit", "Le château interdit", "Le cœur d'Incendium", "Trouve le château interdit.", "minecraft:crying_obsidian", [struct("incendium:forbidden_castle")], R(2500, "l")),
     Q("sanctum", "Le Sanctuaire", "Prière au feu", "Trouve le Sanctum d'Incendium.", "minecraft:soul_lantern", [struct("incendium:sanctum")], R(2500, "l")),
     Q("heatran", "Heatran", "Le Pokémon de la lave", "Attrape Heatran.", "minecraft:magma_block", [catch(1, pokemon="heatran")], R(6000, "l"), shape="gear")],
    [Q("halo_end", "Le halo du néant", "Depuis Incarnam", "L'End ne s'ouvre que depuis Incarnam. Traverse le halo du néant.", "minecraft:end_stone", [dim("minecraft:the_end")], R(1500, "r"), deps=["halo_nether"]),
     Q("dragon", "L'Ender Dragon", "Le gardien du néant", "Vaincs l'Ender Dragon.", "minecraft:dragon_head", [kill("minecraft:ender_dragon")], R(5000, "l", cmds=[cle("legendaire", 2)]), shape="gear", size=1.5),
     Q("end_city", "Cité de l'End", "Les Shulkers veillent", "Trouve une cité de l'End.", "minecraft:purpur_block", [struct("minecraft:end_city")], R(1500, "r")),
     Q("elytres", "Élytres", "Voler sans Pokémon", "Récupère des élytres.", "minecraft:elytra", [item("minecraft:elytra")], R(2000, "l")),
     Q("nullscape", "Le Rift", "Nullscape", "Trouve une faille (Rift) dans les îles de l'End.", "minecraft:obsidian", [struct("nullscape:rift")], R(2000, "l")),
     Q("squelette", "Squelette de dragon", "Les restes d'un géant", "Trouve un squelette de dragon dans l'End.", "minecraft:bone_block", [struct("nullscape:dragon_skeleton")], R(2000, "l")),
     Q("chateau_end", "Château de l'End", "Dungeons and Taverns", "Trouve le château de l'End.", "minecraft:end_rod", [struct("#nova_structures:end_castle")], R(2500, "l")),
     Q("deoxys", "Deoxys", "Venu de l'espace", "Attrape Deoxys.", "minecraft:end_crystal", [catch(1, pokemon="deoxys")], R(6000, "l"), shape="gear")],
])

# ============================================================ 12. Gadgets
gadgets = dict(file="gadgets", title="Gadgets", sub="Les outils du dresseur moderne", icon=T("gadgets"), rows=[
    [Q("smartphone", "Smartphone", "Le PC dans la poche", "Fabrique un Smartphone : il ouvre ton PC et soigne ton équipe à distance.", "cobblemon_smartphone:red_smartphone", [item("cobblemon_smartphone:red_smartphone")], R(800, "r"), size=1.5),
     Q("pokenav", "PokéNav", "Ne jamais se perdre", "Fabrique un PokéNav.", "cobblenav:pokenav_item_base", [item("cobblenav:pokenav_item_base")], R(500, "c")),
     Q("sac", "Sac de voyage", "Traveler's Backpack", "Fabrique un sac à dos de voyageur.", "travelersbackpack:standard", [item("travelersbackpack:standard")], R(500, "c")),
     Q("compteur", "Compteur de captures", "Le combo shiny", "Attrape 20 fois la même espèce : le compteur augmente tes chances de chromatique. Tape /counter pour voir ton combo.", "cobblemon:poke_ball", [check()], R(600, "c")),
     Q("canne", "Canne à pêche Poké", "Pêcher des Pokémon", "Fabrique une Canne Poké et pêche un Pokémon.", "cobblemon:poke_rod", [cob("reel", 1)], R(400, "c")),
     Q("multi_exp", "Multi Exp", "Tout le monde progresse", "Obtiens un Multi Exp.", "cobblemon:exp_share", [item("cobblemon:exp_share")], R(800, "r")),
     Q("oeuf_chance", "Œuf Chance", "Plus d'expérience", "Obtiens un Œuf Chance.", "cobblemon:lucky_egg", [item("cobblemon:lucky_egg")], R(1000, "r"))],
    [Q("bonbons_exp", "Bonbons Exp.", "Monter de niveau sans combattre", "Réunis des Bonbons Exp. S, M et L.", "cobblemon:exp_candy_m", [item("cobblemon:exp_candy_s"), item("cobblemon:exp_candy_m"), item("cobblemon:exp_candy_l")], R(600, "c"), deps=["smartphone"]),
     Q("niveau_50", "Niveau 50", "Un compagnon aguerri", "Fais monter un Pokémon au niveau 50.", "cobblemon:rare_candy", [cob("level_up", 1, min_level=50)], R(1000, "r")),
     Q("niveau_100", "Niveau 100", "Le sommet", "Fais monter un Pokémon au niveau 100.", "cobblemon:exp_candy_xl", [cob("level_up", 1, min_level=100)], R(3000, "l"), shape="gear"),
     Q("equipe_6", "Équipe complète", "Six niveaux 100", "Fais monter 6 Pokémon au niveau 100.", "cobblemon:exp_candy_xl", [cob("level_up", 6, min_level=100)], R(8000, "l", cmds=[cle("legendaire", 2)]), shape="gear", size=1.5)],
])

# ============================================================ 13. Journalières & hebdomadaires
J, H = 72000, 518400  # 20 h (une fois par jour) et 6 jours (une fois par semaine)
def jour(key, title, sub, desc, icon, tasks, reward, rep=J, **kw):
    return Q(key, title, sub, desc + "|§7Se renouvelle " + ("chaque jour." if rep == J else "chaque semaine."), icon, tasks, reward, deps=[], repeat=rep, **kw)
journalieres = dict(file="journalieres", title="Journalières", sub="De quoi faire chaque jour", icon=T("journalieres"), rows=[
    [jour("j_capture", "Chasse du jour", "10 captures", "Attrape 10 Pokémon.", "cobblemon:poke_ball", [catch(10)], R(300)),
     jour("j_combat", "Entraînement du jour", "15 victoires", "Bats 15 Pokémon sauvages.", "cobblemon:muscle_band", [cob("defeat", 15)], R(300)),
     jour("j_dresseur", "Duel du jour", "3 dresseurs", "Bats 3 dresseurs.", "cobblemon:black_belt", [cob("defeat_trainer", 3)], R(400)),
     jour("j_peche", "Pêche du jour", "3 prises", "Pêche 3 Pokémon avec une Canne Poké.", "cobblemon:poke_rod", [cob("reel", 3)], R(250)),
     jour("j_evolution", "Évolution du jour", "2 évolutions", "Fais évoluer 2 Pokémon.", "cobblemon:everstone", [cob("evolve", 2)], R(400)),
     jour("j_oeufs", "Couvée du jour", "2 éclosions", "Fais éclore 2 œufs.", "cobbreeding:pokemon_egg", [cob("hatch_egg", 2)], R(300)),
     jour("j_raid", "Raid du jour", "1 victoire", "Gagne un raid.", "cobblemonraiddens:raid_crystal_block", [cob("win_raid", 1)], R(500, "c"))],
    [jour("j_eau", "Pokémon Eau", "Au bord de l'eau", "Attrape 5 Pokémon de type Eau.", "cobblemon:water_stone", [catch(5, pokemon_type="water")], R(300)),
     jour("j_feu", "Pokémon Feu", "Là où il fait chaud", "Attrape 5 Pokémon de type Feu.", "cobblemon:fire_stone", [catch(5, pokemon_type="fire")], R(300)),
     jour("j_plante", "Pokémon Plante", "Dans les hautes herbes", "Attrape 5 Pokémon de type Plante.", "cobblemon:leaf_stone", [catch(5, pokemon_type="grass")], R(300)),
     jour("j_nuit", "Chasse nocturne", "Après le coucher du soleil", "Attrape 5 Pokémon la nuit.", "cobblemon:dusk_ball", [catch(5, time_min=13000, time_max=23000)], R(400)),
     jour("j_baies", "Livraison de baies", "La Pension a faim", "Donne 16 baies Oran (elles sont consommées).", "cobblemon:oran_berry", [item("cobblemon:oran_berry", 16, consume=True)], R(400)),
     jour("j_noigrumes", "Livraison de Noigrumes", "Pour l'atelier de Balls", "Donne 16 Noigrumes rouges (ils sont consommés).", "cobblemon:red_apricorn", [item("cobblemon:red_apricorn", 16, consume=True)], R(400))],
    [jour("h_captures", "Grande chasse", "100 captures dans la semaine", "Attrape 100 Pokémon.", "cobblemon:ultra_ball", [catch(100)], R(2500, "r"), rep=H, shape="hexagon", size=1.25),
     jour("h_dresseurs", "Tournée des dresseurs", "20 dresseurs", "Bats 20 dresseurs.", "cobblemon:expert_belt", [cob("defeat_trainer", 20)], R(2500, "r"), rep=H, shape="hexagon", size=1.25),
     jour("h_raids", "Semaine des raids", "5 raids 3 étoiles ou plus", "Gagne 5 raids de 3 étoiles ou plus.", "minecraft:nether_star", [cob("win_raid", 5, raid_tiers="3,4,5")], R(3000, "r"), rep=H, shape="hexagon", size=1.25),
     jour("h_shiny", "Lueur de la semaine", "Un chromatique", "Attrape un Pokémon chromatique.", "cobblemon:shiny_stone", [catch(1, shiny=True)], R(5000, "l"), rep=H, shape="gear", size=1.5),
     jour("h_safari", "Safari de la semaine", "10 captures au Safari", "Attrape 10 Pokémon avec des Safari Balls.", "cobblemon:safari_ball", [catch(10, poke_ball_used="cobblemon:safari_ball")], R(2000, "r"), rep=H, shape="hexagon", size=1.25)],
])

from series import SERIES
CHAPITRES = [mega, raids, eleveur, safari, montures, explorateur, arenes, *SERIES, legendes, artisan, economie, nether_end, gadgets, journalieres]
