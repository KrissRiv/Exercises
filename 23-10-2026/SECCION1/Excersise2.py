#Ejercicio 2:
""" Lea por teclado el nombre de una ruta logística, la distancia recorrida en
kilómetros (decimal) y la cantidad de galones de combustible consumidos (decimal).
Calcule el rendimiento del vehículo (km por galón) y muestre el mensaje:
"En la ruta [nombre] el vehículo tuvo un rendimiento de [rendimiento] km/galón"
(el rendimiento debe redondearse a 2 cifras decimales). """

route_name = input("Ingrese el nombre de la ruta: ")
distance = float(input("Ingrese la distancia recorrida (Km): "))
galons = float(input("Ingrese la cantidad de galones consumidos: "))

performance = distance / galons

print(f"En la ruta {route_name} el vehículo tuvo un rendimiento de {performance:,.2f} km/galón")