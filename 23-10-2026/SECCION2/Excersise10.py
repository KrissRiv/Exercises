#Ejercicio 10:
""" Clasifique el rendimiento de un operario según su calificación (de 0.0 a 5.0):
- Menor a 3.0: "Bajo rendimiento"
- De 3.0 a 3.7: "Desempeño Aceptable"
- Más de 3.7 a 4.4: "Desempeño Destacado"
- Más de 4.4 a 5.0: "Desempeño Sobresaliente - Bonificación"
Valide que la nota esté dentro del rango permitido (0.0 a 5.0); en caso contrario,
muestre "Calificación fuera de rango". """

print("\n--------- CALIFICACION DE RENDIMIENTO DE OPERARIO ----------")
rating = float(input("Ingrese la calificación del operario entre 0.0 y 5.0 (Ej: 4.5): "))

if rating < 0 or rating > 5:
    print("Calificación fuera de rango")
else:
    if rating < 3.0:
        print("Bajo rendimiento")
    elif rating <= 3.7:
        print("Desempeño Aceptable")
    elif rating <= 4.4:
        print("Desempeño Destacado")
    else:
        print("Desempeño Sobresaliente - Bonificación")

print("--------------------------------------------------------")
