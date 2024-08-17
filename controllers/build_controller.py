from database import create_connection

def add_build(build):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO builds (name, race, class, subclass, level, notes) VALUES (?, ?, ?, ?, ?, ?)",
                   (build.name, build.race, build.class_, build.subclass, build.level, build.notes))

    conn.commit()
    conn.close()

def get_all_builds():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, race, class, subclass, level FROM builds")
    builds = cursor.fetchall()

    conn.close()
    return builds