#Actividad 1
notas = [8.5, 7.0, 9.0, 6.5, 8.0, 7.5, 9.5, 8.0, 6.0, 7.0]
print("Notas de 10 estudiantes: ", notas)
#Promedio de notas
for i in range(len(notas)):
    promedio = sum(notas) / len(notas)
print("Promedio de notas: ", promedio)
#Nota más alta
for i in range(len(notas)):
    nota_mas_alta = max(notas)
print("Nota más alta: ", nota_mas_alta)
#Nota más baja
for i in range(len(notas)):
    nota_mas_baja = min(notas)
print("Nota más baja: ", nota_mas_baja)