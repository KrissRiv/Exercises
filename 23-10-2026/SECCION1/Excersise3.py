#Ejercicio 3:
""" Lea una cantidad entera positiva de segundos registrada en una fábrica.
Utilizando únicamente operadores aritméticos (// y %), calcule y muestre en
líneas separadas:
- Horas completas contenidas en ese tiempo.
- Minutos restantes.
- Segundos finales sobrantes.
En una cuarta línea, imprima el tiempo total expresado en horas exactas (con
decimales usando /). """

seconds = int(input("Ingrese una cantidad de segundos: "))

hours_completas = seconds // 3600
free_minutes = seconds % 3600
free_seconds = free_minutes % 60

total_hours = seconds / 3600

print(f"Horas completas: {hours_completas}")
print(f"Minutos restantes: {free_minutes}")
print(f"Segundos finales: {free_seconds}")
print(f"Horas totales: {total_hours}")