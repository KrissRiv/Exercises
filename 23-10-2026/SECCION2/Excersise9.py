#Ejercicio 9:
"""Calcule la tarifa de energía de una bodega según su consumo en kWh:
- Hasta 100 kWh: Tarifa básica de $45.000.
- Más de 100 y hasta 250 kWh: $45.000 más $650 por cada kWh que supere los 100.
- Más de 250 kWh: $142.500 más $900 por cada kWh que supere los 250.
Valide primero que el consumo no sea negativo; de serlo, muestre un mensaje de
error."""

print("\n-------------- CALCULO DE TARIFA DE ENERGIA DE BODEGA --------------")

kwh_consumed = float(input("Ingrese el consumo en kWh (Ej: 100): "))

if kwh_consumed < 0:
    print("El consumo no puede ser negativo.")
elif kwh_consumed <= 100:
    base_cost = 45000
elif kwh_consumed <= 250:
    excedent_kwh = kwh_consumed - 100
    base_cost = 45000 + (excedent_kwh * 650)
else:
    excedent_kwh = kwh_consumed - 250
    base_cost = 142500 + (excedent_kwh * 900)

if kwh_consumed >= 0:
    print(f"Para un consumo de {kwh_consumed} kWh, el costo a pagar es de ${base_cost:,.0f}")
print("--------------------------------------------------------")