class Clase1(object):

    def __init__(self, mivalor):
        self.valor = mivalor

    def __str__(self):
        return "###" + self.valor + "###"

class Clase2(object):

    def __init__(self, mivalor):
        self.valor = mivalor

    def __str__(self):
        return "@@@" + self.valor + "@@@"

objetoClase1 = Clase1("Hola")
objetoClase2 = Clase2("Adios")

print(str(objetoClase1))
print(str(objetoClase2))
