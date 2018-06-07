def nivel1():
    return "Este es el nivel 1"


def nivel2():
    return "Este es el nivel 2"


def nivel3():
    return "Este es el nivel 3"


def iniciar():
    num = input("Indique el nivel que necesita: ")
    if "nivel" + num in globals():
        if callable(globals()["nivel" + num]):
            print(globals()["nivel" + num]())
    else:
        print("El nivel " + str(num) + " no existe")

iniciar()
