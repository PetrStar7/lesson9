import json

data = input("Zadej Jméno:")
data2 = input("Zadej Věk:")

with open ("data.json", "w") as file: #w / to vždycky přepíše a udělá novej
    json.dump(data, file)

with open ("data.json", "a") as file: # a - přidá na konec další 
    json.dump(data2, file)
