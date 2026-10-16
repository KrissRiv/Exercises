weight = float(input("Ingrese el peso Kg: "))

if weight < 5:
    cost = 12000
elif weight <= 20:
    cost = 25000
else:
    cost = 25000 + (weight - 20) * 800

print(f"El costo total del envio es: ${cost:,.0f}")