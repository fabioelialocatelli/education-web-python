import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def mostrarAsignadas(boton):
    mostrarEstado("ASIGNADA")

def mostrarDenegadas(boton):
    mostrarEstado("DENEGADA")

def mostrarEstado(estado):
    
    fichero = open("becas.txt", "r")

    if(estado == "ASIGNADA"):
        print("ALUMNOS CON BECAS ASIGNADAS:")
        contenido = fichero.readlines()
        for linea in contenido:
            if("S" in linea):
                print(linea)
    else:
        print("ALUMNOS CON BECAS DENEGADAS:")
        contenido = fichero.readlines()
        for linea in contenido:
            if("DENEGADA" in linea):
                print(linea)

    fichero.close()

def agregamosBeca(boton):
    fichero = open("becas.txt", "a+")
    campoNombre = constructorInterfaz.get_object("campoNombre")
    campoApellido = constructorInterfaz.get_object("campoApellido")
    campoExpediente = constructorInterfaz.get_object("campoExpediente")
    campoAsignacion = constructorInterfaz.get_object("campoAsignacion")

    registro = campoNombre.get_text() + " " + campoApellido.get_text() + " " + campoExpediente.get_text() + " " + campoAsignacion.get_text().upper() + "\n"
    fichero.write(registro)

    print("Entrada anadida: " + registro)
    campoNombre.set_text("")
    campoApellido.set_text("")
    campoExpediente.set_text("")
    campoAsignacion.set_text("")


constructorInterfaz = Gtk.Builder()
constructorInterfaz.add_from_file("becas.glade") #cargando el archivo XML construido en Glade

botonDenegadas = constructorInterfaz.get_object("botonDenegadas") #extraccion de objeto
botonDenegadas.connect("clicked", mostrarDenegadas) #asignacion de metodo

botonAsignadas = constructorInterfaz.get_object("botonAsignadas")
botonAsignadas.connect("clicked", mostrarAsignadas)

botonAgregacion = constructorInterfaz.get_object("botonAgregacion")
botonAgregacion.connect("clicked", agregamosBeca)

ventana = constructorInterfaz.get_object("ventana")
ventana.connect("delete-event", Gtk.main_quit)
ventana.show_all() #mostramos todos los componentes
Gtk.main() #esto seria el equivalente del mainloop() de TKinter
