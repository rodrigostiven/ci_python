# Faça você mesmo

# 5.3 Cores de alienígenas #1

alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    print("O jogador ganhou 5 pontos")
if 'blue' in alien_color:
    print("O jogador ganhou 5 pontos")

# 5.4 Cores de alienígenas #2

if 'green' in alien_color:
    print("O jogador ganhou 5 pontos")
else:
    print("O jogador ganhou 10 pontos")

if 'blue' in alien_color:
    print("O jogador ganhou 5 pontos")
else:
    print("O jogador ganhou 10 pontos")

# 5.5 Cores de alienígenas #3

alien_color = ['green']

if 'green' in alien_color:
    print("O jogador ganhou 5 pontos")
elif 'yellow' in alien_color:
    print("O jogador ganhou 10 pontos")
else:
    print("O jogador ganhou 15 pontos")

alien_color = ['yellow']

if 'green' in alien_color:
    print("O jogador ganhou 5 pontos")
elif 'yellow' in alien_color:
    print("O jogador ganhou 10 pontos")
else:
    print("O jogador ganhou 15 pontos")

alien_color = ['red']

if 'green' in alien_color:
    print("O jogador ganhou 5 pontos")
elif 'yellow' in alien_color:
    print("O jogador ganhou 10 pontos")
else:
    print("O jogador ganhou 15 pontos")

# 5.6 Fases da vida

age = 1

if age < 2:
    print("A pessoa é um neném")
elif age == 2 or age < 4:
    print("A pessoa é uma criança")
elif age == 4 or age < 13:
    print("A pessoa é um(a) garoto(a)")
elif age == 13 or age < 20:
    print("A pessoa é um adolescente")
elif age == 20 or age < 65:
    print("A pessoa é um adulto")
else:
    print("A pessoa é um(a) idoso(a)")

# 5.7 Fruta favorita

favorite_fruits = ['maçã', 'abacaxi', 'uva']

if 'maçã' in favorite_fruits:
    print(f"Você realmente gosta de {favorite_fruits[0]}")

if 'abacaxi' in favorite_fruits:
    print(f"Você realmente gosta de {favorite_fruits[1]}")

if 'uva' in favorite_fruits:
    print(f"Você realmente gosta de {favorite_fruits[2]}")

# 5.8 Olá, admin | 5.9 Sem usuários

# users = ['abel', 'ronaldo', 'admin', 'reinaldo']

users = []

if users:
    for user in users:
        if user == 'admin':
            print("Olá administrador, gostaria de ver um relatório de status?")
        else:
            print(f"Olá {user}, obrigado por fazer login novamente")
else:
    print("É necessário encontrar alguns usuários!")

# 5.10 Verificando nomes de usuários

current_users = ['renato', 'beatriz', 'regis', 'ronaldo', 'abel']
current_users_lower = [user.lower() for user in current_users]
new_users = ['Ronaldo', 'renato', 'rogerio', 'carlos']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"O nome {new_user} já foi usado, insira um novo nome")
    else:
        print(f"O nome {new_user} está disponível!")

# 5.11 Números ordinais

numbers = [number for number in range(1, 10)]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")