# Um simples exemplo

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Verificando igualdade

car = 'bmw'
print(car == 'bmw')

# Ignorando letras maiúsculas e minúsculas ao verificar a igualdade

car = 'Audi'
print(car == 'audi')

car = 'Audi'
print(car.lower() == 'audi')