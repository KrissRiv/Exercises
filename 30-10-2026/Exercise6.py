# Ejercicio 6
""" Lea el precio de un producto y la cantidad comprada. Calcule el total; si la cantidad es mayor
o igual a 5, aplique un 10% de descuento usando el operador *= . Muestre el total final con
formato de moneda. """

price = float(input("Ingrese el precio: "))
units = int(input("Ingrese la cantidad: "))

total = price * units
discount = total

if units >= 5:
    discount *= 0.10
    print(f"Su compra recibe un descuento automatico de ${discount:.0f}")

total -= discount
print(f"El total de su compra es: ${total:.0f}")