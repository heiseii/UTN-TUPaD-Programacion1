#Actividad 2
productos = []
for i in range(5):
    producto = input("Ingrese el nombre del producto: ")
    productos.append(producto)
productos.sort()
print("Productos ordenados: ", productos)

opcion   = input("""Quiere eliminar o actualizar algun producto?
                          1. Eliminar
                          2. Actualizar
                          3. Ninguna
                          Ingrese el número de la opción: """)
#Eliminar producto
while opcion == "1":
    producto_eliminar = input("Ingrese el nombre del producto a eliminar: ")
    if producto_eliminar in productos:
        productos.remove(producto_eliminar)
        print("Producto eliminado. Productos restantes: ", productos)
    else:
        print("Producto no encontrado.")
    opcion = input("""Quiere eliminar o actualizar algun producto?
                          1. Eliminar
                          2. Actualizar
                          3. Ninguna
                          Ingrese el número de la opción: """)
#Actualizar producto    
while opcion == "2":
    producto_actualizar = input("Ingrese el nombre del producto a actualizar: ")
    if producto_actualizar in productos:
        nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
        index = productos.index(producto_actualizar)
        productos[index] = nuevo_nombre
        print("Producto actualizado. Productos actuales: ", productos)
    else:
        print("Producto no encontrado.")
    opcion = input("""Quiere eliminar o actualizar algun producto?
                          1. Eliminar
                          2. Actualizar
                          3. Ninguna
                          Ingrese el número de la opción: """)

print("Operación finalizada. Productos finales: ", productos)