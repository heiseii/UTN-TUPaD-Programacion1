#Actividad 3
import random
numeros = []
for i in range(15):
    numero = random.randint(1, 100)
    numeros.append(numero)
print("Números generados: ", numeros)

#Lista de pares
numeros_pares = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
print("Números pares: ", numeros_pares)
print("Tiene ", len(numeros_pares), "números pares.")
#Lista de impares
numeros_impares = []
for numero in numeros:
    if numero % 2 != 0:
        numeros_impares.append(numero)
print("Números impares: ", numeros_impares)
print("Tiene ", len(numeros_impares), "números impares.")