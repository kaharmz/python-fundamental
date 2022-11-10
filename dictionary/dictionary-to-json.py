import json

menus = {
    "foods": {
        "Pecel lele": 16000,
        "Pecel ayam": 20000,
        "Ikan goreng": 25000,
        "Sate usus": 4000,
        "Sate atiampla": 400,
        "Nasi": {
            "Nasi uduk": 7000,
            "Nasi biasa": 5000
        }
    },
    "drinks": {
        "Es jeruk": 7000,
        "Es Teh manis": 6000,
        "Teh tawar": 4000,
        "Air putih": "Gratis"
    }
}

with open('menus.json', 'w') as file:
    json.dump(menus, file)

