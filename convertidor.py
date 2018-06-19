class Convertidor(object):
    def __init__(self, cambioDia):
        self.cambio = cambioDia
        self.cantidadEuros = 0
        self.cantidadDolares = 0

    def convertirEuros(self, cantidadConversion):
        self.cantidadEuros = cantidadConversion
        self.cantidadDolares = cantidadConversion * self.cambio

    def convertirDolares(self, cantidadConversion):
        self.cantidadDolares = cantidadConversion
        self.cantidadEuros = cantidadConversion / self.cambio

    def devolverConversion(self):
        print(f"Euros: {round(self.cantidadEuros, 3)}\nDolares: {round(self.cantidadDolares, 3)}")

    def devolverCantidad(self, opcion):
        if(opcion == "e"):
            return round(self.cantidadEuros, 3)
        elif(opcion == "d"):
            return round(self.cantidadDolares, 3)
        else:
            print("Conversion invalida")


print("Establecemos el cambio euro-dolar en 1.37")
objetoConvertidor = Convertidor(1.37)
print("Indicamos una cantidad impuesta de 220 euros")
objetoConvertidor.convertirEuros(220)
objetoConvertidor.devolverConversion()
print("Indicamos una cantidad impuesta de 350 dolares")
objetoConvertidor.convertirDolares(350)
objetoConvertidor.devolverConversion()
