#Diccionario de frases
#1- Se le solicita al usuario una frase e imprime:
frase = input("Ingrese una frase: ")
#las palabras unicas usando un set
palabras_unicas = set(frase.split())
print("Palabras únicas:", palabras_unicas)
#un diccionario con la cantidad de veces que se repite cada palabra
contador_palabras = {}
for palabra in frase.split():
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print("Recuento de palabras:", contador_palabras)
