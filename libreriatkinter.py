from tkinter import *


def calcula():
    varResultado.set(varNombre.get() + " " + varApellidos.get())

ventana = Tk()
ventana.title("Test")

varNombre = StringVar()
varApellidos = StringVar()
varResultado = StringVar()

cuadro1 = Entry(ventana, textvariable=varNombre)
cuadro2 = Entry(ventana, textvariable=varApellidos)

etiqueta1 = Label(ventana, text="Nombre: ")
etiqueta2 = Label(ventana, text="Apellido: ")
etiqueta3 = Label(ventana, textvariable=varResultado)

boton1 = Button(ventana, text="Aceptar", bg='red', command=calcula)
boton1.grid(row=2, column=0)

'''
boton2 = Button(ventana, text="Boton", relief=FLAT)
boton3 = Button(ventana, text="Boton", relief=SUNKEN)
boton4 = Button(ventana, text="Boton", relief=RIDGE)
boton5 = Button(ventana, text="Boton", relief=SOLID)
boton6 = Button(ventana, text="Boton", relief=GROOVE)
boton7 = Button(ventana, text="Boton", relief=RAISED)

boton2.grid(row=3, column=1)
boton3.grid(row=3, column=2)
boton4.grid(row=3, column=3)
boton5.grid(row=3, column=4)
boton6.grid(row=3, column=5)
boton7.grid(row=3, column=6)'''

etiqueta1.grid(row=0, column=0)
etiqueta2.grid(row=1, column=0)
etiqueta3.grid(row=2, column=1)

cuadro1.grid(row=0, column=1)
cuadro2.grid(row=1, column=1)

ventana.mainloop()
