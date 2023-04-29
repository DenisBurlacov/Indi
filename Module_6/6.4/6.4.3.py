sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125
}

for key in ('name', 'calories', 'id'):
    print(sweet[key])


print(sweet["name"])
print(sweet["calories"])
print(sweet["id"])