# Ejercicio 1: Saludo personalizado
""" Crea una función llamada saludar que reciba un parámetro nombre y devuelva (con
return) el texto "Hola, " seguido del nombre.
En el programa principal, pide al usuario que escriba su nombre con input(), llama a la
función y muestra el resultado con print().
Ejemplo de funcionamiento: si el usuario escribe Ana, el programa debe mostrar: Hola,
Ana. """

def greeting(name):
    return "Hola, " + name

name = input("Escribe tu nombre: ").strip()
print(greeting(name))