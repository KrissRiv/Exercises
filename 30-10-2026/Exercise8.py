# Ejercicio 8
""" Lea un nombre completo con formato "nombre apellido" (por ejemplo, "pedro gomez") y
genere un usuario: primera letra del nombre + apellido completo, todo en minúsculas (por
ejemplo, "pgomez"). Use indexing, lower() y concatenación. """

name = input("Ingrese el nombre completo: ")

name_format = name.strip().lower().split()
initial = name_format[0][0].split()

username = initial[0] + name_format[1]

print(username)

