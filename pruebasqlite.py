import sqlite3

conex = sqlite3.connect('productos.db')
cursor = conex.cursor()

def creacion():
    cursor.execute("CREATE TABLE listado (" +
    "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, " +
    "nombre TEXT NOT NULL, " +
    "proveedor TEXT NOT NULL," +
    "precio REAL, " +
    "stock INTEGER DEFAULT 0)")

def insercion():
    nombre = input("Nombre Producto: ")
    proveedor = input("Proveedor: ")
    precio = input("Precio: ")

    cursor.execute("INSERT INTO listado (nombre, proveedor, precio) " + "VALUES (?, ?, ?)", (nombre, proveedor, precio))
    conex.commit()

def listado():
    cursor.execute("SELECT * FROM listado")
    milista = cursor.fetchall()
    print("Listado General\n")
    for registro in milista:
        print("{0} : {1}, de {2}, precio {3}$".format(registro[0], registro[1], registro[2], registro[3]))

def id():
    ID = input("Numero Identificacion: ")
    cursor.execute("SELECT * FROM listado WHERE id=?", ID)
    registro = cursor.fetchone()

    if(registro is None):
        print("Numero no localizado")
    else:
        print("{0} : {1}, de {2}, precio {3}$".format(registro[0], registro[1], registro[2], registro[3]))

def insertarMultiple():
    productos = [
        ("All Bran", "Kelloggs", "6.85"),
        ("Protein Hit", "Tararua Dairy", "3.25"),
        ("Sourdough Bread", "Lewis Road Bakery", "5.65")
    ]

    cursor.executemany("INSERT INTO listado (nombre, proveedor, precio) " + "VALUES (?, ?, ?)", productos)
    conex.commit()

def actualizaStock():
    cursor.execute("SELECT nombre FROM listado")
    listanombres = cursor.fetchall()

    for nombre in listanombres:
        cantidad = input("Stock de " + str(nombre[0]) + " (-1 para salir): ")
        if cantidad == "-1":
            break
        else:
            cursor.execute("UPDATE listado SET stock = ? WHERE nombre = ?", (eval(cantidad), nombre[0]))
    conex.commit()
    print("Actualizacion Finalizada")

def transaccion():
    print("Actualizamos todos los precios a 1.99\n")
    conex.execute("UPDATE listado SET precio = 1.99")
    listado()
    print("\nDeshacemos la transaccion\n")
    conex.rollback()
    listado()

#creacion()
#insercion()
#listado()
#id()
#insertarMultiple()
#actualizaStock()
transaccion()
cursor.close()
