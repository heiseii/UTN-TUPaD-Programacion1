#Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana
#Actividad 7
temperaturas = [
    ["lunes", 15, 25],
    ["martes", 17, 27],
    ["miércoles", 14, 24],
    ["jueves", 16, 26],
    ["viernes", 18, 28],
    ["sábado", 19, 29],
    ["domingo", 20, 30]
]
print("Temperaturas mínimas y máximas de la semana: ")
for dia in range(len(temperaturas)):
    print(f"Día {temperaturas[dia][0]}: Mínima: {temperaturas[dia][1]}°C, Máxima: {temperaturas[dia][2]}°C")
#promedios
#min
suma_minimas = sum(temperaturas[i][1] for i in range(len(temperaturas)))
promedio_minimas = suma_minimas / len(temperaturas)
print(f"Promedio de temperaturas mínimas: {promedio_minimas}°C")
#max
suma_maximas = sum(temperaturas[i][2] for i in range(len(temperaturas)))
promedio_maximas = suma_maximas / len(temperaturas)
print(f"Promedio de temperaturas máximas: {promedio_maximas}°C")
#temperatura más alta registrada
max_temp = max(temperaturas[i][2] for i in range(len(temperaturas)))
print(f"Temperatura máxima registrada en la semana: {max_temp}°C en el dia {temperaturas[[i for i in range(len(temperaturas)) if temperaturas[i][2] == max_temp][0]][0]}")
