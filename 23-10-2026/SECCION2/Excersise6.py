#Ejercicio 6:
""" Lea las ventas totales del día de la Sucursal Norte y de la Sucursal Sur.
Imprima cuál de las dos sucursales vendió más y la diferencia en dinero frente
a la otra. Si ambas vendieron lo mismo, muestre un mensaje de empate. """

north_sales = int(input("Ingrese las ventas totales del día de la sucursal Norte (Ej: 1000000): "))
south_sales = int(input("Ingrese las ventas totales del día de la sucursal Sur (Ej: 500000): "))

if north_sales > south_sales:
    difference = north_sales - south_sales
    print(f"La sucursal norte vendió más y la diferencia con la sucursal sur es de ${difference:,.0f}")
elif south_sales > north_sales:
    difference = south_sales - north_sales
    print(f"La sucursal sur vendió más y la diferencia con la sucursal norte es de ${difference:,.0f}")
else:
    print("Ambas sucursales vendieron lo mismo")