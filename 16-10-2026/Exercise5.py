import datetime

age = int(input("Ingrese su edad: "))
actuall_year = datetime.datetime.now()
future_age = 2030 - actuall_year.year + age

print(f"Usted para el año 2030 tendra: {future_age}")
print(f"Será mayor de edad? {future_age >= 18}")