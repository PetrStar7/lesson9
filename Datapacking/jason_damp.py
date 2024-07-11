import json

data = ("Franta", "Tonda", "Pepík", "Šašíček")

with open ("data.json", "w") as file:
    json.dump(data, file)

