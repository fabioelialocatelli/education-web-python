# -*- coding: utf-8 -*-
from modulo.funciones import devuelveAzar as elAzar
from modulo.funciones import mensajeAcertado as elAcierto
from modulo.funciones import mensajeFallado as elFallo
from modulo.funciones import mensajeFinalizado as elFinal

contador = 1
hasAcertado = False
numeroAzar = elAzar(15)

while contador <= 3 and hasAcertado is False:
    numeroUsuario = eval(input("Digame numero por favor:"))

    if numeroAzar == numeroUsuario:
        elAcierto()
        hasAcertado = True
    else:
        elFallo()
        
    contador += 1
if(not hasAcertado):
    elFinal(numeroAzar)
