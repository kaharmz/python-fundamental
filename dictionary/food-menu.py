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

print('Silahkan pilih menu yang kalian suka')
food = str(input('Silahkan pilih makanan: '))
drink = input('Silahkan pilih minuman: ')
jumlah_makanan = int(input('Masukan jumlah makanan: '))
jumlah_minuman = int(input('Masukan jumlah minuman: '))

#compare key in dictionary with input
if food in menus['foods'] and drink in menus['drinks']:
    harga_makanan = menus['foods'][food]
    harga_minuman = menus['drink'][drink]
    total_makanan = harga_makanan * jumlah_makanan
    total_minuman = harga_minuman * jumlah_minuman
    total_pesanan = total_makanan + total_minuman
    print(f'Total pesanan = {total_pesanan}')
else:
    print(f'Menu not available')







#pesanan = [makanan, minuman, jumlah_makanan, jumlah_minuman]









