#Ejercicio 11:
""" Lea tres números diferentes por teclado. Sin usar las funciones max() ni min(),
utilice condicionales para determinar e imprimir cuál es el mayor, cuál el del
medio y cuál el menor. """

print("\n---------- CALCULO DE TRES NUMEROS DIFERENTES ----------")
number1 = int(input("Ingrese el primer número: "))
number2 = int(input("Ingrese el segundo número: "))
number3 = int(input("Ingrese el tercer número: "))

if number1 > number2 and number1 > number3:
    if number2 > number3:
        print("El mayor es", number1)
        print("El del medio es", number2)
        print("El menor es", number3)
    else:
        print("El mayor es", number1)
        print("El del medio es", number3)
        print("El menor es", number2)
elif number2 > number1 and number2 > number3:
    if number1 > number3:
        print("El mayor es", number2)
        print("El del medio es", number1)
        print("El menor es", number3)
    else:
        print("El mayor es", number2)
        print("El del medio es", number3)
        print("El menor es", number1)
else:
    if number1 > number2:
        print("El mayor es", number3)
        print("El del medio es", number1)
        print("El menor es", number2)
    else:
        print("El mayor es", number3)
        print("El del medio es", number2)
        print("El menor es", number1)

print("--------------------------------------------------------")