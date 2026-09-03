import sqlite3
from unit_data import all_units
try:
    conn = sqlite3.connect('dbzTeam.db')

    c = conn.cursor()

    c.execute("drop table if exists units")
    c.execute(""" CREATE TABLE IF NOT EXISTS units(
            Name_unit text,
            type_unit text,
            rarity text,
            category text,
            has_revive bool,
            id INTEGER PRIMARY KEY  

         )""")

    unit_tuples = []
    for unit in all_units:
        unit_tuples.append((unit.name , unit.type, unit.rarity, unit.category, unit.has_revive))
    c.executemany("INSERT INTO units (Name_unit, type_unit, rarity, category, has_revive) VALUES (?, ?, ?, ?, ?)", unit_tuples)
    c.execute("SELECT * FROM units")
    print(c.fetchall())
    conn.commit()


except sqlite3.Error as e:
    print(f"Database error: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("Database connection closed cleanly.")