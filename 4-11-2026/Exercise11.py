# Ejercicio 7: Estadísticas de una lista de notas
""" Crea una función analizar_notas(notas) que reciba una lista de números y devuelva una
tupla con tres valores: la suma de las notas, la nota más alta y la nota más baja.
El programa principal define la lista [3.5, 4.2, 2.8, 5.0, 3.9], llama a la función,
desempaqueta la tupla y muestra los tres resultados.
Ejemplo de salida: Suma: 19.4 - Mayor: 5.0 - Menor: 2.8. """

def analyze_notes(notes):
    return sum(notes), max(notes), min(notes)

# notes = [3.5, 4.2, 2.8, 5.0, 3.9]
notes = [float(n.strip()) for n in input("Ingrese las notas separadas por coma: ").split(",")]
result = analyze_notes(notes)
print("Suma:", result[0], "- Mayor:", result[1], "- Menor:", result[2])