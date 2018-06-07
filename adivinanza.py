def adivinanza(intento=1):
    respuesta = input("¿Cual es la estrella mas cercana? ")
    if respuesta != "Proxima":
        
        if intento < 5:
            print("Fallaste! Intentalo de nuevo")
            intento += 1
            
            adivinanza(intento)
            
        elif intento == 5:
            print("Perdiste! Se acabaron las oportunidades")
            
    elif respuesta == "Proxima":
        print("Ganaste! Acertado en " + str(intento) + " intento(s)")

adivinanza()
