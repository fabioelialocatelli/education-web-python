liga = {"FC Barcelona": 0, "Getafe": 0, "Granada CF": 0, "Malaga": 0, "Sevilla": 0, "Valencia": 0}

numeroEquipos = 0
numeroGoles = 0

masGoles = 0
equipoMasGoles = ""

menosGoles = 300
equipoMenosGoles = ""

print("LIGA DE FUTBOL\n")
for clave in liga.items():
    goles = eval(input("Goles del " + clave[0] + ": "))
    liga[clave[0]] = goles
    # numeroEquipos y numeroGoles son para calcular el promedio de goles
    numeroEquipos += 1
    numeroGoles += goles
    # masGoles siempre tendrá el valor máximo introducido
    if goles > masGoles:
        masGoles = goles
        equipoMasGoles = clave[0]
    # menosGoles siempre tendrá el valor mínimo introducido
    if goles < menosGoles:
        menosGoles = goles
        equipoMenosGoles = clave[0]

print("\nPromedio de goles: " + str(numeroGoles / numeroEquipos))
print("Equipo con máximo de goles (" + str(masGoles) + "): " + equipoMasGoles)
print("Equipo con mínimo de goles (" + str(menosGoles) + "): " + equipoMenosGoles)

liga.pop(equipoMasGoles)
liga.pop(equipoMenosGoles)

print("\nLa liga discriminando al máximo y al mínimo queda:")
print(liga)
