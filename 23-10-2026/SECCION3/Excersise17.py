#Ejercicio 17:
""" Lea el valor total de una compra y el número de cuotas (valide con ciclo que las
cuotas estén entre 2 y 12). Muestre la tabla de amortización cuota por cuota con
el formato:
"Mes [i] | Cuota: $[valor] | Saldo restante: $[saldo]"
(Asegúrese de que el saldo final en la última cuota sea exactamente $0). """

total_buy = float(input("Ingrese el valor total de la compra: "))
num_pays = int(input("Ingrese el número de cuotas: "))

while num_pays < 2 or num_pays > 12:
    num_pays = int(input("Número de cuotas inválido. Ingrese un número entre 2 y 12: "))

value_per_pay = total_buy / num_pays
current_balance = total_buy

print("\nTabla de Amortización:")
for i in range(1, num_pays + 1):
    current_balance -= value_per_pay
    print(f"Mes {i} | Cuota: ${value_per_pay:.2f} | Saldo restante: ${current_balance:.2f}")