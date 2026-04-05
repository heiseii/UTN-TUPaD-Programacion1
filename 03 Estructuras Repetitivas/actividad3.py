lunes = 4 #Turnos
martes = 3 #Turnos

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Introduzca el nombre de su operador: ")
while operador.isalpha() == False or operador == "":
    print("El nombre del operador no puede contener números, estar vacio o caracteres especiales. Intente nuevamente.")
    operador = input("Introduzca el nombre de su operador: ")

opcion = "0"
while opcion != "5":
    print("\nSeleccione una opcion \n1. Reservar turno \n2. Cancelar turno \n3. Ver agenda del dia \n4. Ver resumen general \n5. Cerrar Sistema")
    opcion = input("Ingrese el numero de la opcion que desea: ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5":
        print("Opcion no valida, intente nuevamente.")
        opcion = input("Ingrese el numero de la opcion que desea: ")

    if opcion == "1":
        dia = input("Ingrese el dia para reservar turno\n1= Lunes\n2= Martes: ")
        while dia != "1" and dia != "2":
            print("Dia no valido, intente nuevamente.")
            dia = input("Ingrese el dia para reservar turno\n1= Lunes\n2= Martes: ")

        if dia == "1":
            if lunes > 0:
                paciente = input("Ingrese el nombre del paciente: ")
                while paciente.isalpha() == False or paciente == "":
                    print("El nombre del paciente no puede contener números, estar vacio o caracteres especiales. Intente nuevamente.")
                    paciente = input("Ingrese el nombre del paciente: ")
                while paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4 or paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("El paciente ya tiene un turno reservado, intente nuevamente.")
                    paciente = input("Ingrese el nombre del paciente: ")
                    while paciente.isalpha() == False or paciente == "":
                        print("El nombre del paciente no puede contener números, estar vacio o caracteres especiales. Intente nuevamente.")
                        paciente = input("Ingrese el nombre del paciente: ")
                if lunes1 == "":
                    lunes1 = paciente
                elif lunes2 == "":
                    lunes2 = paciente
                elif lunes3 == "":
                    lunes3 = paciente
                elif lunes4 == "":
                    lunes4 = paciente
                lunes -= 1
                print("Turno reservado para el Lunes. Turnos restantes:", lunes)
            else:
                print("No hay turnos disponibles para el Lunes.")

        else:
            if martes > 0:
                paciente = input("Ingrese el nombre del paciente: ")
                while paciente.isalpha() == False or paciente == "":
                    print("El nombre del paciente no puede contener números, estar vacio o caracteres especiales. Intente nuevamente.")
                    paciente = input("Ingrese el nombre del paciente: ")
                while paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4 or paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("El paciente ya tiene un turno reservado, intente nuevamente.")
                    paciente = input("Ingrese el nombre del paciente: ")
                    while paciente.isalpha() == False or paciente == "":
                        print("El nombre del paciente no puede contener números, estar vacio o caracteres especiales. Intente nuevamente.")
                        paciente = input("Ingrese el nombre del paciente: ")
                if martes1 == "":
                    martes1 = paciente
                elif martes2 == "":
                    martes2 = paciente
                elif martes3 == "":
                    martes3 = paciente
                martes -= 1
                print("Turno reservado para el Martes. Turnos restantes:", martes)
            else:
                print("No hay turnos disponibles para el Martes.")
        
    elif opcion == "2":
        dia = input("Ingrese el dia para cancelar turno\n1= Lunes\n2= Martes: ")
        while dia != "1" and dia != "2":
            print("Dia no valido, intente nuevamente.")
            dia = input("Ingrese el dia para cancelar turno\n1= Lunes\n2= Martes: ")

        if dia == "1":
            paciente = input("Ingrese el nombre del paciente: ")
            while paciente.isalpha() == False or paciente == "":
                print("El nombre del paciente no puede contener números, estar vacio o caracteres especiales. Intente nuevamente.")
                paciente = input("Ingrese el nombre del paciente: ")
            if paciente == lunes1:
                lunes1 = ""
                lunes += 1
                print("Turno cancelado para el Lunes. Turnos disponibles:", lunes)
            elif paciente == lunes2:
                lunes2 = ""
                lunes += 1
                print("Turno cancelado para el Lunes. Turnos disponibles:", lunes)
            elif paciente == lunes3:
                lunes3 = ""
                lunes += 1
                print("Turno cancelado para el Lunes. Turnos disponibles:", lunes)
            elif paciente == lunes4:
                lunes4 = ""
                lunes += 1
                print("Turno cancelado para el Lunes. Turnos disponibles:", lunes)
            else:
                print("No se encontró un turno reservado para ese paciente en el Lunes.")
        
        else:
            paciente = input("Ingrese el nombre del paciente: ")
            while paciente.isalpha() == False or paciente == "":
                print("El nombre del paciente no puede contener números, estar vacio o caracteres especiales. Intente nuevamente.")
                paciente = input("Ingrese el nombre del paciente: ")
            if paciente == martes1:
                martes1 = ""
                martes += 1
                print("Turno cancelado para el Martes. Turnos disponibles:", martes)
            elif paciente == martes2:
                martes2 = ""
                martes += 1
                print("Turno cancelado para el Martes. Turnos disponibles:", martes)
            elif paciente == martes3:
                martes3 = ""
                martes += 1
                print("Turno cancelado para el Martes. Turnos disponibles:", martes)
            else:
                print("No se encontró un turno reservado para ese paciente en el Martes.")
        
    elif opcion == "3":
        print("\nAgenda del dia:")
        print("Lunes:")
        if lunes1 != "":
            print("- " + lunes1)
        if lunes2 != "":
            print("- " + lunes2)
        if lunes3 != "":
            print("- " + lunes3)
        if lunes4 != "":
            print("- " + lunes4)
        print("Martes:")
        if martes1 != "":
            print("- " + martes1)
        if martes2 != "":
            print("- " + martes2)
        if martes3 != "":
            print("- " + martes3)

    elif opcion == "4":
        print("\nResumen general:")
        print("Turnos ocupados el Lunes:", 4 - lunes)
        print("Turnos ocupados el Martes:", 3 - martes)
        print("Turnos disponibles el Lunes:", lunes)
        print("Turnos disponibles el Martes:", martes)
        print("Dias con mas turnos ocupados:")
        if 4 - lunes > 3 - martes:
            print("Lunes")
        elif 3 - martes > 4 - lunes:
            print("Martes")
        else:
            print("Empate")