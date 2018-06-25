import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

global fichero
fichero = open("becas.txt", "a+") #esto se parece muchisimo al Perl

def mostrarAsignadas(boton):
    mostrarEstado("S")

def mostrarDenegadas(boton):
    mostrarEstado("N")

def mostrarEstado(estado):
    final = fichero.tell() - 61 #posicion del cursor menos el numero de bytes
    actual = 0
    fichero.seek(actual) #posicion actual del cursor
    if(estado == "S"):
        print("ALUMNOS CON BECAS ASIGNADAS:")
    else:
        print("ALUMNOS CON BECAS DENEGADAS:")
    while(actual <= final):
        campoNombre = fichero.read(20)
        campoApellido = fichero.read(30)
        campoExpediente = fichero.read(10)
        campoAsignacion = fichero.read(1) #el numero de bytes determina la posicion donde cada atributo esta en el registro
        if(campoAsignacion.upper() == estado):
            print(campoExpediente + " " + campoApellido.strip() + ", " + campoNombre.strip())
        actual += 61 # adelantamos de un registro

def agregamosBeca(boton):
    campoNombre = constructorInterfaz.get_object("campoNombre")
    campoApellido = constructorInterfaz.get_object("campoApellido")
    campoExpediente = constructorInterfaz.get_object("campoExpediente")
    campoAsignacion = constructorInterfaz.get_object("campoAsignacion")

    #aqui se ve que cada registro ocupa 61 bytes. personalmente esto la haria con una base de datos, mucho mas sencillo
    registro = campoNombre.get_text().ljust(20) + campoApellido.get_text().ljust(30) + campoExpediente.get_text().ljust(10) + campoAsignacion.get_text().ljust(1).upper()
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
