# Ejercicio 1
""" Declare variables para un envío: ciudad destino (str), número de guía (int), valor declarado
en pesos (float) y es_fragil (bool) con valores de ejemplo. Imprima un resumen con una f-string
en el formato: "Envío 4521 a Cali — Valor: $125000.0 — Frágil: True". """

end_city = "Pereira"
guide_number = 4
value_declare = 320.34
is_fragile = True

print(f"Envío {guide_number} a {end_city} — Valor: ${value_declare} — Frágil: {is_fragile}")

# Ejercicio 2
""" Lea por teclado un número decimal como texto, conviértalo a float y luego obtenga su parte
entera con int(). Muestre el valor convertido y el tipo de cada variable usando type(). """

number = float(input("Ingresa un número: "))
number_int = int(number)

print(f"El número: {number:.2f}, su entero es: {number_int}, el tipo de cada variable es: {type(number)} y {type(number_int)}")

# Ejercicio 3
""" Lea dos números enteros A y B e intercambie sus valores usando una variable auxiliar.
Muestre ambos valores antes y después del intercambio. """

number_a = int(input("Ingrese un Número: "))
print(f"Al valor del primer número es: {number_a}")
number_b = int(input("Ingrese un Número: "))
print(f"Al valor del segundo número es: {number_b}")

number_changed = number_a
number_a = number_b
number_b = number_changed

print(f"Ahora el primer valor quedo: {number_a}")
print(f"Ahora el segundo valor quedo: {number_b}")