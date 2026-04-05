num=int(input('Escriba la magnitud de un terremoto: '))
if num < 3:
    print('Muy leve (imperceptible)')
elif num >= 3 and num < 4:
    print('Leve (ligeramente perceptible)')
elif num >= 4 and num < 5:
    print('Moderado (sentido por personas, pero generalmente no causa daños)')
elif num >= 5 and num < 6:
    print('Fuerte (puede causar daños en estructuras débiles)')
elif num >= 6 and num < 7:
    print('Muy fuerte (puede causar daños significativos)')
else: print('Extremo (puede casuar daños a gran escala)')