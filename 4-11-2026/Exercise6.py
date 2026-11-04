# Ejercicio 2: Doble y triple con lambda
""" Crea dos funciones lambda: una llamada doble que reciba un número y devuelva el
doble, y otra llamada triple que devuelva el triple.
Pide al usuario un número entero, aplica ambas funciones y muestra los dos resultados.
Ejemplo: si el usuario escribe 4, el programa debe mostrar: El doble es 8 y el triple es
12. """

double = lambda x: x * 2
triple = lambda x: x * 3

number = int(input("Escribe un número: "))
print("El doble es:", double(number))
print("El triple es:", triple(number))