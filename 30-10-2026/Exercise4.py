# Ejercicio 4
""" Lea dos enteros positivos y muestre: el cociente entero (//), el residuo (%) y un mensaje que
indique si el primero es divisible por el segundo. Controle la división entre cero. """

number_a = int(input("Ingrese un número: "))
number_b = int(input("Ingrese un número: "))

if number_a == 0 or number_b == 0:
    print("Ingrese velores superiores a 0")
else:
    result_a = number_a // number_b
    result_b = number_a % number_b

    print(f"El cociente de ambos valores es: {result_a}")
    print(f"El residuo de ambos valores es: {result_b}")
    
    if result_b == 0:
        print(f"El numero {number_a}, es divisible por {number_b}")
    else:
        print(f"El numero {number_a}, no es divisible por {number_b}")