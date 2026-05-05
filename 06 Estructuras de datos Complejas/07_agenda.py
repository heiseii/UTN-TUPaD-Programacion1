#Agenda con con tuplas
agenda = {
    "Clases de bateria": ("Lunes", "20:00hs"),
    "Clases de Ingles": ("Martes", "19:00hs"),
    "Torneo de futbol": ("Miercoles", "18:00hs"),
    "Reunion con amigos": ("Jueves", "21:00hs"),
    "Cita con mi novia": ("Viernes", "17:00hs")
}
#1- Se permite consultar la actividad por el dia o la hora
while True:
    consulta = input("Ingrese el dia o la hora para consultar la actividad (o 'salir' para terminar): ")
    if consulta.lower() == "salir":
        print("Saliendo del programa.")
        break
    encontrado = False
    for actividad, (dia, hora) in agenda.items():
        if consulta.lower() == dia.lower() or consulta.lower() == hora.lower():
            print(f"Actividad: {actividad}, Dia: {dia}, Hora: {hora}")
            encontrado = True
    if not encontrado:
        print("No se encontraron actividades para esa consulta.")
    
