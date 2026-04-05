# Ejercicio 1 - Caja del kiosko

nombre = input('Ingrese su nombre: ')
while nombre.isalpha() == False:
    nombre = input('El nombre no puede contener números. Vuelva a ingresarlo: ')

cantidad = input('Ingrese la cantidad de productos: ')
while cantidad.isdigit() == False:
    cantidad = input('Debe ser un número entero positivo. Vuelva a ingresarlo: ')
cantidad = int(cantidad)
while cantidad <= 0:
    cantidad = input('Debe ser mayor a 0. Vuelva a ingresarlo: ')
    cantidad = int(cantidad)

total_c_desc = 0
total_s_desc = 0

print('Cliente: ' + nombre)
print('Cantidad de productos: ' + str(cantidad))

for i in range(cantidad):
    nombre_producto = input('Ingrese el nombre del producto: ')
    while nombre_producto.isalpha() == False:
        nombre_producto = input('El nombre del producto no puede contener números. Vuelva a ingresarlo: ')

    precio = input('Ingrese el precio del producto: ')
    while precio.isdigit() == False:
        precio = input('El precio debe ser un número entero. Vuelva a ingresarlo: ')
    precio = int(precio)

    descuento = input('¿Tiene descuento? S/s o N/n: ')
    while descuento != 'S' and descuento != 's' and descuento != 'N' and descuento != 'n':
        descuento = input('Ingrese S/s o N/n: ')

    print('Producto ' + str(i + 1) + ' - Precio: ' + str(precio) + ' Descuento (S/N): ' + descuento)

    total_s_desc = total_s_desc + precio

    if descuento == 'S' or descuento == 's':
        precio = precio * 0.9

    total_c_desc = total_c_desc + precio

ahorro = total_s_desc - total_c_desc
promedio = total_c_desc / cantidad
print(f'Total con descuento: {total_c_desc}')
print(f'Total sin descuento: {total_s_desc}')
print(f'Total ahorrado: {ahorro}')
print(f'Precio promedio: {promedio}')