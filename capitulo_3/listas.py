# Listas

bicycles = ['trek', 'cannonble', 'redline', 'specialized']
print(bicycles)

# Acessando os elementos em uma lista

print(bicycles[0])
print(bicycles[0].title())

# Usando valores individuais de uma lista 

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)


# Faça você mesmo

# 3.1
names = ['luis', 'romario', 'diego']
print(names[0].title())
print(names[1].title())
print(names[2].title())

# 3.2

message = f"Olá, {names[0].title()}"
print(message)
message = f"Olá, {names[1].title()}"
print(message)
message = f"Olá, {names[2].title()}"
print(message)

# 3.3

veiculos = ['carro', 'moto']

message = f"Gostaria de um {veiculos[0]}"
print(message)
message = f"Gostaria de um {veiculos[1]}"
print(message)


# Modificando, adicionando e removendo elementos

# Modificando elementos em uma lista

motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)

motorcycle[0] = 'ducati'
print(motorcycle)

# Adicionando elementos de uma lista

# Anexando elementos ao final de uma lista

motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)

motorcycle.append('ducati')
print(motorcycle)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Inserindo elementos em uma lista

motorcycles.insert(0, 'ducati')

print(motorcycles)

# Removendo elementos de uma lista

# Removendo um elemento usando a instrução del

del motorcycles[0]

print(motorcycles)


# Removendo um elemento com o método pop()

motos = ['honda', 'yamaha', 'suzuki']
print(motos)

popped_motos = motos.pop()
print(f"Motos: {motos}")
print(f"Motos Pop: {popped_motos}")

print(f"The last motorcycle I owned was a {popped_motos.title()}")


# Removendo elementos de qualquer posição em uma lista

motorcycle_pop = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycle_pop.pop(0)
print(f"The first motorcycle I owned was a {first_owned}")


# Removendo um elemento por valor

motorcycle_remove = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycle_remove)

motorcycle_remove.remove('ducati')
print(motorcycle_remove)

too_expensive = 'suzuki'
motorcycle_remove.remove(too_expensive)
print(motorcycle_remove)
print(f"\nA {too_expensive.title()} is too expensive for me")

# Faça você mesmo


# 3.4 - Lista de Convidados

convidados = ['Jean', 'Mikasa', 'Eren']

print(f"Convite para {convidados[0]} ir o meu evento!")
print(f"Convite para {convidados[1]} ir o meu evento!")
print(f"Convite para {convidados[2]} ir o meu evento!")


# 3.5 Mudando a lista de convidados

print(f"O convidado {convidados[2]} não poderá ir a festa")

convidados[2] = "Levi"

print(f"Convite para {convidados[2]} ir o meu evento!")


# 3.6

print("Temos uma mesa maior")

convidados.insert(0, 'Luffy')
convidados.insert(2, 'Nami')
convidados.append('Naruto')


print(f"Convite para {convidados[0]} ir o meu evento!")
print(f"Convite para {convidados[2]} ir o meu evento!")
print(f"Convite para {convidados[5]} ir o meu evento!")

print("Só temos duas vagas disponíveis!")

print(f"{convidados[5]} Lamentamos pelo cancelamento")
convidados.pop()

print(f"{convidados[4]} Lamentamos pelo cancelamento")
convidados.pop()

print(f"{convidados[3]} Lamentamos pelo cancelamento")
convidados.pop()

print(f"{convidados[2]} Lamentamos pelo cancelamento")
convidados.pop()


print(f"{convidados[1]} Você está confirmado")
print(f"{convidados[0]} Você está confirmado")


del convidados[1]
del convidados[0]

print(f"Lista: {convidados}")


# Organizando uma lista

# Ordenando uma lista permanentemente com o método sort()

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# Ordenando uma lista temporariamente com a função sorted()

cars_sorted = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is a the original list:")
print(cars_sorted)

print("\nHere is the sorted list:")
print(sorted(cars_sorted))

print("\nHere  is the original list again")
print(cars_sorted)

# Exibindo uma lista em ordem inversa


cars_reverse = ['bmw', 'audi', 'toyota', 'subaru']
print(cars_reverse)

cars_reverse.reverse()
print(cars_reverse)

cars_reverse.reverse()
print(cars_reverse)

# Identificando o tamanho de uma lista

cars_len = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))


# Faça você mesmo

# 3.8 Conhecendo o mundo

favorite_places = ['Casa', 'Alter do Chão', 'Cinema', 'Shopping', 'Estádio']

print(favorite_places)

print(sorted(favorite_places))

print(favorite_places)

print(sorted(favorite_places, reverse=True))

print(favorite_places)

favorite_places.reverse()

print(f"Reverse: {favorite_places}")

favorite_places.reverse()

print(f"Reverse_two: {favorite_places}")

favorite_places.sort()

print(f"Sort: {favorite_places}")

favorite_places.sort(reverse=True)

print(f"Sort_two: {favorite_places}")


# 3.9 Convidados para o jantar

convidados.insert(0, 'Luffy')
convidados.insert(2, 'Nami')
convidados.append('Naruto')

print(f"Número convidados: {len(convidados)}")


# 3.10

names = []

names.append('Ryan')
names.append('Bruce')
names.insert(2, 'John')
names.append('Nami')
names.append('Naruto')
names.append('Luffy')
names.append('Alexandre')
names.append('Amélia')


print(names)

names.pop()

print(names)

del names[2]

print(names)

names.remove('Ryan')

print(names)

print(names[-1])

name_pop = names.pop(0)

print(names)

names.sort()

print(names)

names.sort(reverse=True)

print(names)

names.reverse()

print(names)

print(len(names))