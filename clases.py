class casa:
    def __init__(self, calle, numerocasa, avenida, barrio, Municipio, estrato):
        self.calle = calle
        self.numerocasa = numerocasa
        self.avenida = avenida
        self.barrio = barrio
        self.Municipio = Municipio
        self.estrato = estrato
    
    def imp(self):
        print(f"Estrato: {self.estrato}, Numero de casa: {self.numerocasa}, Avenida: {self.avenida}, Barrio: {self.barrio}, Municipio: {self.Municipio}, Calle: {self.calle}")


Casa1=  casa(15, 27, "Decima", "Betania", "LosPatios", 4)
Casa2=  casa(15, 27, "quinta", "El sol", "LosPatios", 1)

Casa1.imp()
Casa2.imp()