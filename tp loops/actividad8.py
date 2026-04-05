cantidad = 100
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(cantidad):
    num = int(input("Ingrese un numero: "))    
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1    
    if num > 0:
        positivos = positivos + 1
    elif num < 0:
        negativos = negativos + 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)