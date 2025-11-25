# Copiando uma lista

my_food = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_food[:]

print("My favorite foods are:")
print(my_food)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

my_food.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_food)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

# Faça você mesmo

# 4.10 Fatias

print(f"Lista: {my_food}")
print(f"Os três primeiros elementos da lista são: {my_food[:3]}")
print(f"Os três elementos que ficam no meio da lista: {my_food[1:3]}")
print(f"Os três últimos elementos da lista são: {my_food[1:]}")

# 4.11 Minhas pizzas, suas pizzas

pizzas = ["Quatro Queijos", "Bacon", "Frango"]

friend_pizzas = pizzas[:]

pizzas.append('Calabresa')
friend_pizzas.append('Pepperoni')

print("Minhas pizzas favoritas são:")
for pizza in pizzas:
    print(pizza)

print("\nMinhas pizzas favoritas são:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

# 4.12 Mais loops

for food in my_food[:2]:
    print(food)