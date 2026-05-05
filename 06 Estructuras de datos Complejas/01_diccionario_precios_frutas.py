#Diccionario de precios de frutas
#1- Se imprime el diccionario con las frutas y sus precios originales
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print("Precios originales:", precios_frutas)
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
#Se imprime el diccionario con las nuevas frutas y sus precios
print("Nuevas frutas y precios:", precios_frutas)
#2- Se actualizan los precios de las frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
#Se imprime el diccionario con los precios actualizados
print("Precios actualizados:", precios_frutas)
#3- Se crea una lista de las frutas sin los precios
lista_frutas = list(precios_frutas.keys())
#Se imprime la lista de frutas
print("Lista de frutas sin el precio:", lista_frutas)
