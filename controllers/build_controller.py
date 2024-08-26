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


def get_subclasses(class_name):
    """Récupère les sous-classes disponibles pour une classe donnée."""
    conn = sqlite3.connect('data/bg3_classes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM subclasses WHERE class_name = ?", (class_name,))

    subclasses = [row[0] for row in cursor.fetchall()]

    conn.close()

    return subclasses


def get_classes_with_images():
    """Récupère toutes les classes avec les chemins d'accès des images."""
    conn = sqlite3.connect('data/bg3_classes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, image_path FROM classes")
    classes = cursor.fetchall()

    conn.close()
    return classes

def get_subclasses_with_images(class_name):
    """Récupère les sous-classes avec les chemins d'accès des images pour une classe donnée."""
    conn = sqlite3.connect('data/bg3_classes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, image_path FROM subclasses WHERE class_name = ?", (class_name,))
    subclasses = cursor.fetchall()

    conn.close()
    return subclasses


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


def save_build_to_db(race_name, class_name, subclass_name, weapon_name, armor_name, footwear_name):
    """Sauvegarde un build dans la base de données en utilisant les noms des items.

    Arguments:
        race_name (str): Le nom de la race sélectionnée.
        class_name (str): Le nom de la classe sélectionnée.
        subclass_name (str): Le nom de la sous-classe sélectionnée.
        weapon_name (str): Le nom de l'arme sélectionnée.
        armor_name (str): Le nom de l'armure sélectionnée.
        footwear_name (str): Le nom des bottes sélectionnées.
    """
    conn = sqlite3.connect('data/bg3_builds.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO builds (race_name, class_name, subclass_name, weapon_name, armor_name, footwear_name)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (race_name, class_name, subclass_name, weapon_name, armor_name, footwear_name))

    conn.commit()
    conn.close()


def get_all_builds():
    """Récupère tous les builds et ajoute les chemins d'accès des images des classes et sous-classes à partir d'une autre base de données."""
    try:
        # Connexion à la base de données des builds
        conn_builds = sqlite3.connect('data/bg3_builds.db')
        cursor_builds = conn_builds.cursor()

        # Connexion à la base de données des classes
        conn_classes = sqlite3.connect('data/bg3_classes.db')
        cursor_classes = conn_classes.cursor()

        # Récupérer les builds
        cursor_builds.execute('''
            SELECT id, race_name, class_name, subclass_name, weapon_name, armor_name, footwear_name
            FROM builds
        ''')
        builds = cursor_builds.fetchall()

        # Ajouter les images des classes et sous-classes
        builds_with_images = []
        for build in builds:
            class_name = build[2]
            subclass_name = build[3]

            # Récupérer l'image de la classe
            cursor_classes.execute('SELECT image_path FROM classes WHERE name = ?', (class_name,))
            class_image_path = cursor_classes.fetchone()

            # Récupérer l'image de la sous-classe
            cursor_classes.execute('SELECT image_path FROM subclasses WHERE name = ? AND class_name = ?', (subclass_name, class_name))
            subclass_image_path = cursor_classes.fetchone()

            builds_with_images.append(
                build + (class_image_path[0] if class_image_path else None, subclass_image_path[0] if subclass_image_path else None)
            )

        return builds_with_images

    except sqlite3.Error as e:
        print(f"Une erreur s'est produite lors de l'exécution de la requête SQL : {e}")
        return []

    finally:
        if conn_builds:
            conn_builds.close()
        if conn_classes:
            conn_classes.close()


def delete_build(build_id):
    """Supprime un build de la base de données."""
    conn = sqlite3.connect('data/bg3_builds.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM builds WHERE id = ?", (build_id,))

    conn.commit()
    conn.close()


def update_build(build_id, race_name, class_name, subclass_name, weapon_name, armor_name, footwear_name):
    """Met à jour un build dans la base de données."""
    conn = sqlite3.connect('data/bg3_builds.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE builds
        SET race_name = ?, class_name = ?, subclass_name = ?, weapon_name = ?, armor_name = ?, footwear_name = ?
        WHERE id = ?
    ''', (race_name, class_name, subclass_name, weapon_name, armor_name, footwear_name, build_id))

    conn.commit()
    conn.close()