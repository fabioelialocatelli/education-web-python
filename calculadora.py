def suma(parametroA, parametroB):
    return parametroA + parametroB


def resta(parametroA, parametroB):
    return parametroA - parametroB

opcion = ""

while(opcion != "salir"):

    opcion = input("Indique la operación matemática (suma - resta) o salir: ")

    primerParametro = eval(input("Parametro A: "))
    segundoParametro = eval(input("Parametro B: "))

    if opcion == "suma":
        print("La suma es " + str(suma(primerParametro, segundoParametro)))
    elif opcion == "resta":
        print("La resta es " + str(resta(primerParametro, segundoParametro)))
    else:
        if opcion != "salir":
            print("La operacion especificada no existe")
