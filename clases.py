class casa:
    def __init__(self, calle, numerocasa, avenida, barrio, Municipio, estrato):
        self.calle = calle
        self.numerocasa = numerocasa
        self.avenida = avenida
        self.barrio = barrio
        self.Municipio = Municipio
        self.estrato = estrato
Casa1=  casa(15, 27, "Decima", "Betania", "LosPatios", 4)

print(Casa1.estrato)
print(Casa1.avenida)
print(Casa1.barrio)
print(Casa1.calle)
print(Casa1.Municipio)
print(Casa1.numerocasa)