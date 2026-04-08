#Actividad 5
alumnos_presentes = ["Juan", "María", "Pedro", "Ana", "Luis", "Carlos", "Sofia", "Lucia"]
opcion = input("""¿Desea eliminar o Agregar algún alumno?
                  1. Eliminar
                  2. Agregar
                  3. Ninguna
                  Ingrese el número de la opción: """)
#Eliminar alumno
while opcion == "1":
    alumno_eliminar = input("Ingrese el nombre del alumno a eliminar: ")
    if alumno_eliminar in alumnos_presentes:
        alumnos_presentes.remove(alumno_eliminar)
        print("Alumno eliminado. Alumnos presentes restantes: ", alumnos_presentes)
    else:
        print("Alumno no encontrado.")
    opcion = input("""¿Desea eliminar o actualizar algún alumno?
                      1. Eliminar
                      2. Agregar
                      3. Ninguna
                      Ingrese el número de la opción: """)
#Agregar alumno
while opcion == "2":
    alumno_agregar = input("Ingrese el nombre del alumno a agregar: ")
    if alumno_agregar not in alumnos_presentes:
        alumnos_presentes.append(alumno_agregar)
        print("Alumno agregado. Alumnos presentes actuales: ", alumnos_presentes)
    else:
        print("Alumno ya presente.")
    opcion = input("""¿Desea eliminar o actualizar algún alumno?
                      1. Eliminar
                      2. Agregar
                      3. Ninguna
                      Ingrese el número de la opción: """)
print("Lista Actualizada: ", alumnos_presentes)