import requests

card_id = 1034201

url = "https://api.dokkandb.com/api/card"

response = requests.get(
    url,
    params={"code": card_id},
    headers={
        "Accept": "application/json",
        "Referer": "https://www.dokkandb.com/"
    }
)

print("Status:", response.status_code)

data = response.json()[0]

print("\nCARD")
print("ID:", data["id"])
print("Name:", data["name"])
print("Rarity:", data["rarity"])
print("Cost:", data["cost"])

print("\nLEADER SKILL")
print(data["leader_skill"])

print("\nPASSIVE")
print(data["passive_skill_name"])
print(data["passive_skill_description"])

print("\nACTIVE SKILL")
print(data["active_skill_name"])
print(data["active_skill_effect"])

print("\nCATEGORIES")
for category in data["category_names"]:
    print("-", category)

print("\nLINKS")
for link in data["link_skill_name_1"], data["link_skill_name_2"], data["link_skill_name_3"], data["link_skill_name_4"], data["link_skill_name_5"], data["link_skill_name_6"], data["link_skill_name_7"]:
    print("-", link)