class comida:
    def __init__(self, color, sabor, consistencia, precio, descripcion, nombre):
        self.color = color
        self.sabor = sabor
        self.consistencia = consistencia
        self.precio = precio
        self.descripcion = descripcion
        self.nombre = nombre
comida1=  comida("rojo", "dulce", "dura", 2000, "dulcedefresa", "fresaachocolatada")

print(comida1.color)
print(comida1.sabor)
print(comida1.consistencia)
print(comida1.precio)
print(comida1.descripcion)
print(comida1.nombre)