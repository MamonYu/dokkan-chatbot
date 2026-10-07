import requests

url = "https://api.dokkandb.com/api/categories"

response = requests.get(
    url,
    headers={
        "Accept": "application/json",
        "Referer": "https://www.dokkandb.com/"
    }
)

print("Status:", response.status_code)
print(response.text)
