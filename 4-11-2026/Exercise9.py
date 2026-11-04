# Ejercicio 5: Raíz cuadrada y potencia (math)
""" Crea una función operaciones(numero) que reciba un número y devuelva una tupla con
dos valores: la raíz cuadrada del número (usa math.sqrt) y el número elevado al cuadrado
(usa math.pow o el operador **).
El programa principal pide un número positivo, desempaqueta la tupla que devuelve la
función y muestra ambos resultados redondeados a 2 decimales.
Ejemplo: con el número 9, debe mostrar la raíz cuadrada 3.0 y el cuadrado 81.0. """

import math

def operations(number):
    return math.sqrt(number), math.pow(number, 2)

number = float(input("Escribe un número positivo: "))
result = operations(number)
print("Raíz cuadrada:", round(result[0], 2), "- Cuadrado:", round(result[1], 2))