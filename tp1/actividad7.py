print('Ingrese una frase o palabra: ')
frase=str(input())
ultimo = frase [-1]
if ultimo in 'aeiou':
    print(frase + '!')
else: print (frase)

