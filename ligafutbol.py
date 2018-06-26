ligaFutbol = {"FC Barcelona": 0, "Getafe": 0, "Granada CF": 0, "Malaga": 0, "Sevilla": 0, "Valencia": 0}
equipos = ligaFutbol.items()

numeroEquipos = 0
numeroGoles = 0

valorMaximoGoles = 0
valorMinimoGoles = 300

equipoMasGoles = ""
equipoMenosGoles = ""

print("LIGA DE FUTBOL\n")

for equipo in equipos:
    golesEquipo = eval(input("Goles del " + equipo[0] + ": "))

    ligaFutbol[equipo[0]] = golesEquipo    
    numeroEquipos += 1
    numeroGoles += golesEquipo
    
    if(golesEquipo > valorMaximoGoles):
        valorMaximoGoles = golesEquipo
        equipoMasGoles = equipo[0]
    
    if(golesEquipo < valorMinimoGoles):
        valorMinimoGoles = golesEquipo
        equipoMenosGoles = equipo[0]

print("\nPromedio de goles: " + str(numeroGoles / numeroEquipos))
print("Equipo con mas goles (" + str(valorMaximoGoles) + "): " + equipoMasGoles)
print("Equipo con menos goles (" + str(valorMinimoGoles) + "): " + equipoMenosGoles)

ligaFutbol.pop(equipoMasGoles)
ligaFutbol.pop(equipoMenosGoles)

print("\nLa liga discriminando al maximo y al minimo queda:")

equiposIntermedios = ligaFutbol.items()
for equipoIntermedio in equiposIntermedios:
    print("• " + equipoIntermedio[0] + "\n")
