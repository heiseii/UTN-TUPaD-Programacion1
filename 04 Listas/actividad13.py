#Actividad 13
puntajes = [450, 1200, 875, 990, 300, 1500, 640]
print("Puntajes de los jugadores: ", puntajes)
#jugador con el puntaje más alto
for i in range(len(puntajes)):
    puntaje_mas_alto = max(puntajes)
print("El jugador con el puntaje más alto tiene: ", puntaje_mas_alto, "puntos.")
#jugador con el puntaje más bajo
for i in range(len(puntajes)):
    puntaje_mas_bajo = min(puntajes)
print("El jugador con el puntaje más bajo tiene: ", puntaje_mas_bajo, "puntos.")
#ranking
for i in range(len(puntajes)):
    ranking = sorted(puntajes, reverse=True)
print("Ranking de jugadores de mayor a menor puntaje: ", ranking)
#990
for i in range(len(puntajes)):
    posicion_990 = puntajes.index(990) + 1
    posicion_990_rank = ranking.index(990) + 1
print("El jugador con el puntaje de 990 puntos se encuentra ", posicion_990,"° en la lista normal")
print("El jugador con el puntaje de 990 puntos se encuentra ", posicion_990_rank,"° en el ranking")