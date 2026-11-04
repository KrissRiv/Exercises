# Ejercicio 6: Fecha de hoy (datetime)
""" Crea una función mostrar_fecha() que use la librería datetime para obtener la fecha
actual y devolverla como texto en el formato dd/mm/aaaa.
El programa principal llama a la función y muestra: Hoy es: seguido de la fecha
devuelta.
Pista: usa date.today() y strftime con el formato "%d/%m/%Y". """

import datetime

def show_date():
    return datetime.date.today().strftime("%d/%m/%Y")

print("Hoy es: ", show_date())