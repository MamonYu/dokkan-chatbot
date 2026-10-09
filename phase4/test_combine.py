import requests

url = "https://api.dokkandb.com/api/categories"

response = requests.get(url)

categories = response.json()

category_lookup = {item['id']: item['name'] for item in categories}

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

all_cards = data1 + data2

print("number of all cards:",len(all_cards))


sample = all_cards[0]

print("Name:" , sample.get("name"))
print("Rarity:" , sample.get("rarity"))
print("Element:" , sample.get("element"))


# Get the category IDs from the first card
category_ids = sample.get("category_ids", [])

print("Categories:")

for category_id in category_ids:
    category_name = category_lookup.get(category_id, "Unknown category")
    print(category_name)