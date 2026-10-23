#Ejercicio 1:
""" Declare variables para registrar un producto en el inventario de una tienda de
tecnología: código de referencia (texto), unidades en stock (entero), precio
unitario en dólares (decimal) y si cuenta con garantía extendida (booleano).
Asigne valores de ejemplo, calcule en una variable adicional el valor total del
stock y muestre un resumen con el siguiente formato exacto:
"Ref: [código] | Stock: [unidades] uds | Unitario: $[precio] | Valor total: $[total] |
Garantía: [booleano]" """

reference = "TEST_REFERRNCE"
stock = 50
unit_price = 20.5
have_warranty = True

total_price_stock = stock * unit_price

print("-------------- INVENTARIO --------------")
print(f"Ref: {reference} | Stock: {stock} uds | Unitario: ${unit_price} | Valor total: ${total_price_stock:.2f} | Garantía: {have_warranty}")
print("----------------------------------------")