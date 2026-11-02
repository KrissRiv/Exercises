# Ejercicio 5
""" Lea un número entero de 4 dígitos y, usando solo // y %, extraiga y muestre cada dígito por
separado (unidades, decenas, centenas, miles). """

number = int(input("Digite un número: "))

print(f"Miles: {number // 1000}")
print(f"Centenas: {(number // 100) % 10}")
print(f"Decenas: {(number // 10) % 10}")
print(f"Unidades: {number % 10}")