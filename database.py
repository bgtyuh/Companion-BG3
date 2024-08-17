import sqlite3

def create_connection():
    """Crée une connexion à la base de données SQLite."""
    conn = sqlite3.connect("bg3_companion.db")
    return conn

def create_tables():
    """Crée les tables nécessaires dans la base de données."""
    conn = create_connection()
    cursor = conn.cursor()

    # Table pour les builds de personnages
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS builds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            race TEXT,
            class TEXT,
            subclass TEXT,
            notes TEXT
        )
    ''')

    # Table pour les niveaux dans chaque build
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS build_levels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            build_id INTEGER,
            level INTEGER,
            spells TEXT,
            feats TEXT,
            subclass_choice TEXT,
            multiclass_choice TEXT,
            FOREIGN KEY (build_id) REFERENCES builds(id)
        )
    ''')

    # Table pour les items dans le jeu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT,
            region TEXT,
            description TEXT,
            is_collected BOOLEAN NOT NULL CHECK (is_collected IN (0, 1))
        )
    ''')

    # Table pour les ennemis
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enemies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            stats TEXT,
            resistances TEXT,
            weaknesses TEXT,
            abilities TEXT,
            notes TEXT
        )
    ''')

    # Table pour les armures et accessoires
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS armors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT,
            armor_class INTEGER,
            bonus TEXT,
            location TEXT,
            is_favorite BOOLEAN NOT NULL CHECK (is_favorite IN (0, 1)),
            is_owned BOOLEAN NOT NULL CHECK (is_owned IN (0, 1))
        )
    ''')

    conn.commit()
    conn.close()

def insert_build(name, race, class_, subclass, notes):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO builds (name, race, class, subclass, notes)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, race, class_, subclass, notes))

    conn.commit()
    build_id = cursor.lastrowid  # Récupère l'ID du build créé
    conn.close()
    return build_id

def insert_build_level(build_id, level, spells, feats, subclass_choice, multiclass_choice):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO build_levels (build_id, level, spells, feats, subclass_choice, multiclass_choice)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (build_id, level, spells, feats, subclass_choice, multiclass_choice))

    conn.commit()
    conn.close()

def insert_item(name, type_, region, description, is_collected=False):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO items (name, type, region, description, is_collected)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, type_, region, description, int(is_collected)))

    conn.commit()
    conn.close()

def insert_enemy(name, stats, resistances, weaknesses, abilities, notes):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO enemies (name, stats, resistances, weaknesses, abilities, notes)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, stats, resistances, weaknesses, abilities, notes))

    conn.commit()
    conn.close()

def insert_armor(name, type_, armor_class, bonus, location, is_favorite=False, is_owned=False):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO armors (name, type, armor_class, bonus, location, is_favorite, is_owned)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, type_, armor_class, bonus, location, int(is_favorite), int(is_owned)))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()

    # Ajouter un build
    build_id = insert_build("Build Guerrier", "Humain", "Guerrier", "Champion", "Build axé sur les attaques critiques.")

    # Ajouter des niveaux pour ce build
    insert_build_level(build_id, 1, "Attaque puissante", "Aucun", "Champion", "Aucun")
    insert_build_level(build_id, 2, "Attaque rapide", "Aucun", "Champion", "Aucun")
    insert_build_level(build_id, 3, "Maîtrise des armes", "Aucun", "Champion", "Aucun")
    insert_build_level(build_id, 4, "Aucun", "Force augmentée", "Champion", "Aucun")
    # Continue pour les niveaux 5 à 12...

    # Ajouter un autre build
    build_id = insert_build("Build Mage", "Elfe", "Sorcier", "Évocation", "Build avec un focus sur les sorts de zone.")

    # Ajouter des niveaux pour ce build
    insert_build_level(build_id, 1, "Boule de feu", "Aucun", "Évocation", "Aucun")
    insert_build_level(build_id, 2, "Bouclier magique", "Aucun", "Évocation", "Aucun")
    insert_build_level(build_id, 3, "Rayon ardent", "Aucun", "Évocation", "Aucun")
    insert_build_level(build_id, 4, "Aucun", "Augmentation de l'Intelligence", "Évocation", "Aucun")
    # Continue pour les niveaux 5 à 12...
