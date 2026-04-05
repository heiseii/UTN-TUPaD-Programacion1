energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
spam = 0

print("""--- ¡Bienvenido al juego de escape room! ---
    Sos un agente que intenta abrir una boveda con 3 cerraduras. Tenes energia y tiempo limitados.
    Si abris las 3 cerraduras antes de que se acabe el tiempo, ganas. ¡Buena suerte!
    """)

agente = input("Ingrese el nombre del agente: ")
while agente.isalpha() == False or agente == "":
    print("El nombre del agente no puede contener números, estar vacio o caracteres especiales. Intente nuevamente.")
    agente = input("Ingrese el nombre del agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    print(f"\nAgente: {agente} | Energia: {energia} | Tiempo restante: {tiempo}hs | Cerraduras abiertas: {cerraduras_abiertas}/3 | Alarma: {'ON' if alarma else 'OFF'}")
    accion = input("""¿Qué acción desea realizar?
1 - Forzar cerradura  ( costo: -20 energia, -2 tiempo )
2 - Hackear panel     ( costo: -10 energia, -3 tiempo )
3 - Descansar         ( +15 energia (max 100), -1 tiempo; si alarma ON: -10 energia extra )
Opcion: """)
    while accion != "1" and accion != "2" and accion != "3":
        print("Acción no válida, intente nuevamente.")
        accion = input("""¿Qué acción desea realizar?
1 - Forzar cerradura  ( costo: -20 energia, -2 tiempo )
2 - Hackear panel     ( costo: -10 energia, -3 tiempo )
3 - Descansar         ( +15 energia (max 100), -1 tiempo; si alarma ON: -10 energia extra )
Opcion: """)

    # forzar cerradura
    if accion == "1":
        energia -= 20
        tiempo -= 2
        spam += 1

        if spam == 3:
            alarma = True
            spam = 0
            print("Forzaste la cerradura 3 veces seguidas. ¡La cerradura se trabó y se activó la alarma!")
        else:
            if energia < 40:
                print("Advertencia: tu energía está por debajo de 40. Hay riesgo de alarma.")
                numero_alarma = input("Ingrese un numero del 1 al 3: ")
                while numero_alarma.isdigit() == False or int(numero_alarma) < 1 or int(numero_alarma) > 3:
                    print("Número inválido, ingrese un número del 1 al 3.")
                    numero_alarma = input("Ingrese un numero del 1 al 3: ")
                if int(numero_alarma) == 3:
                    alarma = True
                    print("Elegiste el 3. ¡Se activó la alarma!")
                else:
                    cerraduras_abiertas += 1
                    print(f"Cerradura forzada con éxito. Cerraduras abiertas: {cerraduras_abiertas}/3")
            else:
                cerraduras_abiertas += 1
                print(f"Cerradura forzada con éxito. Cerraduras abiertas: {cerraduras_abiertas}/3")

    # hackear panel
    elif accion == "2":
        spam = 0
        energia -= 10
        tiempo -= 3
        print("Hackeando panel...")
        for i in range(4):
            codigo_parcial += "A"  
            print(f"  Paso {i + 1}/4 — Código parcial: {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print(f"¡Código suficiente! Se abrió una cerradura automáticamente. Cerraduras abiertas: {cerraduras_abiertas}/3")

    # descansar
    elif accion == "3":
        spam = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma == True:
            energia -= 10
            print("La alarma está activa: perdiste 10 de energía extra.")
        print(f"Descansaste. Energía actual: {energia}")

    # condiciones de victoria o derrota
    if cerraduras_abiertas == 3:
        print(f"\n¡Felicidades, {agente}! Abriste las 3 cerraduras y escapaste.")
        break
    elif energia <= 0 or tiempo <= 0:
        print(f"\nDerrota: te quedaste sin {'energía' if energia <= 0 else 'tiempo'}, {agente}.")
        break
    elif alarma == True and tiempo <= 3:
        print(f"\nDerrota: la alarma está activa y el tiempo se agotó. El sistema se bloqueó, {agente}.")
        break