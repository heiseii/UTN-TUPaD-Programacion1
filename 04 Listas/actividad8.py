#Actividad 8
notas = [
    ["Juan", ["Lengua", 8.0], ["Matemática", 7.0], ["Biología", 9.0]],
    ["María", ["Lengua", 6.5], ["Matemática", 8.0], ["Biología", 7.5]],
    ["Pedro", ["Lengua", 9.5], ["Matemática", 8.0], ["Biología", 6.0]],
    ["Ana", ["Lengua", 7.0], ["Matemática", 9.0], ["Biología", 8.5]],
    ["Luis", ["Lengua", 8.0], ["Matemática", 7.5], ["Biología", 9.5]]
]
#promedio de cada estudiante
for estudiante in notas:
    nombre = estudiante[0]
    promedio_estudiante = sum(estudiante[i][1] for i in range(1, 4)) / 3
    print(f"Promedio de {nombre}: {promedio_estudiante:.2f}")
#promedio de cada materia
for i in range(1, 4):
    promedio_materia = sum(notas[j][i][1] for j in range(len(notas))) / len(notas)
    print(f"Promedio total de {notas[0][i][0]}: {promedio_materia:.2f}")