# Ejercicio 13
""" Lea la edad de un usuario y el tipo de entrada ("nino", "adulto", "mayor"). Calcule el precio:
niños (menores de 12) pagan 5000, mayores de 65 pagan 7000, el resto pagan 10000. Use la
edad con condicionales y verifique que el tipo de entrada sea válido. """

# Variable
age = int(input("Ingrese su edad: "))
input_type = input("Ingrese el tipo de entrada: ").strip().lower()
price = 0

if age < 12 and input_type == "nino":
    price = 5000
elif age < 65 and input_type == "adulto":
    price = 10000
elif age >= 65 and input_type == "mayor":
    price = 7000

print(f"El precio del {input_type} es: ${price}")