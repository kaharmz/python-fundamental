
choice = input(f"Select menu : ")

menus = ['Pecel lele', 'Ayam goreng', 'Ikan goreng']

quantity = int(input("Enter quantity: "))

discount = 10000

if choice == menus[0]:
    if quantity < 6:
        price = 16000
        total = quantity * price
        print(f'Price : {menus[0]} = {price}')
        print(f'Quantity = {price} x {quantity} = {total}')
    elif quantity > 6:
        price = 16000
        total = (quantity * price) - discount
        print(f'Price : {menus[0]} = {price}')
        print(f'Order quantity = {price} x {quantity} - {discount} = {total}')
elif choice == menus[1]:
    if quantity < 6:
        price = 20000
        total = quantity * price
        print(f'Price : {menus[1]} = {price}')
        print(f'Quantity = {price} x {quantity} = {total}')
    elif quantity > 6:
        price = 20000
        total = (quantity * price) - discount
        print(f'Price : {menus[1]} = {price}')
        print(f'Quantity = {price} x {quantity} - {discount} = {total}')
elif choice == menus[2]:
    if quantity < 6:
        price = 25000
        total = quantity * price
        print(f'Price : {menus[2]} = {price}')
        print(f'Quantity = {price} x {quantity} = {total}')
    elif quantity > 6:
        price = 25000
        total = (quantity * price) - discount
        print(f'Price : {menus[2]} = {price}')
        print(f'Quantity = {price} x {quantity} - {discount} = {total}')
else:
    print("Please select menu :)")




