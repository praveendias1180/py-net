import json
myVar = '{"name": "Bob", "languages": ["English", "French"]}'

loaded = json.loads(myVar)

print(len(loaded))