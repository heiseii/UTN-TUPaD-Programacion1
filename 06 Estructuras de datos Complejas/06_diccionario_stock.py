#Diccionario de stock de productos
#1- Se define el stock inicial
stock_productos = {'Tuercas': 50, 'Taladro': 30, 'Destornillador': 20, 'Martillos': 40}
#2- Menu inicial
while True:
    print("""Menu:
    1. Consultar stock de productos
    2. Agregar stock de un producto
    3. Agregar nuevo producto al stock
    4. Salir""")
    opcion = int(input("Ingrese una opcion: "))
    #1- Se muestra el stock actual de productos
    if opcion == 1:
        opcion_producto = input("Ingrese el nombre del producto a consultar: ").capitalize()
        if opcion_producto in stock_productos:
            print(f"Stock de {opcion_producto}: {stock_productos[opcion_producto]}")
        elif opcion_producto.isdigit():
            print("Por favor, ingrese un nombre de producto válido.")
        elif opcion_producto.strip() == "":
            print("El nombre del producto no puede estar vacío.")
        else:
            print(f"El producto {opcion_producto} no existe en el stock.")
    #2- Se le permite al usuario agregar stock a un producto existente o agregar un nuevo producto al stock
    elif opcion == 2:
        producto = input("Ingrese el nombre del producto: ").capitalize()
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        if producto in stock_productos:
            stock_productos[producto] += cantidad
        else:
            stock_productos[producto] = cantidad
        print(f"Stock actualizado de {producto}: {stock_productos[producto]}")
    #3- Se le permite al usuario agregar un nuevo producto al stock
    elif opcion == 3:
        producto = input("Ingrese el nombre del nuevo producto: ").capitalize()
        cantidad = int(input("Ingrese la cantidad inicial: "))
        stock_productos[producto] = cantidad
        print(f"Producto agregado: {producto}, Stock: {stock_productos[producto]}")
    #4- Se le permite al usuario salir del programa
    elif opcion == 4:
        print("Saliendo del programa.")
        break
    else:
        print("Opcion no valida. Por favor, ingrese una opcion del menu.")