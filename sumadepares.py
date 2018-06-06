contador = 0
sumapares = 0

while contador <= 100:
    contador += 1
    if contador % 2 == 0:
        sumapares += contador
print("La suma es " + str(sumapares))
