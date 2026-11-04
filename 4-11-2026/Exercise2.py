# EJERCICIO 2

""" Un docente necesita analizar las notas de un grupo. Crea una función analizar_notas(notas) que reciba una lista de notas (0 a 5) y devuelva una tupla con el promedio, la nota más alta y la desviación estándar, usando la librería statistics. El programa principal debe pedir las notas separadas por comas, llamar a la función e imprimir el informe redondeado a 2 decimales. """

import statistics

def goals_analyst(goals):
    average = statistics.mean(goals)
    highest = max(goals)
    std_dev = statistics.stdev(goals)
    return average, highest, std_dev
    
notes = [float(x.strip()) for x in input("Ingrese las notas separadas por comas: ").split(",")]

average, highest, std_dev = goals_analyst(notes)
print(f"Promedio: {average:.2f}")
print(f"Nota más alta: {highest:.2f}")
print(f"Desviación estándar: {std_dev:.2f}")