import requests

url = "https://api.dokkandb.com/api/cards-catalog-with-transformations?chunk=1&chunk_size=1000&v=1789521632.1790923291"

response = requests.get(
    url,
    headers={
        "Accept": "application/json",
        "Referer": "https://www.dokkandb.com/"
    }
)

print("Status:", response.status_code)
print(response.text)