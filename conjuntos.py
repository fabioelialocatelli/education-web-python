Umbria = set({"Perusa", "Terni"})
Molise = set({"Campobasso", "Isernia"})
Basilicata = set({"Matera", "Potenza"})
Liguria = set({"Genova", "Imperia", "La Spezia", "Savona"})
Lacio = set({"Frosinone", "Latina", "Rieti", "Roma", "Viterbo"})
Campania = set({"Avellino", "Benevento", "Caserta", "Napoli", "Salerno"})
Veneto = set({"Belluno", "Padua", "Rovigo", "Treviso", "Venecia", "Verona", "Vicenza"})
Calabria = set({"Catanzaro", "Cosenza", "Crotona", "Reggio de Calabria", "Vibo Valentia"})
Toscana = set({"Arezzo", "Florencia", "Grosseto", "Livorno", "Lucca", "Massa-Carrara", "Pisa", "Pistoia"})
Lombardia = set({"Milan", "Monza", "Cremona", "Bergamo", "Brescia", "Pavia", "Mantua", "Sondrio", "Como", "Varese", "Lecco"})

regiones = (Calabria, "Calabria", Campania, "Campania", Lacio, "Lacio", Liguria, "Liguria", Basilicata, "Basilicata", Molise, "Molise", Toscana, "Toscana", Umbria, "Umbria", Veneto, "Veneto", Lombardia, "Lombardia")

def encuentraProvincia(region):
    if(provinciaIndicada in region):
        return True
    elif(provinciaIndicada not in region):
        return False

def formarItalia(region):
    region.remove(provinciaIndicada)

    provinciasOrdenadas = []
    for nombre in region:
        provinciasOrdenadas.append(nombre)
        provinciasOrdenadas.sort()

    print("\nSus provincias son (excepto la que ha indicado):")
    for provincia in provinciasOrdenadas:
        print("• " + provincia + "\n")
        
    Italia = set()
    Italia.update(Calabria, Campania, Lacio, Liguria, Basilicata, Molise, Toscana, Umbria, Veneto, Lombardia)
    
    ItaliaOrdenada = list(Italia)
    ItaliaOrdenada.sort()
    
    print("\n\nLas provincias de Italia en conjunto son:")
    for nombre in ItaliaOrdenada:
        print("• " + nombre + "\n")


provinciaIndicada = input("Escriba la provincia italiana: ").title()
region = ""
contador = 0
                
while(contador < len(regiones)):
    if(encuentraProvincia(regiones[contador])):
        region = regiones[contador]
        nombreRegion = regiones[contador + 1]
    contador = contador + 2
                
if(region == ""):
    print("\nLa region de " + provinciaIndicada + " no se ha encontrado.")
else:
    print("\nLa region de " + provinciaIndicada + " es " + nombreRegion)
    formarItalia(region)
