weight = float(input("Ingrese el peso en KG: "))

if weight <= 0:
    print("El peso debe ser mayor a 0")
elif weight <= 5:
    cost = 12000
elif weight <= 20:
    cost = 25000
else:
    extra_weight = weight - 20
    cost = extra_weight * 500 + 25000

print(f"El costo total del envio es: ${cost:,.2f}")