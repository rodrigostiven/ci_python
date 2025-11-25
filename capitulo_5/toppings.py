# Verificando a diferença

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")

# Verificando elementos especiais

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")

# Verificando se uma lista não está vazia

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza!")

# Usando múltiplas listas

availabe_toppings = ['mushrooms', 'olives', 'green peppers',
                    'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in availabe_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")