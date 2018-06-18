'''nombre = "Jose"
print(type(nombre))

longitud = 850
print(type(longitud))

precio = 940.65
print(type(precio))

archivo = open("agenda.txt", "a+")
print(dir(archivo))
print(type(archivo.name))
print(type(archivo.write))

print(dir(str))'''

class Estrella(object):

    def __init__(self, nombreConstructor, colorConstructor, tipoConstructor):
        if(isinstance(nombreConstructor, str)):
            self.nombre = nombreConstructor
            self.color = colorConstructor
            self.tipo = tipoConstructor
        else:
            raise TypeError("El nombre tiene que ser un string")

class Coordenada(object):

    def __init__(self, valorx=0, valory=0):
        if(isinstance(valorx, (int, float)) and isinstance(valorx, (int, float))) :
            self.x = valorx
            self.y = valory
        else:
            raise TypeError("x e y deben ser valores numericos")

    def __str__(self):
        return("(" + str(self.x) + ", " + str(self.y) + ")")

    def __add__(self, otra):
        return Coordenada(self.x + otra.x, self.y + otra.y)

    def __sub__(self, otra):
        return Coordenada(self.x - otra.x, self.y - otra.y)

    def restar(self, otra):
        return Coordenada(otra.x - self.x, otra.y - self.y)

    def norma(self):
        return(self.x **2) + (self.y ** 2) ** 0.5

    def distancia(self, otra):
        '''distx = otra.x - self.x
        disty = otra.y - self.y'''
        nuevacoor = self.restar(otra)
        return(nuevacoor.norma())

objetoEstrella = Estrella("Suhail", "rojo", "Ib")

print("Nombre: " + objetoEstrella.nombre + "\r")
print("Color: " + objetoEstrella.color + "\r")
print("Tipo: " + objetoEstrella.tipo + "\r")

objetoCoordenada1 = Coordenada(0, 0)
objetoCoordenada2 = Coordenada(10, 10)
objetoCoordenada3 = objetoCoordenada1.restar(objetoCoordenada2)

print("\rPrimera Coordenada: " + str(objetoCoordenada1.y) + ", " + str(objetoCoordenada1.y))
print("\rSegunda Coordenada: " + str(objetoCoordenada2.y) + ", " + str(objetoCoordenada2.y))
print("\rTercera Coordenada: " + str(objetoCoordenada3.y) + ", " + str(objetoCoordenada3.y))
print("\rNorma: " + str(objetoCoordenada1.distancia(objetoCoordenada2)))
print("\rCoincide con Distancia: " + str(objetoCoordenada1.distancia(objetoCoordenada2)))
print("\rContenido Primera Coordinada: " + str(objetoCoordenada1))

inicio = Coordenada(100, 100)
fin = Coordenada(250, 250)

print("\rCoordenada Inicial: " + str(inicio))
print("\rCoordenada Final: " + str(fin))
print("\rLa resta de coordenadas es " + str (inicio - fin))
print("\rLa suma de coordenadas es " + str(inicio + fin))
