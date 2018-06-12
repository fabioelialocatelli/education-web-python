tabla = ("Aluminio", "Al", "Azufre", "S", "Bismuto", "Bi",
"Cloro", "Cl", "Mercurio", "Hg", "Bromo", "Br", "Yodo", "I")

#Personalmente utilizaria un diccionario para este ejercicio

def findElement(nombre):
    if tabla.count(nombre) == 0:
        print("Elemento no encontrado en la tabla.")
    else:

        #Intente con modulos pero esta solucion es mas facil
        if tabla.index(nombre) / 2 != tabla.index(nombre) // 2:
             
            print("Elemento no encontrado en la tabla.")
        else:
            print((nombre.ljust(15, ".") +
            tabla[tabla.index(nombre) + 1].rjust(10, ".")))


def findSymbol(simbolo):
    if tabla.count(simbolo) == 0:
        print("Simbolo no encontrado en la tabla.")
    else:        
        
        if tabla.index(simbolo) / 2 == tabla.index(simbolo) // 2:
            
            print("Simbolo no encontrado en la tabla.")
        else:
            print((simbolo.ljust(15, ".") +
            tabla[tabla.index(simbolo) - 1].rjust(10, ".")))

opcion = -1
while opcion != 0:
    print("\nTABLA PERIODICA - MENU DE OPCIONES:")
    print("1 - Buscar por elemento")
    print("2 - Buscar por simbolo")
    print("0 - Salir")
    opcion = eval(input("Escriba opcion: "))
    if opcion == 1:
        elemento = input("Escribe el nombre del elemento quimico: ")
        findElement(elemento)
    if opcion == 2:
        simbolo = input("Escribe el simbolo del elemento quimico: ")
        findSymbol(simbolo)
print("Hasta la proxima vez")
