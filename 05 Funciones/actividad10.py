def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio de los números es: {promedio:.2f}")
