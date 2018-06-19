class Dispositivo(object):

    def __init__(self, puntuacion=0, precio=10000, fabricante="(Omitido)", modelo="(Omitido)", tipo="(Omitido)"):
        self.fabricante = fabricante
        self.tipo = tipo
        self.modelo = modelo

        if(isinstance(puntuacion, (int, float))):
            self.puntuacion = puntuacion
        else:
            raise TypeError("La puntuacion debe ser un numero")
        if(isinstance(precio, (int, float))):
            if precio > 0:
                self.precio = precio
            else:
                self.precio = 10000
        else:
            raise TypeError("El precio debe ser un numero")

    def __str__(self):
        return self.tipo + " fabricado por " + self.fabricante + \
        "\nModelo: " + self.modelo + \
        "\nPuntuacion: " + str(self.puntuacion) + \
        "\nPrecio: " + str(self.precio) + "$"

    def __gt__(self, otro):
        if self.tipo == otro.tipo:
            diferencia = self.calidadPrecio() - otro.calidadPrecio()
            if diferencia > 0:
                return True
            else:
                return False
        else:
            raise TypeError("Los dispositivos no son del mismo tipo")

    def __lt__(self, otro):
        if self.tipo == otro.tipo:
            diferencia = self.calidadPrecio() - otro.calidadPrecio()
            if diferencia < 0:
                return True
            else:
                return False
        else:
            raise TypeError("Los dispositivos no son del mismo tipo")

    def dimePuntuacion(self):
        return(self.puntuacion)

    def dimePrecio(self):
        return(self.precio)

    def calidadPrecio(self):
        return((self.puntuacion ** 2) * 10) / self.precio

'''objetoDispositivo1 = Dispositivo(3.25, 159, "Samsung", "Galaxy Tab 3", "Tablet")
objetoDispositivo2 = Dispositivo(4.75, 1300, "Google", "Pixel XL", "Smartphone")

print(f"{objetoDispositivo1}\r")
print(f"{objetoDispositivo2}\r")'''


'''def calidadPrecioMultiple(objeto1, objeto2):
        print("\nComparamos la relacion calidad-precio de " + 
        objeto1.fabricante + " " + objeto1.modelo +
        " con " + 
        objeto2.fabricante + " " + objeto2.modelo)
        if objeto1 > objeto2:
            return "Es mejor " + objeto1.fabricante + " " + objeto1.modelo
        elif objeto1 < objeto2:
            return "Es mejor " + objeto2.fabricante + " " + objeto2.modelo
        else:
            return "Tienen la misma relacion calidad-precio"'''

objetoDispositivo3 = Dispositivo(8.25, 780, "HTC", "One M8", "Smartphone")
objetoDispositivo4 = Dispositivo(9.25, 450, "LG", "G2", "Smartphone")
objetoDispositivo5 = Dispositivo(9.25, 450, "SONY", "Xperia Z2", "Smartphone")
objetoDispositivo6 = Dispositivo(6.82, 329, "BQ", "Tesla W8", "Smartphone")

'''print(calidadPrecioMultiple(objetoDispositivo3, objetoDispositivo4))
print(calidadPrecioMultiple(objetoDispositivo4, objetoDispositivo3))
print(calidadPrecioMultiple(objetoDispositivo4, objetoDispositivo5))'''

lista = [objetoDispositivo3, objetoDispositivo4, objetoDispositivo5, objetoDispositivo6]
lista.sort(key=Dispositivo.dimePuntuacion)

print("\rDispositivos Ordenados por Puntuacion:")

for disp in lista:
    print(" Puntuacion: " + str(disp.puntuacion) + " " + disp.fabricante + " " + disp.modelo + "Precio: " + str(disp.precio))

lista.sort(key=Dispositivo.dimePrecio)

print("\rDispositivos Ordenados por Precio:")

for disp in lista:
    print(" Puntuacion: " + str(disp.precio) + " " + disp.fabricante + " " + disp.modelo + "Precio: " + str(disp.puntuacion))
