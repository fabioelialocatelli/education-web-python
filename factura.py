articulo1 = input("Primer artículo: ")
precioArticulo1 = eval(input("Precio: "))
articulo2 = input("Segundo artículo: ")
precioArticulo2 = eval(input("Precio: "))
articulo3 = input("Tercer artículo: ")
precioArticulo3 = eval(input("Precio: "))

print("/n")
print("factura".upper().center(90, "-"))

print(articulo1.title().ljust(40, ".") + str(precioArticulo1).zfill(5) + "€")
print(articulo2.title().ljust(40, ".") + str(precioArticulo2).zfill(5) + "€")
print(articulo3.title().ljust(40, ".") + str(precioArticulo3).zfill(5) + "€")

print("-".center(90, "-"))

base = precioArticulo1 + precioArticulo2 + precioArticulo3
iva = base * 0.21
total = base + iva

txtbase = str(base)
txtbase = txtbase[:txtbase.find(".") + 3]

txtiva = str(iva)
txtiva = txtiva[:txtiva.find(".") + 3]

txttotal = str(total)
txttotal = txttotal[:txttotal.find(".") + 3]

print("Precio base: ".rjust(40) + txtbase.zfill(5) + "€")
print("IVA: ".rjust(40) + txtiva.zfill(5) + "€")
print("TOTAL A PAGAR: ".rjust(40) + txttotal.zfill(5) + "€")
