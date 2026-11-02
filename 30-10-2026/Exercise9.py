# Ejercicio 9
""" Lea una frase y muestre sus iniciales: la primera letra de cada palabra en mayúscula
separadas por punto (por ejemplo, "logistica de carga" → "L.D.C."). """

sentence = input("Ingresa una oración: \n").strip()

split_sentence = sentence.split()
initials = ""

for word in split_sentence:
    initials += word[0].upper() + "."


print(initials)