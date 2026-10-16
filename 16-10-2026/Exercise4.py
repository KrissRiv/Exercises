cost_weight = float(input("Ingrese el costo por peso (ej. 5.000): "))
how_weight = float(input("Cuantos kilos quieres transportar: "))
subtotal_cost = cost_weight * how_weight
tax_iva = 0.19 * subtotal_cost
total_cost = subtotal_cost + tax_iva

print("------------- SUBTOTAL --------------")
print(f"El subtotal es: ${subtotal_cost:,.0f}")

print("------------- IVA (19%) --------------")
print(f"El IVA es: ${tax_iva:,.0f}")

print("------------- COSTO TOTAL --------------")
print(f"El costo total es: ${total_cost:,.0f}")
print("----------------------------------------")