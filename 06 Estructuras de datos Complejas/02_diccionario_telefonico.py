#Programa de diccionario de telefonos
while True:
    #Nota
    #Me atrevi a integrar un menú para una interaccion mas fluida con el programa
    print("""Menu:
    1. Cargar contactos (Minimo 5)
    2. Buscar contacto
    3. Salir""")
    opcion = int(input("Ingrese una opcion: "))
        #1
        #Se le permite al usuario cargar 5 contactos con su nombre y numero de telefono
    if opcion == 1:
        agenda_telefonica = {}
        for i in range(5):
            nombre = input("Ingrese el nombre del contacto: ")
            numero = input("Ingrese el numero de telefono del contacto: ")
            agenda_telefonica[nombre] = numero
        #2
        #Se le permite ingresar un nombre y verifica si existe en la agenda
    if opcion == 2:
        nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
        if nombre_buscar in agenda_telefonica:
            print(f"El numero de telefono de {nombre_buscar} es: {agenda_telefonica[nombre_buscar]}")
        else:    print(f"El contacto {nombre_buscar} no existe en la agenda.")  
    if opcion == 3:
        print("Saliendo del programa.")
        break
    else:
        print("Opcion no valida. Por favor, ingrese una opcion del menu.")