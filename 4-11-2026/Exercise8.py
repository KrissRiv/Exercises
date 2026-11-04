# Ejercicio 4: Número aleatorio (random)
""" Crea una función lanzar_dado() que use la librería random para devolver un número
entero aleatorio entre 1 y 6, como un dado.
El programa principal lanza el dado dos veces, guarda los dos resultados en variables y
muestra ambos valores.
Ejemplo de salida: Primer lanzamiento: 4 - Segundo lanzamiento: 2. """

import random

def launch_dice():
    return random.randint(1, 6)

dado1 = launch_dice()
dado2 = launch_dice()
print("Primer lanzamiento:", dado1, "- Segundo lanzamiento:", dado2)