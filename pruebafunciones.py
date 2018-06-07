'''def mensaje():
    print("Estamos cerrados")


def sumador():
    return 100 + 43

mensaje()
print(sumador())'''


'''def nombrecompleto(nombre, apellido):
    return("Te llamas " + nombre + " " + apellido)

print(nombrecompleto(nombre="Ivan", apellido="Moody"))

#print(nombrecompleto("Ivan Moody"))
#print(nombrecompleto("Ivan", "Moody"))'''


def usuario(nombre, *aficiones, **datos):
    print("Te llamas " + nombre + " y tus aficiones son: ")
    texto = ""

    for aficion in aficiones:
        texto += aficion + " "
    print(texto)

    for dato in datos:
        if dato == "padre":
            print("Tu padre se llama " + datos[dato])
        elif dato == "madre":
            print("Tu madre se llama " + datos[dato])

usuario("Fabio", "Astronomia", "Deportes", "Ciencias",
     madre="Monica", padre="Gianluigi")

listadatos = ["Ivan", "cantar", "tocar guitarra", "familia"]
listadatospersonales = {"madre": "Primrose", "padre": "Aurelius"}
usuario(*listadatos, **listadatospersonales)
