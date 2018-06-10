print("Resultado Clasico".upper())
cadena = input("Indique el resultado del partido mas reciente: ")
espacios = cadena.count(" ")

if(espacios != 3):
    print("Formato erroneo")
else:
    barcelona = cadena.find("Barcelona")
    madrid = cadena.find("Madrid")
    if(barcelona == -1 or madrid == -1):
        print("Equipos incorrectos")
    elif(barcelona < madrid):
        print("Jugado en el Camp Nou")
    elif(barcelona > madrid):
        print("Jugado en el Santiago Bernabeu")
