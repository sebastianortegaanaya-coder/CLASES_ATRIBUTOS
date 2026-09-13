class carro:
    def __init__(self, color, llantas, marca, convertible, velocidad):
        self.color = color
        self.llantas = llantas
        self.marca = marca
        self.convertible = convertible
        self.velocidad = velocidad
carro1=  carro("verde", "pantaneras", "Lamborguini", False, 167)

print(carro1.color)
print(carro1.llantas)
print(carro1.marca)
print(carro1.convertible)
print(carro1.velocidad)