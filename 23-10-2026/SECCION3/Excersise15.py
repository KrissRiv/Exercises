#Ejercicio 15:
""" Lea un número entero N que representa los días laborados por un empleado
(valide con un ciclo while que N esté entre 1 y 15). Luego, pida las horas
trabajadas en cada uno de esos días. Al final muestre el total de horas acumuladas
y el valor a pagar sabiendo que la hora se remunera a $18.000. """

print("\n--- Calculadora de Pago de Empleado ---")
days = int(input("Ingrese el número de días laborados por el empleado (entre 1 y 15): "))
total_hours = 0

while days < 15 and days > 0:
    hours = int(input(f"Ingrese las horas trabajadas en el día {days}: "))
    total_hours = hours + total_hours
    days -= 1
print(f"Total de horas trabajadas: {total_hours}")
print(f"Total a pagar: ${total_hours * 18000:,.0f}")
    
