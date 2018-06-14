# -*- coding: utf-8 -*-

import gi
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

fichero = "agenda.txt"

def borraRegistro(boton):
    #global fichero
    try:
        ultimo = fichero.tell() - 50
        actual = 0
        fichero.seek(actual)
        # Obtenemos el nombre y le añadimos los espacios igual que al guardar
        nombre_saltar = constructorInterfaz.get_object("nombre").get_text().ljust(20)
        ficherotemp = open("agendatemporal.txt", "w")
        while(actual <= ultimo):
            nombre = fichero.read(20)
            email = fichero.read(30)
            # Si no coinciden los nombres, lo guardamos en el archivo temporal
            if(nombre != nombre_saltar):
                ficherotemp.write(nombre + email)
            actual += 50
        # Cerramos los dos y hacemos el cambio del temporal por el original
        fichero.close()
        ficherotemp.close()
        os.remove(fichero)
        os.rename("agendatemporal.txt", fichero)
        # Lo dejamos como estaba
        fichero = open(fichero, "a+")
        print("Operación finalizada.")
    except NameError:
        print("ERROR: El archivo no se ha abierto aun!")

def listaRegistro(boton):
    # restamos 50 del ultimo caracter para saber
    # donde comienza el ultimo registro
    try:
        final = fichero.tell() - 50
        actual = 0
        fichero.seek(actual)
        print("contenido de la agenda".upper().center(70, "="))
        while(actual <= final):
            nombre = fichero.read(20)
            email = fichero.read(30)
            print("Nombre: " + nombre + "Email: " + email)
            actual += 50
    except NameError:
        print("ERROR: El archivo no se ha abierto aun!")

def anadeRegistro(boton):
    minombre = constructorInterfaz.get_object("nombre")
    miemail = constructorInterfaz.get_object("email")
    registro = minombre.get_text().ljust(20) + miemail.get_text().ljust(30)
    try:
        fichero.write(registro)
        print("Registro añadido: " + registro)
        minombre.set_text("")
        miemail.set_text("")
    except NameError:
        print("ERROR: El archivo no se ha abierto aun!")

def eliminamosArchivo(boton):
    try:
        if(fichero.closed is False):
            fichero.close()
            print("El archivo estaba abierto, ha habido que cerrarlo.")
        os.remove(fichero.name)
        print("Archivo eliminado.")
    except NameError:
        print("ERROR: El archivo no se ha abierto aun!")

def creamosArchivo(boton):
    global fichero
    fichero = open(fichero, "a+")
    print("archivo " + fichero.name + " preparado.")
    if(fichero.closed):
        print("Está cerrado")
    else:
        print("Está abierto.")
        print("Modo de apertura: " + fichero.mode)


constructorInterfaz = Gtk.Builder()
constructorInterfaz.add_from_file("ficheros2.glade")

botonCreado = constructorInterfaz.get_object("crear")
botonCreado.connect("clicked", creamosArchivo)

botonEliminado = constructorInterfaz.get_object("eliminar")
botonEliminado.connect("clicked", eliminamosArchivo)

botonAnadido = constructorInterfaz.get_object("anadir")
botonAnadido.connect("clicked", anadeRegistro)

botonlistado = constructorInterfaz.get_object("listar")
botonlistado.connect("clicked", listaRegistro)

botonBorrado = constructorInterfaz.get_object("borrar")
botonBorrado.connect("clicked", borraRegistro)

interfazUsuario = constructorInterfaz.get_object("ventana")
interfazUsuario.connect("delete-event", Gtk.main_quit)
interfazUsuario.show_all()
Gtk.main()
