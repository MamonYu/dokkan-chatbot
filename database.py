import sqlite3
# from test_practice import Team

conn = sqlite3.connect('dbzTeam.db')

c = conn.cursor()

# c.execute("drop table if exists units")
# c.execute(""" CREATE TABLE units(
#             Name_unit text,
#             type_unit text,
#             rarity text,
#             category text,
#             has_revive bool,
#             id integer primary key

#          )""")


# c.execute(""" insert into units
#            vallues() 

         
#          """)


c.execute("SELECT * FROM units")
print(c.fetchall())
conn.commit()

conn.close()