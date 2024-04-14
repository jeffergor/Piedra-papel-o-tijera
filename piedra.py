import random

options = ('piedra', 'papel', 'tijera')

rounds = 1
computer_wins = 0
user_wins = 0

print(""" !!!🤖 Bienvenid@ al Juego, estás a punto de realizar un reto que solo los genios podrán ganar 🧠!!! """)
nombre = input("Por favor, ingresa tu nombre para comenzar el juego: ")
respuesta = input(""" WARNING!!!: ¿Te enfrentarás a tu propia computadora, estás seguro de continuar? (si/no)""")

if respuesta.lower() == "si":
    print("¡Genial! Comencemos con el juego.")

elif respuesta.lower() == "no":
    print("Gracias por participar, vuelve cuando quieras. 😎 ")
    exit()

else:
    print("Respuesta no válida, vuelve a intentarlo y responde solo 'si' o 'no'")
    exit()

while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)

    user_option = input('Piedra ⛰️, papel 📄 o tijera ✂️ =>').lower()

    rounds += 1

    if user_option not in options:
        print('Esa opción no es válida')
        continue

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    if user_option == computer_option:
        print('Empate!')

    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('¡Usuario gana!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('¡Computadora gana!')
            computer_wins += 1

    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('¡Usuario gana!')
            user_wins += 1
        else:
            print('Tijera gana a papel')
            print('¡Computadora gana!')
            computer_wins += 1

    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('¡Usuario gana!')
            user_wins += 1
        else:
            print('Piedra gana a tijera')
            print('¡Computadora gana!')
            computer_wins += 1

    if computer_wins == 5:
        print('El ganador es la computadora')
        break

    if user_wins == 5:
        print(f'¡El ganador es {nombre}!')
        print('🏆 ¡Felicidades! Eres un genio 🏆')
        break
