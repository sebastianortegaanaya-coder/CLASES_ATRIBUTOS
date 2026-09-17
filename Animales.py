class animal:
    def __init__(self, nombre, especie, color):
        self.nombre = nombre
        self.especie = especie
        self.color = color

class perro(animal):
    def __init__(self, nombre, especie, color, raza):
        super().__init__(nombre, especie, color)
        self.raza = raza
    def hacersonido(self):
        print (f"Guau Guau")
    def presentarse(self):
        print (f"Soy un {self.especie}, mi nombre es {self.nombre} el {self.raza}, soy de color {self.color}")

class gato(animal):
    def __init__(self, nombre, especie, color, raza):
        super().__init__(nombre, especie, color)
        self.raza = raza
    def hacersonido(self):
        print (f"Miau Miau")
    def presentarse(self):
        print (f"Soy un {self.especie}, mi nombre es {self.nombre} el {self.raza}, soy de color {self.color}")

class pajaro(animal):
    def __init__(self, nombre, especie, color, raza):
            super().__init__(nombre, especie, color)
            self.raza = raza
    def hacersonido(self):
            print (f"pio pio")
    def presentarse(self):
            print (f"Soy un {self.especie}, mi nombre es {self.nombre} el {self.raza}, soy de color {self.color}")


perro1=perro("Rex", "perro", "marrón", "labrador")
gato1=gato("Michi", "gato", "blanco", "persa")
pajaro1=pajaro("Piolin", "pajaro", "amarillo", "canario")

perro1.presentarse()
perro1.hacersonido()   
gato1.presentarse()
gato1.hacersonido()
pajaro1.presentarse()
pajaro1.hacersonido()