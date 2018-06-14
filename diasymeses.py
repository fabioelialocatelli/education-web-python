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
        descripcionError.set("No Reconocido")
    else:
        descripcionError.set("Todo bien")


ventana = Tk()
ventana.minsize(250, 250)
ventana.maxsize(500, 500)

primerPanel = Frame(ventana, background='teal', width=125, height=8)
primerPanel.pack(side=TOP, expand=True, fill=BOTH)

descripcionError = StringVar()
Label(primerPanel, bg='fuchsia', textvariable=descripcionError).pack(side=BOTTOM)

etiquetaNombre = Label(primerPanel, text="NOMBRE:", bg='fuchsia')
etiquetaNombre.pack(side=LEFT)
textoIntroducido = StringVar()
cuadroIntroduccion = Entry(primerPanel, textvariable=textoIntroducido)
cuadroIntroduccion.pack(side=LEFT)
botonIntroduccion = Button(primerPanel, text="Introducir", bg='fuchsia', relief=RIDGE, command=agregaPalabras)
botonIntroduccion.pack(side=RIGHT)

segundoPanel = Frame(ventana, background='gray', width=30, height=10)
segundoPanel.pack(side=BOTTOM, expand=True, fill=X)
textoDias = StringVar()
textoDias.set("DIAS:")
Label(segundoPanel, text="DIAS:", bg='yellow', textvariable=textoDias).pack(side=LEFT)
textoMeses = StringVar()
textoMeses.set("MESES:")
Label(segundoPanel, bg='red', textvariable=textoMeses).pack(side=RIGHT)

ventana.mainloop()
