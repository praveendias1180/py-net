import requests

r = requests.get("https://httpbin.org/get")

print(r.status_code)
print(r.url)
print(r.text)

print("----------------------------")

data = {'somekey': 'somevalue'}
r = requests.post("https://httpbin.org/post", data = data)

print(r.status_code)
print(r.url)
print(r.text)