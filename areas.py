import gi
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def areaCilindro(boton):
    PIgriego = 3.141516
    radio = float(constructorInterfaz.get_object("base").get_text())
    altura = float(constructorInterfaz.get_object("altura").get_text())
    area = round((2 * PIgriego * radio * altura), 4)
    etiqueta = constructorInterfaz.get_object("resultado")
    etiqueta.set_text(str(area))

def areaRectangulo(boton):
    base = float(constructorInterfaz.get_object("base").get_text())
    altura = float(constructorInterfaz.get_object("altura").get_text())
    area = round((base * altura), 4)
    etiqueta = constructorInterfaz.get_object("resultado")
    etiqueta.set_text(str(area))

def areaTriangulo(boton):
    base = float(constructorInterfaz.get_object("base").get_text())
    altura = float(constructorInterfaz.get_object("altura").get_text())
    area = round(((base * altura) / 2), 4)
    etiqueta = constructorInterfaz.get_object("resultado")
    etiqueta.set_text(str(area))

constructorInterfaz = Gtk.Builder()
constructorInterfaz.add_from_file("areas.glade")

botonCilindro = constructorInterfaz.get_object("cilindro")
botonCilindro.connect("clicked", areaCilindro)

botonRectangulo = constructorInterfaz.get_object("rectangulo")
botonRectangulo.connect("clicked", areaRectangulo)

botonTriangulo = constructorInterfaz.get_object("triangulo")
botonTriangulo.connect("clicked", areaTriangulo)

interfazUsuario = constructorInterfaz.get_object("ventana")
interfazUsuario.connect("delete-event", Gtk.main_quit)
interfazUsuario.show_all()
Gtk.main()
