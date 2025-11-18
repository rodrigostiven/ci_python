# Alterando letras maiúsculas e minúsculas em uma string com métodos

name = "ada lovelace"

print(name.title())
print(name.upper())
print(name.lower())

# Usando variáveis em strings

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# Adicionando espaço em branco a strings com tabs ou quebras de linhas

print("Python")

print("\tPython")

print("Languages:\nPython\nC\nJavascript")

# Removendo espaços em branco com o strip()

favorite_language = 'python '

print(favorite_language)

favorite_language.rstrip()

print(favorite_language)


# Removendo prefixos

nostarch_url = 'https://nostarch.com'
print(nostarch_url)
nostarch_url.removeprefix('https://')
print(nostarch_url.removeprefix('https://'))


# Evitando erros de sintaxe com strings

message = "One of Python's strengths is its diverse community"
print(message)

#message = 'One of Python's strengths is its diverse community'
#print(message)

# Faça você mesmo

# 2.3

name = "Eric"

print(f"Olá, {name}, gostaria de aprender um pouco de Python hoje?")

# 2.4

print(name.title())
print(name.upper())
print(name.lower())

# 2.5

print('Albert Einstein disse uma vez: "Uma pessoa que nunca cometeu um erro nunca tentou nada de novo"')

# 2.6

famous_person = 'Albert Einstein'

message = 'disse uma vez: "Uma pessoa que nunca cometeu um erro nunca tentou nada de novo"'

print(f"{famous_person} {message}")

# 2.7

fruit_l = " maçã"
fruit_r = "maçã "
fruit = " maçã "

print(fruit_l.lstrip())
print(fruit_r.rstrip())
print(fruit.strip())
print(f"\t{fruit.strip()}")


# 2.8

# Arquivo
filename = "python_notes.txt"

print(filename.removesuffix('.txt'))


# Números

## Inteiros
print(2 ** 3)

## Floats

print(0.1 + 0.1)

print(0.1 * 0.2)

print(2 * 0.2)

print(0.2 + 0.1)

## Inteiros e floats

print(4 / 2)

print(1 + 2.0)

# Underscores em números

universe_age = 14_000_000_000

print(universe_age)

# Atribuição múltipla

x, y, z = 0, 0, 0

print(x, y, z)

# Constantes

MAX_CONNECTIONS = 5000

print(MAX_CONNECTIONS)


# Faça você mesmo

# 2.9

print(4 + 4)
print(10 - 2)
print(2 * 4)
print(16 / 2)

# 2.10

# Meu número favorito 
favorite_number = 33

print(f"Meu número favorito é {favorite_number}")



# Comentários

# Diga olá a todos
print("Hello Python people!")

