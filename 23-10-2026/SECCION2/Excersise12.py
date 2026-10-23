#Ejercicio 12:
""" Simule el menú interactivo de una cuenta bancaria con saldo inicial de $500.000
usando if-elif-else:
1. Consultar saldo
2. Consignar dinero
3. Retirar dinero
4. Salir
Lea la opción:
- Opción 1: Muestre el saldo actual.
- Opción 2: Lea el valor a consignar (debe ser mayor a 0) y muestre el nuevo saldo.
- Opción 3: Lea el valor a retirar; si es mayor a cero y no excede el saldo,
réstelo y muestre el nuevo saldo; de lo contrario muestre "Fondos insuficientes
o monto inválido".
- Opción 4: Muestre un mensaje de despedida.
- Otra opción: Muestre "Opción no válida". """

account_balance = 500000

print("\n-------------- MENU INTERACTIVO DE CUENTA BANCARIA --------------")
print("1. Consultar saldo")
print("2. Consignar dinero")
print("3. Retirar dinero")
print("4. Salir")
option = int(input("Ingrese la opción deseada: "))
print("--------------------------------------------------------")

if option == 1:
    print(f"Saldo actual: ${account_balance:,.0f}")
elif option == 2:
    deposit_amount = int(input("Ingrese el valor a consignar: "))
    if deposit_amount > 0:
        account_balance += deposit_amount
        print(f"Nuevo saldo: ${account_balance:,.0f}")
    else:
        print("Monto inválido")
elif option == 3:
    withdraw_amount = int(input("Ingrese el valor a retirar: "))
    if withdraw_amount > 0 and withdraw_amount <= account_balance:
        account_balance -= withdraw_amount
        print(f"Nuevo saldo: ${account_balance:,.0f}")
    else:
        print("Fondos insuficientes o monto inválido")
elif option == 4:
    print("Gracias por usar nuestros servicios")
else:
    print("Opción no válida")
print("--------------------------------------------------------")