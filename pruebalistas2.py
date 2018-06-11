jugadores = []
equipos = []
listado = [jugadores, equipos]

jugador = ""

while jugador.upper() != "FIN":
    jugador = input("Nombre del jugador (FIN para acabar): ")
    if jugador.upper() != "FIN":
        equipo = input("Nombre del equipo: ")
        jugadores.append(jugador)
        equipos.append(equipo)
print("\n\nDATOS INTRODUCIDOS")
print("\n\nCONSULTAS")

equipo = ""

while equipo.upper() != "FIN":
    equipo = input("Nombre del equipo (FIN para acabar): ")
    if equipo.upper() != "FIN":
        if equipo in equipos:
            print("JUGADORES: ", end="")
        for i in range(len(equipos)):
            if listado[1][i] == equipo:
                print(listado[0][i].ljust(20, end="")
    else:
        print("\nEquipo no encontrado")
