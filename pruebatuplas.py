estrellas = "navi", "sephdar", "capella", "dalim"


def imprime():
    contador = 0
    while contador < len(estrellas):
        print(estrellas[contador].ljust(10))
        contador += 1

print("Tupla original: ")
imprime()

estrellasAlteradas = list(estrellas)
estrellasAlteradas.append("antares")
estrellasAlteradas.sort()

print("Tupla alterada: ")
for estrella in estrellasAlteradas:
    print(estrella.title())

