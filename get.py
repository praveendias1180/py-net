import requests

BASE_URL = 'http://host1.open.uom.lk:8080'
BASE_URL = 'https://jsonplaceholder.typicode.com/users'
# response = requests.get(f"{BASE_URL}/api/products")
response = requests.get(BASE_URL)

dict = response.json()

print(len(dict))