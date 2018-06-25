print("GESTIÓN DE INCIDENCIAS".center(80, "-"))

incidencia = input("Indique la incidencia: ").upper()
respuesta = "INCIDENCIA NO RECONOCIDA"

if incidencia.startswith("ERROR"):
    paneles = incidencia.count("PANEL")
    if paneles == 1:
        respuesta = "Detectado un error en " + str(paneles) + " panel"
    elif paneles > 1:
            respuesta = "Detectado un error en " + str(paneles) + " paneles"
else:
    if incidencia.startswith("AVISO") and incidencia.count("CONMUTADOR") == 1:
        if incidencia.endswith("VERDE"):
            respuesta = "Atasco en puerta de salida"
        elif incidencia.endswith("AZUL"):
                respuesta = "Reponer aceite en cinta"
print(respuesta)
