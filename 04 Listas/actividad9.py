#Actividad 9
tablero = [
    [" - ", " - ", " - "],
    [" - ", " - ", " - "],
    [" - ", " - ", " - "]
]
print("TABLERO INICIAL:")
for fila in tablero:
    print("".join(fila))
jugador_1 = "Jugador 1 (X)"
jugador_2 = "Jugador 2 (O)"
jugador_actual = jugador_1
#ingreso de jugada
while True:
    fila = int(input(f"{jugador_actual}, ingresa la fila (1, 2, 3): "))
    columna = int(input(f"{jugador_actual}, ingresa la columna (1, 2, 3): "))
    if tablero[fila-1][columna-1] == " - ":
        tablero[fila-1][columna-1] = " " + jugador_actual + " "
    else:
        print("Esa posición ya está ocupada. Intenta de nuevo.")
        continue
    for fila in tablero:
        print("".join(fila))
#condicionales de posiciones de fichas
    if (tablero[0][0] == tablero[0][1] == tablero[0][2] != " - ") or \
       (tablero[1][0] == tablero[1][1] == tablero[1][2] != " - ") or \
       (tablero[2][0] == tablero[2][1] == tablero[2][2] != " - ") or \
       (tablero[0][0] == tablero[1][0] == tablero[2][0] != " - ") or \
       (tablero[0][1] == tablero[1][1] == tablero[2][1] != " - ") or \
       (tablero[0][2] == tablero[1][2] == tablero[2][2] != " - ") or \
       (tablero[0][0] == tablero[1][1] == tablero[2][2] != " - ") or \
       (tablero[0][2] == tablero[1][1] == tablero[2][0] != " - "):
        print("¡Jugador " + jugador_actual + " gana!")
        break
    if all(tablero[i][j] != " - " for i in range(3) for j in range(3)):
        print("¡Empate!")
        break
    jugador_actual = jugador_2 if jugador_actual == jugador_1 else jugador_1
