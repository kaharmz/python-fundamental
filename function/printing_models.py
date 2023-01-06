def print_models(unprinted_designs, completed_models):
    # Simulate printing each design, until non are left
    # Move each design to completed_models after printing

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)

# Display complete model
def show_completed_models(completed_models):
    print('\nThe following models have been printed: ')
    for completed_model in completed_models:
        print(completed_model)

# Start some designs that needs to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)




