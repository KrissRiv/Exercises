# Ejercicio 3: Área y circunferencia del círculo (math)
""" Usando la librería math, crea una función calcular_circulo(radio) que devuelva el área
del círculo. Recuerda que el área es pi por radio al cuadrado.
El programa principal pide el radio al usuario, llama a la función y muestra el área
redondeada a 2 decimales.
Ejemplo: con radio 3, el área es 28.27. """

import math

def circle_calculate(radio):
    return math.pi * radio ** 2

radio = float(input("Escribe el radio del círculo: "))
print("El área del círculo es:", round(circle_calculate(radio), 2))