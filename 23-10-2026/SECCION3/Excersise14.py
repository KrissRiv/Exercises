#Ejercicio 14:
""" Genere una tabla de equivalencia térmica desde 10 °C hasta 100 °C de 5 en 5,
empleando un ciclo for y range().
Fórmula: F = C * 9/5 + 32. Formato: "[C] °C equivalen a [F] °F". """

for degrees in range(10, 101, 5):
    farenheit = degrees * 9 / 5 + 32
    print(f"{degrees} °C equivalen a {farenheit} °F")