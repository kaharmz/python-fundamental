
foods = ['Pecel lele', 'Nasi goreng', 'Gado-gado']

choice = input(f"Select menu : ")

inputs = int(input("Enter quantity: "))

if choice == foods[0]:
    if inputs < 6:
        price = 16000
        total = inputs * price
        print(f'{foods[0]} == {price}')
        print(f'Total amount = {foods[0]} x {inputs} = {total}')
    elif inputs > 6:
        price = 16000
        discount = 10000
        total = (inputs * price) - discount
        print(f'Total amount = {foods[0]} x {inputs} - {discount} = {total}')
elif choice == foods[1]:
    if inputs < 6:
        price = 14000
        total = inputs * price
        print(f'{foods[1]} == {price}')
        print(f'Total amount = {foods[1]} x {inputs} = {total}')
    elif inputs > 6:
        price = 14000
        discount = 5000
        total = inputs * price - discount
        print(f'{foods[1]} == {price}')
        print(f'Total amount = {foods[1]} x {inputs} - {discount} = {total}')
elif choice == foods[2]:
    if inputs < 6:
        price = 15000
        total = inputs * price
        print(f'{foods[2]} == {price}')
        print(f'Total amount = {foods[2]} x {inputs} = {total}')
    elif inputs > 6:
        price = 14000
        discount = 3000
        total = inputs * price - discount
        print(f'{foods[2]} == {price}')
        print(f'Total amount = {foods[2]} x {inputs} - {discount} = {total}')
else:
    print("Please select menu :)")




