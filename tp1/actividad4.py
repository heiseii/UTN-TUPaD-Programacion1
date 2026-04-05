age=int(input('Ingrese su edad: '))
if age < 12 and age >= 0:
    print('Usted es un/a niño/a')
elif age >= 12 and age < 18:
    print('Usted es un/a adolescente')
elif age >= 18 and age < 30:
    print('Usted es un/a adulto/a joven')
elif age >= 30:
     print('Usted es un adulto')
else: print('Ingrese un numero válido')