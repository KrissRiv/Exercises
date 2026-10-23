#Ejercicio 19:
""" Lea dos números enteros positivos A y B (valide que ambos sean mayores a 0 y que
B sea mayor que A). Recorra el rango de números entre A y B (inclusive) y cuente:
1. Cuántos son múltiplos de 4 y de 6 a la vez.
2. Cuántos son impares mayores a 50.
3. La suma de los números que terminen en 7 (evaluando num % 10 == 7). """

number_a = int(input("Ingrese primer numero: "))
number_b = int(input("Ingrese segundo numero: "))

count_mult_4_6 = 0
count_odd_50 = 0
sum_ends_7 = 0

if number_a > 0 and number_b > 0 and number_b > number_a:
    while number_a <= number_b:
        if number_a % 4 == 0 and number_a % 6 == 0:
            count_mult_4_6 += 1
        if number_a % 2 != 0 and number_a > 50:
            count_odd_50 += 1
        if number_a % 10 == 7:
            sum_ends_7 += number_a
        number_a += 1
    print("Cantidad de multiplos de 4 y 6 a la vez: ", count_mult_4_6)
    print("Cantidad de impares mayores a 50: ", count_odd_50)
    print("Suma de los numeros que terminan en 7: ", sum_ends_7)
    