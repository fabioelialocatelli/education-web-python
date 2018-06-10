# -*- coding: utf-8 -*-
from modulo.funciones import azar
from modulo.funciones import mensajeAcierto as msgAcierto
from modulo.funciones import mensajeFallo as msgFallo
from modulo.funciones import mensajeFin as msgFin

numeroAzar = azar(10)
contador = 1
acierto = False
while contador <= 3 and acierto is False:
    numeroUsuario = eval(input("Dame un numero:"))
    if numeroAzar == numeroUsuario:
        msgAcierto()
        acierto = True
    else:
        msgFallo()
    contador = contador + 1
if(not acierto):
    msgFin(numeroAzar)
