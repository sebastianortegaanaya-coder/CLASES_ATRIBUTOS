class ropa:
    def __init__(self, textura, talla, prenda, color, marca):
        self.textura = textura
        self.talla = talla
        self.prenda = prenda
        self.color = color
        self.marca = marca
ropa1=  ropa("algodon", "M", "camiseta", "Gris", "Koaj")

print(ropa1.textura)
print(ropa1.talla)
print(ropa1.prenda)
print(ropa1.color)
print(ropa1.marca)