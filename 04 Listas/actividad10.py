#Actividad 10
ventas = [
    ["Cigarrillos", ["lunes", 10], ["martes", 15], ["miercoles", 20], ["jueves", 25], ["viernes", 30], ["sabado", 35], ["domingo", 40]],
    ["Galletitas", ["lunes", 5], ["martes", 10], ["miercoles", 15], ["jueves", 20], ["viernes", 25], ["sabado", 30], ["domingo", 35]],
    ["Refresco", ["lunes", 8], ["martes", 12], ["miercoles", 16], ["jueves", 20], ["viernes", 24], ["sabado", 28], ["domingo", 32]],
    ["Chocolates", ["lunes", 12], ["martes", 8], ["miercoles", 10], ["jueves", 17], ["viernes", 15], ["sabado", 28], ["domingo", 30]],
]
#total de venta de productos
print("Total vendido por cada producto: ")
for producto in ventas:
    total = sum(venta[1] for venta in producto[1:])
    print(f"{producto[0]}: {total}")
ventas_por_dia = [sum(ventas[i][j][1] for i in range(len(ventas))) for j in range(1, 8)]
#dia con mayores ventas
dia_mayores_ventas = ventas_por_dia.index(max(ventas_por_dia))
print(f"El dia con mayores ventas fue el dia {ventas[0][dia_mayores_ventas + 1][0]} con ventas totales de {ventas_por_dia[dia_mayores_ventas]}")
#productos con mas ventas
producto_mayores_ventas = max(ventas, key=lambda producto: sum(venta[1] for venta in producto[1:]))
print(f"El producto con mayores ventas totales fue: {producto_mayores_ventas[0]}")
