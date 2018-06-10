# -*- coding: utf-8 -*-
import random


def azar(maximo):
    return random.randint(1, maximo)


def mensajeAcierto():
    print("Acertaste!")


def mensajeFallo():
    print("Lo sentimos, fallaste!")


def mensajeFin(numero):
    print("No hay oportunidades, no acertaste! el número era el " + str(numero))
