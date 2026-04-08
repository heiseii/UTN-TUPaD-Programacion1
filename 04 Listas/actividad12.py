#Actividad 12
print("Ingrese 8 numeros enteros y se guardaran en una lista")
for i in range(8):
    numero = int(input(f"Ingrese el numero del {i+1}° puesto: "))
    if i == 0:
        numeros = [numero]
    else:
        numeros.append(numero)
print("Lista de numeros ingresados: ", numeros)
#lista de menor a mayor
for i in range(len(numeros)):
    numeros_ordenados = sorted(numeros)
print("Lista de numeros ordenados de menor a mayor: ", numeros_ordenados)
#lista de mayor a menor
for i in range(len(numeros)):
    numeros_ordenados_desc = sorted(numeros, reverse=True)
print("Lista de numeros ordenados de mayor a menor: ", numeros_ordenados_desc)