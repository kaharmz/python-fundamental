food = [
    'Ayam goreng',
    'Nasi Goreng',
    'Pecel Ayam',
    'Burger',
    'Pizza',
    'Kebab',
    'Sate ayam',
    'Bubur ayam',
    'Gorengan',
    'Lontong sayur',
    'Siomay',
]

price = [
    '21000',
    '14000',
    '18000',
    '45000',
    '87000',
    '25000',
    '26000',
    '12000',
    '2500',
    '15000',
    '17000'
]

merger = [
    list(i)
    for i in zip(food, price)
]

for j in merger:
    print(j)




