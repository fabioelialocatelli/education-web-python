import mysql.connector

conex = mysql.connector.connect(user="root", password="Unukalhai17#", host="localhost")
cursor = conex.cursor()
#cursor.execute("DROP SCHEMA python")

def creacion():
    cursor.execute("CREATE DATABASE python")
    cursor.execute("USE python")

    cursor.execute("CREATE TABLE usuario (" +
    "id INTEGER PRIMARY KEY UNIQUE NOT NULL, " +
    "nombre TEXT, fecha_registro DATE)")

    cursor.execute("CREATE TABLE webs (" +
    "idUsuario INTEGER, web TEXT, descripcion TEXT, " +
    "FOREIGN KEY(idUsuario) REFERENCES usuario(id))")

def insercion():

    cursor.execute("USE python")
    cursor.execute("INSERT INTO usuario (id, nombre, fecha_registro) VALUES (%s, %s, %s)", (140, "Josef Linares", "2018-06-10"))
    cursor.execute("INSERT INTO usuario (id, nombre, fecha_registro) VALUES (%s, %s, %s)", (150, "Salvador Herbert", "2018-05-10"))
    conex.commit()

    print("2 Usuarios Agregados")

    coleccion = [
                    (140, "www.python.org", "Python"),
                    (140, "www.taiga.io", "Taiga"),
                    (150, "www.marvel.com", "Marvel"),
                    (150, "www.meridian.co.nz", "Meridian Energy"),
                    (140, "www.agar.io", "Agar"),
                ]
    cursor.executemany("INSERT INTO webs (idUsuario, web, descripcion) VALUES (%s, %s, %s)", coleccion)
    conex.commit()

    print("Varias Webs Agregadas")
    

def listado():
    cursor.execute("USE python")
    cursor.execute("SELECT u.id, u.nombre, w.web, w.descripcion FROM usuario u, webs w WHERE u.id = w.idusuario")

    milista = cursor.fetchall()
    for registro in milista:
        print("Scio {0} : {1}, {2}, ({3})".format(registro[0], registro[1], registro[2], registro[3]))

#creacion()
#insercion()
listado()
