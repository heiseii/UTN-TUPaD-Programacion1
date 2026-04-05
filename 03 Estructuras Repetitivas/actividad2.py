#Ejercicio 2 - 'Acceso al campus y menu seguro'

usuario_correcto = "alumno"
clave_correcta = "python123"

for i in range(3):
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    while not (usuario == usuario_correcto and clave == clave_correcta):
        print("Usuario o clave incorrectos. Intente nuevamente. Intentos restantes:", 2 - i)
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
    while usuario == usuario_correcto and clave == clave_correcta:
        print("Bienvenido al campus")
        print("""
        1. Ver estado de inscripcion
        2. Cambiar clave
        3. Mostrar mesaje motivacional
        4. Salir
    """)
        
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 4:
            print("Opción inválida. Por favor, ingrese un número del 1 al 4.")
        elif opcion.isdigit() == False:
            print("Opción inválida. Por favor, ingrese un número del 1 al 4.")
        
        elif opcion == 1:
            print("Su estado de inscripción es: Inscripto")
            
        elif opcion == 2:           
            nueva_clave = input("Ingrese su nueva clave: ")
            while nueva_clave == clave_correcta:
                print("La nueva clave no puede ser igual a la anterior. Intente nuevamente.")
                nueva_clave = input("Ingrese su nueva clave: ")
            clave_correcta = nueva_clave
            print("Clave cambiada exitosamente.")
            
        elif opcion == 3:
            print("¡Sigue adelante, estás haciendo un gran trabajo!")
            
        elif opcion == 4:
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
      
    
    
    

        