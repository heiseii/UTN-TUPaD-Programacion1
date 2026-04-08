#Actividad 11
estudiantes = ["Juan", "María", "Pedro", "Ana", "Luis", "Sofía", "Carlos", "Lucía", "Diego", "Valentina"]
#busqueda de estudiantes
busqueda = input("Ingrese el nombre del estudiante a buscar: ")
while busqueda.lower() in estudiantes or busqueda.capitalize() in estudiantes or busqueda.upper() in estudiantes:
    print(f"El/la alumno/a {busqueda.capitalize()} está en la lista y aparece en la posicion {estudiantes.index(busqueda.capitalize()) + 1}.")
    busqueda = input("Ingrese el nombre del estudiante a buscar: ")
#opcion de salida
else:
    print(f"{busqueda} no está presente en la lista de estudiantes. Intente nuevamente o escriba salir para finalziar la busqueda.")
    busqueda = input()
    while busqueda.lower() != "salir" and busqueda != "SALIR" and busqueda != "Salir":
        if busqueda.lower() in estudiantes or busqueda.capitalize() in estudiantes or busqueda.upper() in estudiantes:
            print(f"El/la alumno/a {busqueda.capitalize()} está en la lista y aparece en la posicion {estudiantes.index(busqueda.capitalize()) + 1}.")
            busqueda = input("Ingrese el nombre del estudiante a buscar: ")
        else:
            print(f"{busqueda} no está presente en la lista de estudiantes. Intente nuevamente o escriba salir para finalizar la búsqueda.")
        busqueda = input()
        if busqueda.lower() == "salir" or busqueda == "SALIR" or busqueda == "Salir":
            break
print("Búsqueda finalizada.")
        