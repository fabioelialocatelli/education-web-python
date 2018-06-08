import os
import sys
import random

carpeta = os.getcwd()
print("ejemplos modulo OS")
print("Carpeta de trabajo actual: " + carpeta)
if(os.path.exists(carpeta + "\\Soluciones")):
    print("Carpeta encontrada")
else:
    print("Carpeta Inexistente")

print("\n")
print("ejemplos modulo SYS")
print("La ruta y nombre del interprete python es " + sys.executable)
print("La plataforma de trabajo es " + sys.platform)
print("La informacion sobre esta version de Python es " + sys.version)

print("\n")
print("ejemplos modulo RANDOM")

contador = 1
linea = ""

while contador <= 10:
    linea += " " + str(random.randint(1, 10))
    contador += 1

print("Diversos numeros al azar entre 1 y 10:")
print(linea)

lista = ["Acamar", "Canopus", "Arcturus", "Hydor"]

print("Una estrella al azar: " + str(random.sample(lista, 1)))
print("Dos estrellas al azar: " + str(random.sample(lista, 2)))

random.shuffle(lista)
print("Estrellas mezcladas: " + str(lista))

