import sqlite3


def get_all_armours():
    """Récupère toutes les armes depuis la base de données.

    Retourne:
        list: Une liste de tuples contenant les détails de chaque arme.
    """
    conn = sqlite3.connect('data/bg3_armours.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items;")
    armours = cursor.fetchall()

    conn.close()
    return armours


def get_armour_details(armour_id, detail_type):
    """Récupère les détails spécifiques d'une arme depuis la base de données.

    Arguments:
        armour_id (int): L'ID de l'arme pour laquelle récupérer les détails.
        detail_type (str): Le type de détail à récupérer (Damages, Notes, etc.).

    Retourne:
        str: Les détails sous forme de texte.
    """
    conn = sqlite3.connect('data/bg3_armours.db')
    cursor = conn.cursor()

    if detail_type == "Armour":
        cursor.execute("SELECT * FROM Items WHERE item_id = ?", (armour_id,))
    elif detail_type == "Locations":
        cursor.execute("SELECT * FROM Locations WHERE item_id = ?", (armour_id,))
    elif detail_type == "Specials":
        cursor.execute("SELECT * FROM Specials WHERE item_id = ?", (armour_id,))

    details = cursor.fetchall()
    conn.close()

    # Construire une chaîne de texte à partir des détails récupérés
    detail_text = "\n".join([str(detail) for detail in details])
    return detail_text
