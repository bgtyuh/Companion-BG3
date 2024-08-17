from database import create_connection

def get_all_builds():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, race, class, subclass FROM builds")
    builds = cursor.fetchall()

    conn.close()
    return builds

def get_build_levels(build_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT level, spells, feats, subclass_choice, multiclass_choice FROM build_levels WHERE build_id = ?", (build_id,))
    levels = cursor.fetchall()

    conn.close()
    return levels
