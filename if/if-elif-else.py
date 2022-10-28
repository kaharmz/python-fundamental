menus = ['Pecel lele', 'Ayam goreng', 'Ikan goreng']

choice = input(f"Select menu : ")

quantity = int(input("Enter quantity: "))

if choice == menus[0]:
    price = 16000
    total = quantity * price
    print(f'Price : {menus[0]} = {price}')
    print(f'Quantity = {price} x {quantity} = {total}')
elif choice == menus[1]:
    price = 20000
    total = quantity * price
    print(f'Price :{menus[1]} = {price}')
    print(f'Quantity = {price} x {quantity} = {total}')
elif choice == menus[2]:
    price = 22000
    total = quantity * price
    print(f'Price :{menus[2]} = {price}')
    print(f'Quantity = {price} x {quantity} = {total}')
else:
    print('Food not available, :)')
