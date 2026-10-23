#Ejercicio 5:
""" Lea el ingreso mensual de una persona, sus gastos mensuales y su puntaje de
crédito (entero de 0 a 1000). Sin utilizar condicionales (if), calcule su ahorro
mensual (ingreso menos gastos) y muestre:
a) Proyección de ahorro en 1 año (12 meses).
b) El resultado booleano (True o False) que indique si califica para un crédito:
el ahorro mensual debe ser estrictamente mayor a $600.000 y el puntaje
crediticio debe ser mayor o igual a 720. """

montly_income = float(input("Ingrese su ingreso mensual (Ej: 1000000): "))
montly_expenses = float(input("Ingrese sus gastos mensuales (Ej: 500000): "))
montly_credit_score = int(input("Ingrese su puntaje de crédito (0-1000) (Ej: 720): "))

montly_savings = montly_income - montly_expenses
saving_year = montly_savings * 12

print(f"\n----------- SU AHORRO MENSUAL ES DE: ${montly_savings:,.0f} ----------- ")
print(f"En un año usted ahorra: ${saving_year:,.0f}")
print(f"Usted califica para un crédito: {montly_savings > 600000 and montly_credit_score >= 720}")
print("--------------------------------------------------------------------------")