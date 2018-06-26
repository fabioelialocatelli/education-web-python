print("GESTION DE INCIDENCIAS".center(90, "-"))

incidencia = input("Indique la incidencia: ").upper()
respuesta = "INCIDENCIA NO RECONOCIDA"

if(incidencia.startswith("AVERIA") or incidencia.startswith("ERROR")):
    panelesAfectados = incidencia.count("PANEL")
    if(panelesAfectados == 1):
        respuesta = "Detectado un error en " + str(panelesAfectados) + " panel"
    elif(panelesAfectados > 1):
        respuesta = "Detectado un error en " + str(panelesAfectados) + " paneles"
else:
    if(incidencia.startswith("AVISO") and incidencia.count("CONMUTADOR") == 1):
        if(incidencia.endswith("VERDE")):
            respuesta = "Atasco en puerta de salida"
        elif(incidencia.endswith("AZUL")):
            respuesta = "Reponer aceite en cinta"
print(respuesta)
