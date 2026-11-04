# Ejercicio 3

""" Crea tres funciones lambda para convertir temperaturas: a_fahrenheit, a_kelvin y a_rankine. Luego crea una función convertir(grados, escala) que reciba la temperatura en Celsius y la letra de la escala destino ("F", "K" o "R") usando un diccionario de funciones. Si la escala no existe, la función debe devolver None. El programa principal imprime el resultado o un mensaje de error si la escala es inválida. """

to_fahrenheit = lambda c: c * 9/5 + 32
to_kelvin = lambda c: c + 273.15
to_rankine = lambda c: c * 9/5 + 491.67

def convert(celsius, scale):
    conversions = {
        "F": to_fahrenheit,
        "K": to_kelvin,
        "R": to_rankine
    }
    function = conversions.get(scale)

    if function is None:
        return None
    else:
        return function(celsius)

temp = float(input("Ingrese la temperatura en C: "))
scale = input("Ingrese la escala de destino (F, K o R): ").upper().strip()
result = convert(temp, scale)
if result is not None:
    print(f"Temperatura en {scale}: {result:.2f}")
else:
    print("Escala inválida")