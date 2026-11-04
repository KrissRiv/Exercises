# Ejercicio 16
""" Implemente un juego de adivinanza: el número secreto es 37. De al usuario hasta 5 intentos
para acertar; en cada fallo muestre la pista "El número es mayor" o "El número es menor". Si
acierta muestre "Adivinado en N intentos"; si agota los 5, muestre "Se acabaron los intentos". """

secret_key = 37
attempts = 5

for attempt in range(attempts):
    guess = int(input("Adivina el número secreto: "))
    if guess == secret_key:
        print(f"Adivinado en {attempt + 1} intentos")
        break
    else:
        print("Número incorrecto.")
        if guess < secret_key:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        attempts -= 1
    if attempts == 0:
        print("Se acabaron los intentos")
    else:
        print("Intentos restantes:", attempts)