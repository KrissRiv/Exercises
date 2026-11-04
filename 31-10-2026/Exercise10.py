# Ejercicio 10
""" Lea un año entero y determine si es bisiesto: es bisiesto si es divisible por 4, excepto si es
divisible por 100, a menos que también sea divisible por 400. Muestre "Bisiesto" o "No bisiesto". """

year = int(input("Ingrese un año: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("El Año es bisiesto")
else:
    print("El Año no es bisiesto")
