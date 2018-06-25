import random

def devuelveAzar(maximo):
    return random.randint(1, maximo)

def mensajeAcertado():
    print("Acertaste!")

def mensajeFallado():
    print("Lo sentimos, fallaste!")

def mensajeFinalizado(numero):
    print("Lo sentimos, no hay mas oportunidades. El numero era el " + str(numero))
