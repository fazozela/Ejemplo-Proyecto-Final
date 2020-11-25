class Animal:

    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color

    def saludar(self):
        return f"Hola soy un {self.tipo} y soy de color {self.color}"


class Insecto(Animal):

    def accionInsecto(self, accion):
        return f"Hola soy un {self.tipo}, soy de color {self.color} y tambien puedo {accion}"


cucaracha = Insecto("Insecto", "Rojo")
print(cucaracha.accionInsecto("volar"))

perro = Animal("mamifero", "cafe")
print(perro.saludar())
