from string import Template

plantilla = Template("La ciudad de $ciudad aporta $$$cantidad al proyecto ${proyecto}landia.")

ciudad1 = plantilla.substitute(ciudad = "Wellington", cantidad = "150000", proyecto = "Uburu")
ciudad2 = plantilla.substitute(ciudad = "Barcelona", cantidad = "300000", proyecto = "Cepi")

print(ciudad1)
print(ciudad2)

plantilladev = Template("Devolver $articulo a $origen")

devolver1 = plantilladev.safe_substitute(articulo = "Exprimidor Philips", origen = "Fnac")
devolver2 = plantilladev.safe_substitute(articulo = "Cafetera Bialetti", origen = "Corte Ingles")

print(devolver1)
print(devolver2)
