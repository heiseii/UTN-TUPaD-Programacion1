print('Ingrese su contraseña de entre 8 y 14 caracteres: ')
passw=input()
if len(passw) >= 8 and len(passw) <= 14:
    print('Acceso valido')
else: print('Introduzca una contraseña valida')
