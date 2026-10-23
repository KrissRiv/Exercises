#Ejercicio 18:
""" Defina una clave numérica fija (por ejemplo, 73). Dé al usuario un máximo de
5 intentos para adivinarla. En cada fallo, indíquele si el número secreto es
mayor o menor y cuántos intentos le quedan. Si acierta, imprima
"¡Acceso autorizado en el intento X!"; si agota los 5 intentos sin éxito,
imprima "Sistema bloqueado. El código era 73". """

secret_key = 73
attempts = 5

for attempt in range(attempts):
    guess = int(input("Ingrese la clave: "))
    if guess == secret_key:
        print("¡Acceso autorizado en el intento", attempt + 1, "!")
        break
    else:
        print("Clave incorrecta.")
        if guess < secret_key:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")
        attempts -= 1
    if attempts == 0:
        print("Sistema bloqueado. El código era", secret_key)
    else:
        print("Intentos restantes:", attempts)