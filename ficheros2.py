import gi
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def creamosArchivo(boton):
    fichero = open("agenda.txt", "a+")
    print("Archivo preparado.")
    if(fichero.closed):
        print("Esta cerrado.")
    else:
        print("Esta abierto.")
        print("Modo de apertura: " + fichero.mode)

def eliminamosArchivo(boton):
    fichero = open("agenda.txt", "w")
    try:
        if(fichero.closed is False):
            fichero.close()
            print("El archivo estaba abierto, ha habido que cerrarlo.")
        os.remove("agenda.txt")
        print("Archivo eliminado.")
    except NameError:
        print("ERROR: El archivo no se ha abierto aun!")

def borraRegistro(boton):
    fichero = open("agenda.txt", "r+")
    try:
                
        nombreSaltar = constructorInterfaz.get_object("nombre").get_text()
        emailSaltar = constructorInterfaz.get_object("email").get_text()

        ficheroTemporal = open("agendaTemporal.tmp", "w")        

        palabras = (nombreSaltar, emailSaltar)
        for line in fichero:
            for palabra in palabras:
                if(palabra not in line):
                    ficheroTemporal.write(line)
        
        fichero.close()
        ficheroTemporal.close()

        os.remove("agenda.txt")
        os.rename("agendaTemporal.tmp", "agenda.txt")
        
        print("Operacion finalizada.")
    except NameError:
        print("ERROR: El archivo no se ha abierto aun!")

def listaRegistro(boton):
    fichero = open("agenda.txt", "r")
    try:
        
        print("contenido de la agenda".upper().center(70, "="))
        contenido = fichero.readlines()
        for linea in contenido:
            print(linea)
        
    except NameError:
        print("ERROR: El archivo no se ha abierto aun!")
    fichero.close()

def anadeRegistro(boton):
    fichero = open("agenda.txt", "a+")
    nombreContacto = constructorInterfaz.get_object("nombre")
    emailContacto = constructorInterfaz.get_object("email")

    registro = nombreContacto.get_text().ljust(20) + emailContacto.get_text().ljust(30)

    try:
        fichero.write(registro + "\n")
        print("Registro anadido: " + registro)
        
    except NameError:
        print("ERROR: El archivo no se ha abierto aun!")

    nombreContacto.set_text("")
    emailContacto.set_text("")
    fichero.close()

constructorInterfaz = Gtk.Builder()
constructorInterfaz.add_from_file("ficheros2.glade")

botonCreado = constructorInterfaz.get_object("crear")
botonCreado.connect("clicked", creamosArchivo)

botonEliminado = constructorInterfaz.get_object("eliminar")
botonEliminado.connect("clicked", eliminamosArchivo)

botonAnadido = constructorInterfaz.get_object("anadir")
botonAnadido.connect("clicked", anadeRegistro)

botonBorrado = constructorInterfaz.get_object("borrar")
botonBorrado.connect("clicked", borraRegistro)

botonListado = constructorInterfaz.get_object("listar")
botonListado.connect("clicked", listaRegistro)

interfazUsuario = constructorInterfaz.get_object("ventana")
interfazUsuario.connect("delete-event", Gtk.main_quit)
interfazUsuario.show_all()
Gtk.main()
