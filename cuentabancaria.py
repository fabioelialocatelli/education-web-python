from convertidor import Convertidor

class Cuenta(Convertidor):
    def __init__(self, numeroIndicado, monedaIndicada, cambioIndicado, cantidadIndicada):
        super(Cuenta, self).__init__(cambioIndicado)
        self.cuentaNumero = numeroIndicado
        self.moneda = monedaIndicada
        self.cantidadEuros = cantidadIndicada

    def monedaActual(self, monedaIndicada):
        if(monedaIndicada == "e"):
            self.moneda = "e"
        elif(monedaIndicada == "d"):
            self.moneda = "d"
        else:
            raise TypeError("Moneda Desconocida")

    def Ingresar(self, cantidadIndicada):
        if(self.moneda == "e"):
            self.cantidadEuros = self.devolverCantidad("e") + cantidadIndicada
        elif(self.moneda == "d"):
            self.cantidadDolares = self.devolverCantidad("d") + cantidadIndicada
        else:
            raise TypeError("Falta indicar la moneda!")

    def Retirar(self, cantidadIndicada):
        if(self.moneda == "e"):
            self.cantidadEuros = self.devolverCantidad("e") - cantidadIndicada
        elif(self.moneda == "d"):
            self.cantidadDolares = self.devolverCantidad("d") - cantidadIndicada
        else:
            raise TypeError("Falta indicar la moneda!")

print("Establecemos una cuenta bancaria con cambio a 1.38 y en euros")
objetoCuenta = Cuenta("125000456", "e", 1.38, 0)
print("Ingresamos 250.5 euros y mostramos el saldo en ambas monedas")
objetoCuenta.Ingresar(250.5)
print((" - Cantidad en euros: " + str(objetoCuenta.devolverCantidad("e"))))
print((" - Cantidad en dolares: " + str(objetoCuenta.devolverCantidad("d"))))
print("Ingresamos 125.75 euros y mostramos el saldo en ambas monedas")
objetoCuenta.Ingresar(125.75)
print((" - Cantidad en euros: " + str(objetoCuenta.devolverCantidad("e"))))
print((" - Cantidad en dolares: " + str(objetoCuenta.devolverCantidad("d"))))
print("Cambiamos la moneda actual a dólares")
objetoCuenta.monedaActual("d")
print("Retiramos 20 dólares y mostramos el saldo en ambas monedas")
objetoCuenta.Retirar(20)
print((" - Cantidad en euros: " + str(objetoCuenta.devolverCantidad("e"))))
print((" - Cantidad en dolares: " + str(objetoCuenta.devolverCantidad("d"))))
