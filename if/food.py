
choice = input(f"Select menu : ")

foods = ['Pecel lele', 'Ayam goreng', 'Ikan goreng']

inputs = int(input("Enter quantity: "))

discount = 10000

if choice == foods[0]:
    if inputs < 6:
        price = 16000
        total = inputs * price
        print(f'{foods[0]} == {price}')
        print(f'Order quantity = {foods[0]} x {inputs} = {total}')
    elif inputs > 6:
        price = 16000
        total = (inputs * price) - discount
        print(f'Order quantity = {foods[0]} x {inputs} - {discount} = {total}')
elif choice == foods[1]:
    if inputs < 6:
        price = 20000
        total = inputs * price
        print(f'{foods[1]} == {price}')
        print(f'Order quantity = {foods[1]} x {inputs} = {total}')
    elif inputs > 6:
        price = 20000
        total = (inputs * price) - discount
        print(f'{foods[1]} == {price}')
        print(f'Order quantity = {foods[1]} x {inputs} - {discount} = {total}')
elif choice == foods[2]:
    if inputs < 6:
        price = 25000
        total = inputs * price
        print(f'{foods[2]} == {price}')
        print(f'Order quantity = {foods[2]} x {inputs} = {total}')
    elif inputs > 6:
        price = 25000
        total = (inputs * price) - discount
        print(f'{foods[2]} == {price}')
        print(f'Order quantity = {foods[2]} x {inputs} - {discount} = {total}')
else:
    print("Please select menu :)")




