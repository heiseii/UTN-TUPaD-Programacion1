def calcular_area_circulo(radio):
    pi = 3.14159
    area = pi * (radio ** 2)
    return area
def calcular_perimetro_circulo(radio):
    pi = 3.14159
    perimetro = 2 * pi * radio
    return perimetro
radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es: {area:.1f}")
print(f"El perímetro del círculo es: {perimetro:.1f}")