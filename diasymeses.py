from tkinter import *

def agregaPalabras():
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    dias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")

    palabraEncontrada = False

    for elMes in meses:
        if elMes.upper() == textoIntroducido.get().upper():
            textoMeses.set(textoMeses.get() + "\r" + elMes)
            textoIntroducido.set("")
            palabraEncontrada = True
    for elDia in dias:
        if elDia.upper() == textoIntroducido.get().upper():
            textoDias.set(textoDias.get() + "\r" + elDia)
            textoIntroducido.set("")
            palabraEncontrada = True
    if not palabraEncontrada:
        textoError.set("No Reconocido")
    else:
        textoError.set("Todo bien")


ventana = Tk()
ventana.minsize(250, 250)
ventana.maxsize(500, 500)

primerPanel = Frame(ventana, background='teal')
segundoPanel = Frame(ventana, background='cyan')

primerPanel.pack(side=TOP, expand=True, fill=BOTH)
segundoPanel.pack(side=BOTTOM, expand=True, fill=BOTH)

textoError = StringVar()
textoDias = StringVar()
textoMeses = StringVar()
textoIntroducido = StringVar()

Label(primerPanel, bg='fuchsia', textvariable=textoError, font='Verdana 10 italic').pack(side=BOTTOM)
Label(segundoPanel, bg='yellow', textvariable=textoDias, font='Ebrima 10').pack(side=LEFT)
Label(segundoPanel, bg='red', textvariable=textoMeses, font='Ebrima 10').pack(side=RIGHT)

etiquetaNombre = Label(primerPanel, text="Nombre:", bg='fuchsia')
etiquetaNombre.pack(side=LEFT)

cuadroIntroduccion = Entry(primerPanel, textvariable=textoIntroducido)
cuadroIntroduccion.pack(side=LEFT)

botonIntroduccion = Button(primerPanel, text="Introducir", bg='fuchsia', relief=RIDGE, command=agregaPalabras)
botonIntroduccion.pack(side=RIGHT)

textoDias.set("DIAS:")
textoMeses.set("MESES:")
textoError.set("De momento bien")

ventana.mainloop()
