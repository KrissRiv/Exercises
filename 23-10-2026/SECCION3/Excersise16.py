#Ejercicio 16:
""" Lea el peso en kg de bultos ingresados a una bodega hasta que el usuario digite 0.
Si el usuario ingresa un número negativo, ignore el dato y muestre una advertencia.
Al terminar con 0, muestre:
- Cantidad total de bultos válidos ingresados.
- Peso total acumulado.
- Promedio de peso por bulto.
- Peso del bulto más liviano.
(Controle el caso en que se digite 0 desde el inicio sin registrar bultos). """

print("\n--- Calculadora de Peso de Bultos ---")
print("Ingrese 0 para salir.")
weight = 1
total_weight = 0
valid_count = 0
min_weight = 1

while weight != 0:
    weight = float(input("Ingrese el peso en kg del bulto: "))
    if weight < 0:
        print("Peso negativo, intente de nuevo.")
    elif weight == 0:
        break
    else:
        total_weight += weight
        valid_count += 1
        if weight < min_weight:
            min_weight = weight

print("\n--- Resultados ---")
print("Cantidad total de bultos válidos ingresados:", valid_count)
print("Peso total acumulado:", total_weight)
print("Promedio de peso por bulto:", total_weight / valid_count)
print("Peso del bulto más liviano:", min_weight)