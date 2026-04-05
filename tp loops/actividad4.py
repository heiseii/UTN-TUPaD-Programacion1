suma = 0
num = int(input("Ingrese un numero (0 para terminar): "))
while num != 0:
    suma = suma + num
    num = int(input("Ingrese un numero (0 para terminar): "))
print("El total es:", suma)