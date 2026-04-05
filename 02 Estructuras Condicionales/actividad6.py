kwh=int(input('Ingrese su consumo en kilovatios (kWh): '))
if kwh < 150:
    print('Consumo bajo')
elif kwh >= 150 and kwh <= 300:
    print('Consumo Medio')
else: print('Consumo alto')
