#Ejercicio 7:
"""Lea los ingresos y los costos operativos de una empresa durante un mes. Calcule
la utilidad neta (ingresos menos costos) y determine el balance:
- Si es positivo, imprima "Ganancias" y el monto.
- Si es negativo, imprima "Pérdidas" y el monto.
- Si es igual a cero, imprima "Punto de equilibrio ($0)"."""

print("\n-------------- BALANCE DE LA EMPRESA --------------")
montly_income = int(input("Ingrese los ingresos mensuales de la empresa (Ej: 1000000): "))
monthly_expenses = int(input("Ingrese los gastos mensuales de la empresa (Ej: 500000): "))

montly_utility = montly_income - monthly_expenses

print("\n--- RESULTADO DEL BALANCE MENSUAL ---")
if montly_utility > 0:
    print(f"Ganancias de ${montly_utility:,.0f}")
elif montly_utility < 0:
    print(f"Pérdidas de ${montly_utility:,.0f}")
else:
    print("Punto de equilibrio ($0)")
print("----------------------------------------")