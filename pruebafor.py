marisqueria = ["centollo", "mejillon", "almeja", "navaja", "bogavante"]
for marisco in marisqueria:
    if marisco == "centollo":
        marisco = "cangrejo"
    print(marisco)
print("esa es toda la marisqueria")

numeros = list(range(10))
print("esta es la tabla de multiplicar del 5: ")
for numero in numeros:
    print(("5 x " + str(numero + 1) + " = " + str(5 * (numero + 1))))
print("eso es todo")
