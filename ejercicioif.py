jugadaI = input("Jugada I")
jugadaII = input("Jugada II")
resultado = ""

if jugadaI == jugadaII:
    resultado = "empatamos"
elif jugadaI == "piedra" and jugadaII == "piedra":
    resultado = "gano"
elif jugadaI == "piedra" and jugadaII == "papel":
    print("pierdo")
elif jugadaI == "piedra" and jugadaII == "tijeras":
    print("gano")
else:
    print("no vale")

print("Tu jugada es " + jugadaII
     + " y mi jugada es " + jugadaII + " por lo tanto " + resultado)
