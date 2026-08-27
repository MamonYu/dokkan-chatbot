import sqlite3
from unit_data import goku , vegeta, messi, cristiano, mbappe, halland,raditz, all_units

conn = sqlite3.connect('dbzTeam.db')

c = conn.cursor()

# c.execute("drop table if exists units")
c.execute(""" CREATE TABLE IF NOT EXISTS units(
            Name_unit text,
            type_unit text,
            rarity text,
            category text,
            has_revive bool,
            id INTEGER PRIMARY KEY  

         )""")


c.executemany("INSERT INTO units (Name_unit, type_unit, rarity, category, has_revive) VALUES (?, ?, ?, ?, ?)", all_units)
c.execute("SELECT * FROM units")
print(c.fetchall())
conn.commit()

conn.close()