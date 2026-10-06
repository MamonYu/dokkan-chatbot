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

print(response.text)