numeros = list(range(10))
print("esta es la tabla de multiplicar del 5: ")
for numero in numeros:
    if numero + 1 == 5:
        continue
    print(("5 x " + str(numero + 1) + " = " + str(5 * (numero + 1))))
print("eso es todo")
