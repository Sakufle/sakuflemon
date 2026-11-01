# Générateur des quêtes Sakuflemon (chapitres « mods »)

- `chapitres.py` : contenu des 12 chapitres (textes, tâches, récompenses, icônes).
- `quetes_mods.py <quests existant> <sortie>` : copie le dossier `config/ftbquests/quests` actuel et ajoute les chapitres + les textes dans `lang/en_us.snbt`. Les ID sont stables (hash des clés) : relancer garde la progression.
- `icones.py <dossier>` : dessine les 12 icônes de chapitre (32x32), copiées dans `sakuflemon-interface.zip` (`assets/sakuflemon/textures/quetes/`).

Installation : serveur ARRÊTÉ, sauvegarder `config/ftbquests/quests`, remplacer par `serveur/ftbquests/quests`, redémarrer.
Tous les ID d'items ont été vérifiés dans les jars du pack (Prism de Lucas, 2026-10-31).
