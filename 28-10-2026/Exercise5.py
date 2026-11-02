package = 10
weight_list = []
count_weight_max_20 = 0

while package > 0:
    weight = float(input("Ingresa el peso del paquete en Kg: "))
    if weight > 20:
        count_weight_max_20 += 1
    weight_list.append(weight)
    package -= 1

print(f"El peso maximo de los paquetes es: {max(weight_list)}")
print(f"El peso minimo de los paquetes es: {min(weight_list)}")
print(f"El promedio fue: {sum(weight_list) / len(weight_list)}")
print(f"Los paquetes que superaron los 20 kg fueron: {count_weight_max_20}")
