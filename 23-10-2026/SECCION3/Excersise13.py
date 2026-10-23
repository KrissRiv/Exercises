#Ejercicio 13:
""" Lea un número entero positivo N. Usando un ciclo while, realice una cuenta
regresiva desde N hasta 0 imprimiendo cada número por línea. Si el número actual
es múltiplo de 5 (distinto de cero), añada al lado el texto "[Punto de control]".
Al finalizar el ciclo, imprima "¡Operación concluida!". """

number = int(input("Ingrese un número entero positivo: "))
while number > 0:
    if number % 5 == 0:
        print(f"{number} [Punto de control]")
    else:
        print(number)
    number -= 1
print("¡Operación concluida!")