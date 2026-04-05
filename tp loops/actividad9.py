cantidad = 100
suma = 0
for i in range(cantidad):
    num = int(input("Ingrese un numero: "))
    suma = suma + num
media = suma / cantidad
print("La media es:", media)