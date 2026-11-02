plate = input("Ingrese la placa de su vehiculo: ").strip().upper()
last_digit = plate[-1]

if last_digit in "0,2,4,6,8":
    print(f"El vehículo de placa {plate}, puede circular hoy")
elif last_digit in "1,3,5,7,9":
    print(f"El vehículo de placa {plate}, no puede circular hoy")
else:
    print(f"El vehículo con placa {plate}, no usa número al final")
