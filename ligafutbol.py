ligaFutbol = {"FC Barcelona": 0, "Getafe": 0, "Granada CF": 0, "Malaga": 0, "Sevilla": 0, "Valencia": 0}
equipos = ligaFutbol.items()

numeroEquipos = 0
numeroGoles = 0

masGoles = 0
equipoMasGoles = ""

menosGoles = 300
equipoMenosGoles = ""

print("LIGA DE FUTBOL\n")

for equipo in equipos:
    golesEquipo = eval(input("Goles del " + equipo[0] + ": "))

    ligaFutbol[equipo[0]] = golesEquipo    
    numeroEquipos += 1
    numeroGoles += golesEquipo
    
    if(golesEquipo > masGoles):
        masGoles = golesEquipo
        equipoMasGoles = equipo[0]
    
    if(golesEquipo < menosGoles):
        menosGoles = golesEquipo
        equipoMenosGoles = equipo[0]

print("\nPromedio de goles: " + str(numeroGoles / numeroEquipos))
print("Equipo con maximo de goles (" + str(masGoles) + "): " + equipoMasGoles)
print("Equipo con minimo de goles (" + str(menosGoles) + "): " + equipoMenosGoles)

ligaFutbol.pop(equipoMasGoles)
ligaFutbol.pop(equipoMenosGoles)

print("\nLa liga discriminando al maximo y al minimo queda:")
print(ligaFutbol)
