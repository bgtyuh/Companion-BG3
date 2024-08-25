import sqlite3


def get_all_weapons():
    conn = sqlite3.connect('data/bg3_weapons.db')  # Chemin mis à jour
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM weapons;")
    weapons = cursor.fetchall()

    conn.close()
    return weapons


def search_weapons(search_term):
    conn = sqlite3.connect('data/bg3_weapons.db')  # Chemin mis à jour
    cursor = conn.cursor()

    query = "SELECT * FROM weapons WHERE name LIKE ?"
    cursor.execute(query, (f'%{search_term}%',))
    results = cursor.fetchall()

    conn.close()
    return results
