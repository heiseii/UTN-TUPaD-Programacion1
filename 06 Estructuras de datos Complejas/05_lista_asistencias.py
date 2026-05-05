#Lista de asistencias
asistencias = ["Ana", "Luis", "María", "Carlos", "Luis", "Jorge", "Lucía", "Ana", "Valentina", "Carlos"]
#1- Se imprime la lista de asistencias
print("Lista de asistencias:", asistencias)
#2- Conjunto de las personas que asistieron al menos una vez
asistentes_unicos = set(asistencias)
print("Personas que asistieron al menos una vez:", asistentes_unicos)
#3- Diccionario con la cantidad de veces que cada persona asistió
contador_asistencias = {}
for persona in asistencias:
    if persona in contador_asistencias:
        contador_asistencias[persona] += 1
    else:
        contador_asistencias[persona] = 1
print("Cantidad de veces que cada empleado asistió a la capacitacion:", contador_asistencias)