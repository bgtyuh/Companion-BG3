import sqlite3


def get_races():
    """Récupère toutes les races de la base de données."""
    conn = sqlite3.connect('data/bg3_races.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM races")
    races = cursor.fetchall()

    conn.close()
    return races


def get_classes():
    """Récupère toutes les classes de la base de données."""
    conn = sqlite3.connect('data/bg3_classes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM classes")
    classes = cursor.fetchall()

    conn.close()
    return classes


def get_weapons():
    """Récupère toutes les armes de la base de données."""
    conn = sqlite3.connect('data/bg3_weapons.db')
    cursor = conn.cursor()

    cursor.execute("SELECT weapon_id, name FROM weapons")
    weapons = cursor.fetchall()

    conn.close()
    return weapons


def get_armors():
    """Récupère toutes les armures de la base de données."""
    conn = sqlite3.connect('data/bg3_armours.db')
    cursor = conn.cursor()

    cursor.execute("SELECT item_id, name FROM items")
    armors = cursor.fetchall()

    conn.close()
    return armors


def get_footwears():
    """Récupère toutes les bottes de la base de données."""
    conn = sqlite3.connect('data/bg3_footwears.db')
    cursor = conn.cursor()

    cursor.execute("SELECT item_id, name FROM items")
    footwears = cursor.fetchall()

    conn.close()
    return footwears


def save_build_to_db(race_name, class_name, weapon_name, armor_name, footwear_name):
    """Sauvegarde un build dans la base de données en utilisant les noms des items.

    Arguments:
        race_name (str): Le nom de la race sélectionnée.
        class_name (str): Le nom de la classe sélectionnée.
        weapon_name (str): Le nom de l'arme sélectionnée.
        armor_name (str): Le nom de l'armure sélectionnée.
        footwear_name (str): Le nom des bottes sélectionnées.
    """
    conn = sqlite3.connect('data/bg3_builds.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO builds (race_name, class_name, weapon_name, armor_name, footwear_name)
        VALUES (?, ?, ?, ?, ?)
    ''', (race_name, class_name, weapon_name, armor_name, footwear_name))

    conn.commit()
    conn.close()


def get_all_builds():
    """Récupère tous les builds depuis la base de données."""
    conn = sqlite3.connect('data/bg3_builds.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM builds")
    builds = cursor.fetchall()

    conn.close()
    return builds


def delete_build(build_id):
    """Supprime un build de la base de données."""
    conn = sqlite3.connect('data/bg3_builds.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM builds WHERE id = ?", (build_id,))

    conn.commit()
    conn.close()


def update_build(build_id, race_name, class_name, weapon_name, armor_name, footwear_name):
    """Met à jour un build dans la base de données."""
    conn = sqlite3.connect('data/bg3_builds.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE builds
        SET race_name = ?, class_name = ?, weapon_name = ?, armor_name = ?, footwear_name = ?
        WHERE id = ?
    ''', (race_name, class_name, weapon_name, armor_name, footwear_name, build_id))

    conn.commit()
    conn.close()