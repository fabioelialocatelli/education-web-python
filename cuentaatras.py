def contarAtras(numero):
    if numero == 0:
        print("Finalizado")
    else:
        print(numero)
        contarAtras(numero - 1)

contarAtras(13)
