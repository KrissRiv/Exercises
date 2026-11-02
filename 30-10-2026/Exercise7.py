# Ejercicio 7
""" Lea una frase y muestre: la cantidad de palabras (use split()), la palabra más larga y si la
frase contiene la palabra "urgente" (use in), con un mensaje diferente para cada caso. """

sentence = input("Ingrese un bloque de texto a ser evaluado: \n").lower().strip()

split_sentence = sentence.split(" ")

print(f"La palabra más grande es: {max(split_sentence)}")

if "urgente" in split_sentence:
    print("La palabra urgente esta incluida")
else:
    print("La palabra no esta incluida")
