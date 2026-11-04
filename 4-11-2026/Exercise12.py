# Ejercicio 8: Contar vocales de una palabra
""" Crea una función contar_vocales(palabra) que reciba un texto y devuelva cuántas
vocales (a, e, i, o, u) contiene. No importa si son mayúsculas o minúsculas.
El programa principal pide una palabra al usuario, llama a la función y muestra: La
palabra tiene X vocales.
Ejemplo: con la palabra "Murcielago", el resultado es 5. """

def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

word = input("Ingrese una palabra: ").strip()
result = count_vowels(word.lower())
print("La palabra", word, "tiene", result, "vocales")