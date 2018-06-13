import os
from tkinter import *


def crearArchivo():
    fichero = open("agenda.txt", "a+")
    print("archivo " + fichero.name + " preparado.")
    if(fichero.closed):
        print("Fichero cerrado")
    else:
        print("Fichero abierto")
        print("Modo de apertura: " + fichero.mode)


def eliminarArchivo():
    fichero = "agenda.txt"
    if os.path.isfile(fichero):
        os.unlink(fichero)
        print("Archivo eliminado")
    else:
        print("Archivo no encontrado")


def anadirDatos():
    nombre = varNombre.get()
    apellidos = varApellidos.get()
    registro = nombre.ljust(20) + apellidos.ljust(30)
    fichero = open("agenda.txt", "a+")
    fichero.write(registro + "\r")
    print("Registro anadido: " + registro)


def listado():
    fichero = "agenda.txt"
    if os.path.isfile(fichero):
        entradas = tuple(open(fichero, "r"))
        for contacto in entradas:
            print(contacto)
    else:
        print("Archivo no encontrado")

fichero = ""
ventana = Tk()
ventana.title("Ficheros")

varNombre = StringVar()
varApellidos = StringVar()

boton1 = Button(ventana, text="Crear", command=crearArchivo)
boton2 = Button(ventana, text="Eliminar", command=eliminarArchivo)
boton3 = Button(ventana, text="Anadir", command=anadirDatos)
boton4 = Button(ventana, text="Leer", command=listado)

cuadro1 = Entry(ventana, textvariable=varNombre)
cuadro2 = Entry(ventana, textvariable=varApellidos)

boton1.grid(row=0, column=0)
boton2.grid(row=1, column=0)
boton3.grid(row=2, column=0)
boton4.grid(row=3, column=0)

cuadro1.grid(row=0, column=1)
cuadro2.grid(row=1, column=1)

ventana.mainloop()
