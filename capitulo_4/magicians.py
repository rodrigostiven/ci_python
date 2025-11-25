# Loops: percorrendo uma lista inteira

magicians = ['alice', 'david','carolina']
for magician in magicians:
    print(magician)


# Fazendo mais tarefas dentro de um loop for

for magician in magicians:
    print(f"{magician.title()}, that was a great trick")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Fazendo mais tarefas após usar um loop for

for magician in magicians:
    print(f"{magician.title()}, that was a great trick")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

# Faça você mesmo

# 4.1 Pizzas

pizzas = ["Quatro Queijos", "Bacon", "Frango"]

for pizza in pizzas:
    print(f"Sua pizza favorita é: {pizza}")
print("Eu gosto de pizza")

# 4.2 Animais

animals = ["Cachorro", "Gato", "Coelho"]

for animal in animals:
    print(f"Um {animal} seria um ótimo animal de estimação!")
print("Qualquer um desses animais daria um ótimo animal de estimação!")