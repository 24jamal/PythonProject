import requests

urls = [
    "https://google.com",
    "https://github.com",
]

for url in urls:
    response = requests.get(url)
    print(response.status_code)