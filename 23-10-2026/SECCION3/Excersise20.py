#Ejercicio 20:
""" Lea un número entero N (valide que sea >= 3). Dibuje en consola un cuadrado hueco
de asteriscos de tamaño N x N usando ciclos anidados y condicionales (sin
multiplicar cadenas de texto).
Ejemplo para N = 4:
****
* *
* *
**** """

print("\n--- Dibujador de Cuadrados Huecos ---")
N = int(input("Ingrese el tamaño del cuadrado (N >= 3): "))

while N < 3:
    print("Error: El tamaño debe ser 3 o mayor.")
    N = int(input("Ingrese el tamaño del cuadrado (N >= 3): "))

for i in range(N):
    for j in range(N):
        if i == 0 or i == N - 1 or j == 0 or j == N - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print("\n--------- FIN DE CUADRO HUECO ----------")