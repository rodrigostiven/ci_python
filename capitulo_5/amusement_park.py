# Sequência if-elif-else

age = 4
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# Outra forma mais sucinta

age = 4
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

# Usando múltiplos blocos elif

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

# Omitindo o bloco else

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 20

print(f"Your admission cost is ${price}.")