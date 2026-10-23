#Ejercicio 4:
""" Lea el precio base de un artículo y el porcentaje de descuento comercial
(por ejemplo, 15 para 15%). Calcule:
1. Monto del descuento.
2. Subtotal (precio base menos descuento).
3. IVA del 19% sobre el subtotal.
4. Total neto a pagar.
Muestre los cuatro valores en líneas separadas con formato de moneda (signo $,
separador de miles y sin decimales). """

base_price = float(input("Ingrese el precio base del articulo (ej. 10000): "))
discount_percentage = float(input("Ingrese el porcentaje de descuento (ej. 15): "))

discount_mount = base_price * (discount_percentage / 100)
subtotal = base_price - discount_mount
iva = subtotal * (0.19)
total = subtotal + iva

print("----------- PRECIO FINAL ----------- ")
print(f" - Precio: ${base_price:,.0f}")
print(f" - Descuento: ${discount_mount:,.0f}")
print(f" - Subtotal: ${subtotal:,.0f}")
print(f" - IVA: ${iva:,.0f}")
print("------------------------------------ ")
print(f" TOTAL: ${total:,.0f}")
print("------------------------------------ ")
