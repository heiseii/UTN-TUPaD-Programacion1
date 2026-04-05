#Arena del gladiador
hp = 100
hp_enemigo = 100
pots = 3
dmg =15
dmg_enemigo = 12
turno = True
print("¡Bienvenido a la Arena del Gladiador!")
nombre = input("Ingrese el nombre de su gladiador: ")
while nombre.isalpha() == False or nombre == "":
    print("El nombre del gladiador no puede contener números, estar vacio o caracteres especiales. Intente nuevamente.")
    nombre = input("Ingrese el nombre de su gladiador: ")
while hp > 0 and hp_enemigo > 0:
    print(f"\n{nombre} - HP: {hp} | Enemigo - HP: {hp_enemigo} | Pociones restantes: {pots}")
    if turno:
        accion = input("""¿Qué acción desea realizar? 
            1 - Atacar |
            2 - Ráfaga velóz | 
            3 - Usar poción |
     """)
        while accion != "1" and accion != "2" and accion != "3":
            print("Acción no válida, intente nuevamente.")
            accion = input("""¿Qué acción desea realizar? 
            1 - Atacar |
            2 - Ráfaga velóz | 
            3 - Usar poción |
     """)
        if accion == "1":
            hp_enemigo -= dmg
            print(f"¡Atacaste al enemigo y le hiciste {dmg} de daño!")
        elif accion == "1" and hp_enemigo <= 20 and hp_enemigo > 0:
            print("Haz realizado un golpe critico!")
            dmg = dmg * 1.5
            hp_enemigo -= dmg
            print(f"¡Atacaste al enemigo y le hiciste {dmg} de daño!")
        elif accion == "2":
            for i in range(3):
                hp_enemigo -= 5
                dmg_rafaga = 5
                print(f"¡Ráfaga velóz! Ataque {i + 1}/3: le hiciste {dmg_rafaga} de daño al enemigo!")
        else:
            if pots > 0 and hp < 100:
                hp += 30
                pots -= 1
                print("¡Usaste una poción y recuperaste 30 HP!")
            elif pots == 0:
                print("No tienes pociones restantes.")
            else:
                print("Tu HP ya está al máximo.")
    else:
        hp -= dmg_enemigo
        print(f"El enemigo te atacó por {dmg_enemigo} puntos de daño!")
    turno = not turno

if hp <= 0 and hp_enemigo <= 0:
    print("¡Es un empate! Ambos gladiadores han caído.")
elif hp <= 0:
    print("DERROTA")
else:    
    print("VICTORIA")