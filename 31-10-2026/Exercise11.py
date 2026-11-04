# Ejercicio 11
""" Lea una hora del día en formato 24 horas (0 a 23) y muestre un saludo con elif: 6-11 "Buenos
días", 12-17 "Buenas tardes", 18-23 "Buenas noches" y 0-5 "Madrugada". Valide que la hora
esté en el rango. """

hour = int(input("Ingrese una hora (debe ser en ormato 24 Horas, de 0 a 23): "))

if hour < 0 or hour > 23:
    print("La hora no es valida")
elif hour >= 6 and hour <= 11:
    print("Buenos dias")
elif hour >= 12 and hour <= 17:
    print("Buenas tardes")
elif hour >= 18 and hour <= 23:
    print("Buenas noches")
elif hour >= 0 and hour <= 5:
    print("Madrugada")

