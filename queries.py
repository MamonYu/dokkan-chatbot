import sqlite3
import json

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


def get_categories_for_unit(unit_name):
      query = """ SELECT categories.category
                  FROM categories
                  JOIN unit_category
                  ON unit_category.category_id = categories.id
                  JOIN units
                  ON units.id = unit_category.unit_id
                  WHERE units.Name_unit = ?;
"""
      cursor.execute(query, (unit_name, ))
      rows = cursor.fetchall()

      category_name = [row[0] for row in rows]
      return category_name

def find_matches_sql(category_name, rarity, has_revive):
      query = """ SELECT units.Name_unit
                      FROM units
                      JOIN unit_category 
                      ON unit_category.unit_id = units.id 
                      JOIN categories
                      ON categories.id = unit_category.category_id 
                      WHERE categories.category = ? AND units.rarity = ? AND units.has_revive = ?;
"""
      cursor.execute(query, (category_name, rarity, has_revive,))
      rows = cursor.fetchall()

      unit_match = [row[0] for row in rows]
      return unit_match

def get_all_units_with_categories():

      query = """ SELECT *
                    FROM units
                    LEFT JOIN unit_category 
                    ON unit_category.unit_id = units.id 
                    LEFT JOIN categories
                    ON categories.id = unit_category.category_id;
"""
      
      cursor.execute(query,)

      all_units = cursor.fetchall()
     
      clean_units = {}
      for unit in all_units:
            name = unit[0]
            category = unit[8]
            if name not in clean_units:
                  if category is None:
                        clean_units[name] = []
                  else:
                       clean_units[name] = [category]
            else:
                  if category is not None:
                       clean_units[name].append(category) 

      a_new_units = [{"name": char, "categories": tags} for char , tags in clean_units.items()]
      return a_new_units


try:
    # print(get_units_by_category("Kamehameha"))
    # print(get_units_by_category('Hybird Saiyans'))
    # print(get_units_by_category("Pure Saiyans"))
    # print(get_categories_for_unit("Goku"))
    # print(find_matches_sql("Pure Saiyans" , "LR" , 0))
   my_units = get_all_units_with_categories()
   
   print(json.dumps(my_units, indent = 3))
   



except sqlite3.Error as e:
    print(f"Database error: {e}")
        
finally:
        # 6. Always clean up and close the connection
        conn.close()