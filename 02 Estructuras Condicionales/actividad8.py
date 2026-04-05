name=input(('Escriba su nombre: '))
print('Elija una opcion: ')
option=int(input('1- Si quiere su nombre en mayusculas\n2- Si quiere su nombre en minusculas\n3- Si quiere su primer letra en mayusculas\n'))
if option == 1:
    name = name.upper()
    print(name)
elif option == 2: 
    name = name.lower()
    print(name)
elif option == 3 :
    name = name.title()
    print(name)
else: print('error')