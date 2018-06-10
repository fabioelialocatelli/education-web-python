cadena = input("Escriba un texto: ")

if(cadena.isalnum()):
    print("Letras y numeros, sin espacios")
if(cadena.isalpha()):
    print("Letras, sin espacios")
if(cadena.isdigit()):
    print("Numeros, sin espacios")
