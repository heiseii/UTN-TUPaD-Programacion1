#Actividad 4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []
for numero in datos:
    if numero not in sin_repetidos:
        sin_repetidos.append(numero)
print("Lista original : ", datos)
print("Lista de datos sin repetir: ", sin_repetidos)