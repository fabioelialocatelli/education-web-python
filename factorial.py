def factorial(numero=10):
    if numero > 1:
        return numero * factorial(numero - 1)
    elif numero == 1:
        return 1

print(("El factorial de 43 es " + str(factorial(43))))
print(("El factorial de 31 es " + str(factorial(31))))
print(("El factorial del valor por defecto (10) es " + str(factorial())))
