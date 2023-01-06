def get_formated_name(first_name, last_name):
    person = f"{first_name} {last_name}"
    return person.title()

while True:
    print('\nPlease tell me your name: ')
    print("(Enter 'q' at any time quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    mucisian = get_formated_name(f_name, l_name)
    print(f"\nHello, {mucisian}!")



