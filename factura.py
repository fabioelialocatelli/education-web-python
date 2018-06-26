articulo1 = input("Primer artículo: ")
precioArticulo1 = eval(input("Precio: "))

articulo2 = input("Segundo artículo: ")
precioArticulo2 = eval(input("Precio: "))

articulo3 = input("Tercer artículo: ")
precioArticulo3 = eval(input("Precio: "))

print("/n")
print("factura".upper().center(90, "-"))

print(articulo1.title().ljust(85, ".") + str(precioArticulo1).zfill(5) + "$")
print(articulo2.title().ljust(85, ".") + str(precioArticulo2).zfill(5) + "$")
print(articulo3.title().ljust(85, ".") + str(precioArticulo3).zfill(5) + "$")

print("-".center(90, "-"))

precioBase = precioArticulo1 + precioArticulo2 + precioArticulo3
impuestos = precioBase * 0.25
coste = precioBase + impuestos

textoBase = str(precioBase)
textoImpuestos = str(impuestos)
textoCoste = str(coste)

textoBase = textoBase[:textoBase.find(".") + 3] #utilizamos slice? quizas porque permite mas control?
textoImpuestos = textoImpuestos[:textoImpuestos.find(".") + 3]
textoCoste = textoCoste[:textoCoste.find(".") + 3]

print("PRECIO BASE: ".rjust(85) + textoBase.zfill(5) + "$")
print("IMPUESTOS: ".rjust(85) + textoImpuestos.zfill(5) + "$")
print("COSTE: ".rjust(85) + textoCoste.zfill(5) + "$")
