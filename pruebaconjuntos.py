conjunto = "sandia", "manzana", "melon", "papaya", "pera", "pasas"
frutas = set(conjunto)

desayuno = set({"trigo", "leche", "pasas", "manzana", "nueces"})

frutas.add("banana")
frutas.add("melocoton")
frutas.remove("melon")

print("\nContenido actual frutas: ")
for comida in frutas:
    print(comida.ljust(15), end="")

print("\nContenido actual desayuno: ")
for comida in desayuno:
    print(comida.ljust(15), end="")

print("\nUnion conjuntos: ")

for comida in desayuno | frutas:
    print(comida.ljust(15), end="")

print("\nInterseccion conjuntos: ")

for comida in desayuno.intersection(frutas):
    print(comida.ljust(15), end="")

print("\nDiferencia conjuntos (elementos que no estan en frutas): ")

for comida in desayuno.difference(frutas):
    print(comida.ljust(15), end="")

print("\nDiferencia conjuntos (elementos que no estan en ambos): ")

for comida in desayuno.symmetric_difference(frutas):
    print(comida.ljust(15), end="")
