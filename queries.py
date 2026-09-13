import sqlite3

conn = sqlite3.connect('dbzTeam.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

def get_units_by_category(category_name):
      query =  """ SELECT units.Name_unit
                      FROM units
                      JOIN unit_category 
                      ON unit_category.unit_id = units.id 
                      JOIN categories
                      ON categories.id = unit_category.category_id 
                      WHERE categories.category = ?;
"""
      cursor.execute(query, (category_name,))
      rows = cursor.fetchall()

      unit_name = [row[0] for row in rows]
      return unit_name      

try:
    print(get_units_by_category("Kamehameha"))
    print(get_units_by_category('Hybird Saiyans'))
    print(get_units_by_category("Pure Saiyans"))

except sqlite3.Error as e:
    print(f"Database error: {e}")
        
finally:
        # 6. Always clean up and close the connection
        conn.close()