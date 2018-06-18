import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

global fichero
fichero = open("becas.txt", "a+")

def mostrarAsignadas(boton):
    mostrarEstado("S")

def mostrarDenegadas(boton):
    mostrarEstado("N")

def mostrarEstado(estado):
    final = fichero.tell() - 61
    actual = 0
    fichero.seek(actual)
    if(estado == "S"):
        print("ALUMNOS CON BECAS ASIGNADAS:")
    else:
        print("ALUMNOS CON BECAS DENEGADAS:")
    while(actual <= final):
        campoNombre = fichero.read(20)
        campoApellido = fichero.read(30)
        campoExpediente = fichero.read(10)
        campoAsignacion = fichero.read(1)
        if(campoAsignacion.upper() == estado):
            print(campoExpediente + " " + campoApellido.strip() + ", " + campoNombre.strip())
        actual += 61

def agregamosBeca(boton):
    campoNombre = constructorInterfaz.get_object("campoNombre")
    campoApellido = constructorInterfaz.get_object("campoApellido")
    campoExpediente = constructorInterfaz.get_object("campoExpediente")
    campoAsignacion = constructorInterfaz.get_object("campoAsignacion")

    # Cada registro ocupa 61 bytes (20 + 30 + 10 + 1)
    registro = campoNombre.get_text().ljust(20) + campoApellido.get_text().ljust(30) + campoExpediente.get_text().ljust(10) + campoAsignacion.get_text().ljust(1).upper()
    fichero.write(registro)

    print("Entrada anadida: " + registro)
    campoNombre.set_text("")
    campoApellido.set_text("")
    campoExpediente.set_text("")
    campoAsignacion.set_text("")

constructorInterfaz = Gtk.Builder()
constructorInterfaz.add_from_file("becas.glade")

botonDenegadas = constructorInterfaz.get_object("botonDenegadas")
botonDenegadas.connect("clicked", mostrarDenegadas)

botonAsignadas = constructorInterfaz.get_object("botonAsignadas")
botonAsignadas.connect("clicked", mostrarAsignadas)

botonAgregacion = constructorInterfaz.get_object("botonAgregacion")
botonAgregacion.connect("clicked", agregamosBeca)

ventana = constructorInterfaz.get_object("ventana")
ventana.connect("delete-event", Gtk.main_quit)
ventana.show_all()
Gtk.main()
