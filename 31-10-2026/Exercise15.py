# Ejercicio 15
""" Pida números enteros hasta que el usuario ingrese uno negativo (el negativo no cuenta). Al
final muestre cuántos números pares ingresó y la suma de los impares."""

number = int(input("Ingrese un número (para salir ingrese un número negativo o 0): "))
count_even, sum_odd = 0, 0

while number > 0:
    if number % 2 == 0:
        count_even += 1
        print("El número es par")
    else:
        sum_odd += number
        print("El número es impar")
    number = int(input("Ingrese un número (para salir ingrese un número negativo o 0): "))

print(f"Cantidad de números pares: {count_even}")
print(f"Suma de los números impares: {sum_odd}")