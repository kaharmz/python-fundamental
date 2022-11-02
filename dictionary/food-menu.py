#dictionary
menus = {
    'foods': {
        'Pecel lele': 14000,
        'Ayam goreng': 18000,
        'Ikan goreng': 20000,
    },
    'drinks': {
        'Es teh manis': 4000,
        'Es teh tawar': 3000,
        'Es jeruk': 7000,
    },
}

#displaying menu
for types, menu in menus.items():
    for key in menu:
        print(key + ' =', menu[key])

print('Select menu')
food = str(input('Choose food: '))
drink = input('Choose a drink: ')
food_amount = int(input('Food amount: '))
drink_amount = int(input('Drink amount: '))

#compare key in dictionary with input
if food in menus['foods'] and drink in menus['drinks']:
    #access value foods
    food_price = menus['foods'][food]
    #access value drink
    drink_price = menus['drink'][drink]
    total_food = food_price * food_amount
    total_drink = drink_price * drink_amount
    total_order = total_food + total_drink
    print(f'Total order = {total_order}')
else:
    print(f'Menu not available')










