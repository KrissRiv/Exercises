years_experience = float(input("Ingrese los años de experiencia "))

if years_experience <= 1:
    print("Novato")
elif years_experience <= 3:
    print("Intermedio")
elif years_experience <= 10:
    print("Experto")
else:
    print("Master")


