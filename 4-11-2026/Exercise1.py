""" Crea una función calcular_tarifa(peso) que devuelva el costo de envío según el peso en kg: si pesa hasta 10 kg, cobra $15.000; si pesa entre 10 y 30 kg, cobra $28.000; si supera los 30 kg, cobra $28.000 más $900 por cada kg adicional. La función debe devolver el valor con return (sin print), y el programa principal muestra el resultado formateado. """

def calculate_cost(weight):
    if weight <= 10:
        return 15000
    elif weight <= 30:
        return 28000
    else:
        return 28000 + (weight - 30) * 900

weight = float(input("Ingrese el peso en kg: "))
cost = calculate_cost(weight)
print(f"El costo de la tarifa es: ${cost:,.0f}")
