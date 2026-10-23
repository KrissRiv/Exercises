number1 = int(input("Ingrese un numero: "))
number2 = int(input("Ingrese otro numero: "))

if number1 > number2:
    print(f"El numero 1: {number1} es mayor que el numero 2: {number2}")
elif number2 > number1:
    print(f"El numero 2: {number2} es mayor que el numero 1: {number1}")
elif number1 == number2:
    print("Los numeros son iguales")
