def celsius_a_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
farenheit = celsius_a_farenheit(celsius)
print(f"{celsius} grados Celsius son {farenheit:.2f} grados Farenheit.")