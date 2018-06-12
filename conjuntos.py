Calabria = set({"Catanzaro", "Cosenza", "Crotona", "Reggio de Calabria", "Vibo Valentia"})
Campania = set({"Avellino", "Benevento", "Caserta", "Napoli", "Salerno"})
Lacio = set({"Frosinone", "Latina", "Rieti", "Roma", "Viterbo"})
Liguria = set({"Genova", "Imperia", "La Spezia", "Savona"})
Lucania = set({"Matera", "Potenza"})
Molise = set({"Campobasso", "Isernia"})
Toscana = set({"Arezzo", "Florencia", "Grosseto", "Livorno", "Lucca", "Massa-Carrara", "Pisa"})
Pistoia = set({"Prato", "Siena"})
Umbria = set({"Perusa", "Terni"})
Veneto = set({"Belluno", "Padua", "Rovigo", "Treviso", "Venecia", "Verona", "Vicenza"})
Lombardia = set({"Milan", "Monza", "Cremona", "Bergamo", "Brescia", "Pavia", "Mantua", "Sondrio", "Como", "Varese", "Lecco"})

regiones = (Calabria, "Calabria", Campania, "Campania", Lacio, "Lacio", Liguria, "Liguria", Lucania, "Lucania", Molise, "Molise", Toscana, "Toscana", Umbria, "Umbria", Veneto, "Veneto", Lombardia, "Lombardia")


def encuentraProvincia(region):
    if provincia in region:
        return True
    else:
        return False


def formarItalia(region):
    region.remove(provincia)
    print("\nSus provincias son (excepto la que ha indicado):")
    for nombre in region:
        print(nombre.ljust(20), end="")
        
    Italia = set()
    Italia.update(Calabria, Campania, Lacio, Liguria, Lucania, Molise, Toscana, Umbria, Veneto, Lombardia)
    
    ItaliaOrdenada = list(Italia)
    ItaliaOrdenada.sort()
    
    print("\n\nLas provincias de Italia en conjunto son:")
    for nombre in ItaliaOrdenada:
        print(nombre.ljust(20), end="")

provincia = input("Escriba la provincia italiana: ")
region = ""
contador = 0
                
# Vamos obteniendo cada conjunto para encuentraRegionr en su interior la
# provincia indicada, gracias a la tupla definida anteriormente
while contador < len(regiones):
    if encuentraProvincia(regiones[contador]):
        region = regiones[contador]
        nombreRegion = regiones[contador + 1]
    contador = contador + 2
                
# Si la variable region no ha cambiado su valor inicial, significa
# que no se ha encontrado la provincia indicada.
if region == "":
    print("\nLa región de " + provincia + " no se ha encontrado.")
else:
    print("\nLa región de " + provincia + " es " + nombreRegion)
    formarItalia(region)
