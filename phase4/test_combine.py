import requests

url = "https://api.dokkandb.com/api/categories"

response = requests.get(url)

categories = response.json()

category_lookup = {item['id']: item['name'] for item in categories}

rarity_lookup = {
    0: "N",
    1: "R",
    2: "SR",
    3: "SSR",
    4: "UR",
    5: "LR"
}
element_lookup = {
    10: "Super STR",
    11: "Super AGL",
    12: "Super TEQ",
    13: "Super INT",
    14: "Super PHY",
    20: "Extreme STR",
    21: "Extreme AGL",
    22: "Extreme TEQ",
    23: "Extreme INT",
    24: "Extreme PHY"
}


# print(category_lookup[32])


url_cards = "https://api.dokkandb.com/api/cards-catalog-with-transformations"


response1 = requests.get(
    url_cards,
    params={
        "chunk": 1,
        "chunk_size": 1000
    }
)

print("resp1", "Status:", response1.status_code)

cards = response1.json()

data1 = response1.json()
print("Response type:", type(cards))
print("Number of cards:", len(cards))


response2 = requests.get(
    url_cards,
    params = {
        "chunk" : 2,
        "chunk_size": 1000
    }
)
data2 = response2.json()

print("resp2" , "Status:", response2.status_code)

# check if all cards are unique
seen_ids = set()
all_cards = []

for card in data1 + data2:
    if card['real_id'] not in seen_ids:
        all_cards.append(card)
        seen_ids.add(card['real_id']) # track the id so it wont duplicate








print("number of all cards:",len(all_cards))
print("before dedupe:", len(data1 + data2))
print("after dedupe: ", len(all_cards))

# ids1 = {card['id'] for card in data1}
# ids2 = {card['id'] for card in data2}

# print("chunk 1: cards =", len(data1), "| unique ids =", len(ids1))
# print("chunk 2: cards =", len(data2), "| unique ids =", len(ids2))
# print("ids in both chunks:", len(ids1 & ids2))

# from collections import Counter

# counts = Counter(card['id'] for card in data2)
# dupe_ids = [card_id for card_id, n in counts.items() if n > 1]

# print("ids that repeat:", len(dupe_ids))
# print("first few:", dupe_ids[:5])

# example_id = dupe_ids[0]
# rows = [card for card in data2 if card['id'] == example_id]

# print("example id:", example_id, "| name:", rows[0]['name'])
# print("rows for that id:", len(rows))
# print("rows identical?", rows[0] == rows[1])

# a, b = rows[0], rows[1]

# for key in a:
#     if a[key] != b.get(key):
#         print(key, "->", str(a[key])[:60], "|", str(b.get(key))[:60])
        
# Get the category IDs from the first card

for index, sample in enumerate(all_cards, start=1):

    print(f"\n------- Unit {index}-----")

    print("Name:", sample.get('name', 'Unknown name'))

    rarity_id = sample.get("rarity")
    rarity_name = rarity_lookup.get(
        rarity_id, f"Unknown rarity({rarity_id}))"
        )
    print("Rarity:", rarity_name)

    element_id = sample.get('element')
    element_name = element_lookup.get(
        element_id, f"Unknown element({element_id})"
    )

    print("Element:" , element_name)

    # Categories
    print("Categories:")

    category_ids = sample.get("category_ids") or []

    for category_id in category_ids:
        category_name = category_lookup.get(
            category_id, "Unknown category"
            )
        print("-", category_name)
