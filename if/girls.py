girls = ['Maudy ayunda', 'Raisa adriana', 'Cut syifa', 'Cinta laura', 'Nazwa sihab', 'Luna maya']

new_girls = 'Agnes monica'

#Not in implementattion
if new_girls not in girls:
    print(f'{new_girls}, my favorite actress!')

for girl in girls:
    if girl != 'Cut syifa':
        print(girl.upper())
    else:
        print(girl.title())
