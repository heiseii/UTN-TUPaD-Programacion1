#Registro de notas y promedio
for i in range(3):
    alumnos = input("Ingrese el nombre del alumno numero " + str(i+1) + ": ") 
    #Se agregan 3 alumnos y para cada uno una tupla de 3 notas:
    notas = ()
    for j in range(3):
        nota = float(input("Ingrese la nota numero " + str(j+1) + " del alumno " + alumnos + ": "))
        notas += (nota,)
        #Se calcula el promedio de las notas de cada alumno
    promedio = sum(notas) / len(notas) 
    print("El promedio de " + alumnos + " es: " + str(promedio))