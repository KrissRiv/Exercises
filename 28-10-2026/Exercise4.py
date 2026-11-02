code = input("Inserte el codigo del pedido: ").strip().upper()

if code.startswith("PED"):
    print(f"El prefijo del codigo {code} es {code[0:3]}")
    print(f"El año del pedido es: {code[4:8]}")
    print(f"El consecutivo es: {code[9::]}")
else:
    print(f"El codigo no tiene el prefijo requerido")

