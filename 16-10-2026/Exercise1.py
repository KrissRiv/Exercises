name = input("Cual es tu nombre: ")
packages = int(input("Cuantos paquetes quieres enviar: "))
total_weight = float(input("Cual es el peso total (Exprese su respuesta en KG): "))
is_assurance = bool(input("Deseas seguro? (S/N): "))

print("------------- ENVIOS ------------")
print(f"Cliente: {name} - Paquetes: {packages} - Peso: {total_weight} kg - Seguro: {is_assurance}")
print("--------------------------------")