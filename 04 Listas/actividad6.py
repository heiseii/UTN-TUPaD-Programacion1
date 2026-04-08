#Actividad 6
numeros = [1, 2, 3, 4, 5, 6, 7]
print("Lista original: ", numeros)
ultimo_numero = numeros[-1]
for i in range(len(numeros)-1, 0, -1):
    numeros[i] = numeros[i-1]
numeros[0] = ultimo_numero
print("Lista rotada: ", numeros)
