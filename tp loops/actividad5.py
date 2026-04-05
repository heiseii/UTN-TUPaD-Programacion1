import random
numero = random.randint(0, 9)
intentos = 0
adivina = -1
while adivina != numero:
    adivina = int(input("Adivine el numero entre 0 y 9: "))
    intentos = intentos + 1
print("Correcto. Intentos:", intentos)