'''dicc = {"manzana": 0.75, "pera": 1.45, "sandia": 0.80, "lechuga": 0.50}

print("Diccionario original: ")
print(dicc)

print("Anadimos un nuevo elemento: ")
dicc["atun"] = 5.55
print(dicc)

print("Eliminamos un elemento: ")
del dicc["lechuga"]
print(dicc)

print("Las claves son: ")
print(dicc.keys())

print("Los valores son: ")
print(dicc.values())'''

def agregar():
    clave = input("Escriba el nombre: ")
    valor = input("Escriba la edad: ")
    dicc.setdefault(clave, valor)

def eliminar():
    clave = input("Escriba el nombre a eliminar: ")
    print("Eliminando " + clave + "... " + dicc.pop(clave, "No encontrado"))

def listar():
    print("Contenido del diccionario: ")
    print(dicc)
    print("nombres".ljust(15) + "edades".rjust(5))
    for clave in dicc.items():
        print(clave[0].ljust(15) + clave[1].rjust(5))

dicc = dict()
opcion = -1

while opcion != 0:
    
    print("\nMENU DE OPCIONES: ")
    print("1 - Agregar Elementos")
    print("2 - Eliminar Elementos")
    print("3 - Listar Contenido")
    print("0 - Salir")
    
    opcion = eval(input("Escriba Opcion: "))
    if opcion == 1:
        agregar()
    if opcion == 2:
        eliminar()
    if opcion == 3:
        listar()
        
print("Hasta la proxima vez")
