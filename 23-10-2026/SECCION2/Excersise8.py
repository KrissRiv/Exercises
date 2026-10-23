#Ejercicio 8:
""" Lea el número de lote de producción de una mercancía (entero positivo).
Indique si el lote es par o impar. Adicionalmente, verifique e informe si el lote
debe ser sometido a "Auditoría Especial", condición que ocurre únicamente si
el número es múltiplo de 3 pero NO es múltiplo de 5."""

print("\n--------- VERIFICACION DE LOTES PRODUCTION --------------")
lote = int(input("Ingrese el número de lote de producción (Ej: 1000000): "))

result = lote % 2

if result == 0:
    print("El lote es par.")
else:
    print("El lote es impar.")

is_audit = lote % 3 == 0 and lote % 5 != 0

if is_audit:
    print("El lote debe ser sometido a Auditoría Especial")
else:
    print("El lote NO debe ser sometido a Auditoría Especial")

print("--------------------------------------------------------")