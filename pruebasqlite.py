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

creacion()
cursor.close()
