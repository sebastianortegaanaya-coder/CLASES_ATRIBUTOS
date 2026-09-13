class estudiante:
    def __init__(self, nombre, documento, sexo, carrera, codigo):
        self.nombre = nombre
        self.documento = documento
        self.sexo = sexo
        self.carrera = carrera
        self.codigo = codigo
estudiante1=  estudiante("Diego", 6742069, "masculino", "mecatronica", 67)

print(estudiante1.nombre)
print(estudiante1.documento)
print(estudiante1.sexo)
print(estudiante1.carrera)
print(estudiante1.codigo)