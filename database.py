import sqlite3

def create_builds_table():
    """Crée une table pour stocker les builds dans la base de données."""
    conn = sqlite3.connect('data/bg3_builds.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS builds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            race_name TEXT,
            class_name TEXT,
            weapon_name TEXT,
            armor_name TEXT,
            footwear_name TEXT
        )
    ''')

    conn.commit()
    conn.close()

def drop_table(table_name):
    """Supprime une table de la base de données.

    Arguments:
        table_name (str): Le nom de la table à supprimer.
    """
    try:
        conn = sqlite3.connect('data/bg3_builds.db')  # Assure-toi que le chemin pointe vers la bonne base de données
        cursor = conn.cursor()

        # Exécuter la commande pour supprimer la table
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

        conn.commit()
        print(f"La table '{table_name}' a été supprimée avec succès.")
    except sqlite3.Error as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    drop_table("builds")
    create_builds_table()