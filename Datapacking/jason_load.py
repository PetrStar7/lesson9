import json


with open ("data.json", "r") as file:
    novy_data = json.load(file)

print(novy_data)