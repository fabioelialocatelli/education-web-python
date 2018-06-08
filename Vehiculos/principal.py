# -*- coding: utf-8 -*-
from tierra.moto import tienemotor

import tierra.bicicleta as bici
import mar.petrolero as barco
import aire.parapente
import aire.helicoptero

print("Bicicleta; cuantas ruedas? " + str(bici.ruedas()))
print("Moto; tiene motor? " + tienemotor)
print("Petrolero; que tipos hay? " + str(barco.tipos()))
print("Parapente; como despega? " + aire.parapente.despegue())
print("Helicoptero; como despega? " + aire.helicoptero.despegue())
