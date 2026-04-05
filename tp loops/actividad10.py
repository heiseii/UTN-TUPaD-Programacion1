num = input("Ingrese un numero: ")
invertido = ""
for i in range(len(num) - 1, -1, -1):
    invertido = invertido + num[i]
print("Numero invertido:", invertido)