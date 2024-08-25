import sqlite3


def get_all_weapons():
    """Récupère toutes les armes depuis la base de données.

    Retourne:
        list: Une liste de tuples contenant les détails de chaque arme.
    """
    conn = sqlite3.connect('data/bg3_weapons.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM weapons;")
    weapons = cursor.fetchall()

    conn.close()
    return weapons


def get_weapon_details(weapon_id, detail_type):
    """Récupère les détails spécifiques d'une arme depuis la base de données.

    Arguments:
        weapon_id (int): L'ID de l'arme pour laquelle récupérer les détails.
        detail_type (str): Le type de détail à récupérer (Damages, Notes, etc.).

    Retourne:
        str: Les détails sous forme de texte.
    """
    conn = sqlite3.connect('data/bg3_weapons.db')
    cursor = conn.cursor()

    if detail_type == "Damage":
        cursor.execute("SELECT * FROM Damage WHERE weapon_id = ?", (weapon_id,))
    elif detail_type == "Notes":
        cursor.execute("SELECT * FROM Notes WHERE weapon_id = ?", (weapon_id,))
    elif detail_type == "Special Abilities":
        cursor.execute("SELECT * FROM Special_Abilities WHERE weapon_id = ?", (weapon_id,))
    elif detail_type == "Weapon Actions":
        cursor.execute("SELECT * FROM Weapon_Actions WHERE weapon_id = ?", (weapon_id,))
    elif detail_type == "Weapon Locations":
        cursor.execute("SELECT * FROM Weapon_Locations WHERE weapon_id = ?", (weapon_id,))

    details = cursor.fetchall()
    conn.close()

    # Construire une chaîne de texte à partir des détails récupérés
    detail_text = "\n".join([str(detail) for detail in details])
    return detail_text
