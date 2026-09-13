import sqlite3
from unit_data import all_units
try:
    conn = sqlite3.connect('dbzTeam.db')

    c = conn.cursor()

    c.execute("PRAGMA foreign_keys = ON;")

    c.execute("drop table if exists units")
    c.execute(""" CREATE TABLE IF NOT EXISTS units(
            Name_unit text,
            type_unit text,
            rarity text,
            category text,
            has_revive bool,
            id INTEGER PRIMARY KEY  

         )""")

    c.execute("drop table if exists categories")
    c.execute(""" CREATE TABLE IF NOT EXISTS categories(
                category text,
                id INTEGER PRIMARY KEY
    
    
    
    ) """)
    c.execute("drop table if exists unit_category")
    c.execute(""" CREATE TABLE IF NOT EXISTS unit_category(
                    unit_id INTEGER,
                    category_id INTEGER,
                    foreign key (unit_id) references units (id),
                    foreign key (category_id) references categories (id)
    
    ) """)

    unit_tuples = []
    for unit in all_units:
        unit_tuples.append((unit.name , unit.type, unit.rarity, unit.category, unit.has_revive))
    c.executemany("INSERT INTO units (Name_unit, type_unit, rarity, category, has_revive) VALUES (?, ?, ?, ?, ?)", unit_tuples)
    c.execute("INSERT INTO categories VALUES ('Pure Saiyans',1),('Hybird Saiyans',2),('Fusion',3),('Fused Fighter',4),('Potara',5),('Free Saiyans',6),('Kamehameha',7),('Fierce Battle',8),('Goku''s Family',9);")
    c.execute("INSERT INTO unit_category VALUES (1,1),(1,7),(1,8),(1,9),(2,1),(2,5),(2,8),(4,2),(4,6),(4,7);")
    c.execute("SELECT * FROM units")
    print(c.fetchall())
    conn.commit()


except sqlite3.Error as e:
    print(f"Database error: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("Database connection closed cleanly.")