nombres = []
nuevo = ""

while nuevo.upper() != "FIN":
    nuevo = input("Escribe un nombre (FIN para acabar): ")
    if nuevo.upper() != "FIN":
        veces = nombres.count(nuevo)
        if veces == 0:
            nombres.append(nuevo)
nombres.sort()
print("Lista ordenada: ")
for nombre in nombres:
    print(nombre.ljust(15), end="")
