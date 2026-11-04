# Ejercicio 4

""" Simula un juego donde el usuario "apuesta" a un número del 1 al 6 y se lanzan dos dados. Crea una función lanzar_dados() que devuelva una tupla con los dos valores, usando random.randint. Dentro de la función guarda cuántos lanzamientos se han hecho en una variable local lanzamientos; fuera de la función declara una variable global con el mismo nombre e intenta imprimirla después de jugar. Comenta la línea problemática y explica por qué da NameError o qué valor muestra. """

import random

count_launches = 0

def launch_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return (dice1, dice2)

print("------------------ LANZAMIENTO DE DADOS ------------------")
continue_gaming = input("¿Quieres jugar? (s/n): ").strip().lower()
    
while continue_gaming == "s":
    number_bet = int(input("¿A qué número apuestas? (1-6): ").strip())
    dice1, dice2 = launch_dice()
    count_launches += 1
    print("Ha salido: ", dice1, "y", dice2)
    if dice1 == number_bet or dice2 == number_bet:
        print("¡Has acertado!")
    else:
        print("Has fallado")
    print("Total de lanzamientos: ", count_launches)
    continue_gaming = input("¿Quieres seguir jugando? (s/n): ").strip().lower()
    if continue_gaming != "s":
        break
    number_bet = int(input("¿A qué número apuestas? (1-6): ").strip())

print("---------------------- END GAME ----------------------")