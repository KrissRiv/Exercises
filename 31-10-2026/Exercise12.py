# Ejercicio 12
""" Lea un salario mensual y calcule el impuesto con esta tabla: menos de 2.000.000 paga 0%;
de 2.000.000 a 4.000.000 paga 10%; más de 4.000.000 paga 20%. Valide que el salario no sea
negativo. Muestre impuesto y salario neto con formato de moneda. """

salary = float(input("Ingrese el salario mensual: "))

if salary < 0:
    print("El salario no puede ser negativo")
elif salary < 2000000:
    taxes = 0
elif salary <= 4000000:
    taxes = salary * 0.10
else:
    taxes = salary * 0.20

if salary > 0:
    total = salary - taxes
    print(f"Impuesto: ${taxes}")
    print(f"Salario neto: ${total}")