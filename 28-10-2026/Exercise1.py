name = input("Ingrese su nombre: ")
name_without_space = name.replace(" ", "")

print(f"Nombre {name} en MAYÚSCULAS: {name.upper()}")
print(f"Nombre {name} en minúsculas: {name.lower()}")
print(f"Nombre sin espacios: {name_without_space}")
print(f"El nombre tiene {len(name_without_space)} caracteres")
print(f"La primer letra de {name_without_space} es {name_without_space[0]}")
print(f"La última letra de {name_without_space} es {name_without_space[-1]}")