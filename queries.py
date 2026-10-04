import sqlite3

def get_units_by_category(category_name):
    conn = sqlite3.connect('dbzTeam.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    query = """ SELECT units.Name_unit
                FROM units
                JOIN unit_category 
                ON unit_category.unit_id = units.id 
                JOIN categories
                ON categories.id = unit_category.category_id 
                WHERE categories.category = ?;
    """
    cursor.execute(query, (category_name,))
    rows = cursor.fetchall()
    conn.close()

    return [row[0] for row in rows]


def get_categories_for_unit(unit_name):
    conn = sqlite3.connect('dbzTeam.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    query = """ SELECT categories.category
                FROM categories
                JOIN unit_category
                ON unit_category.category_id = categories.id
                JOIN units
                ON units.id = unit_category.unit_id
                WHERE units.Name_unit = ?;
    """
    cursor.execute(query, (unit_name,))
    rows = cursor.fetchall()
    conn.close()

    return [row[0] for row in rows]


def find_matches_sql(category_name, rarity, has_revive):
    conn = sqlite3.connect('dbzTeam.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    query = """ SELECT units.Name_unit
                FROM units
                JOIN unit_category 
                ON unit_category.unit_id = units.id 
                JOIN categories
                ON categories.id = unit_category.category_id 
                WHERE categories.category = ? AND units.rarity = ? AND units.has_revive = ?;
    """
    cursor.execute(query, (category_name, rarity, has_revive))
    rows = cursor.fetchall()
    conn.close()

    return [row[0] for row in rows]


def get_all_units_with_categories():
    conn = sqlite3.connect('dbzTeam.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    query = """ SELECT *
                FROM units
                LEFT JOIN unit_category 
                ON unit_category.unit_id = units.id 
                LEFT JOIN categories
                ON categories.id = unit_category.category_id;
    """
    cursor.execute(query)
    all_units = cursor.fetchall()
    conn.close()

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
            clean_units[name].append(category)

    return [{"name": name, "categories": tags} for name, tags in clean_units.items()]


if __name__ == "__main__":
    print(get_units_by_category("Kamehameha"))
    print(get_categories_for_unit("Goku"))
    print(find_matches_sql("Pure Saiyans", "LR", True))
    print(get_all_units_with_categories())