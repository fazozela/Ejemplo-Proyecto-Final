class Persona:
    pass
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola soy {self.nombre} y tengo {self.edad}"


class Doctor (Persona):
    pass

    def saludar(self, especialidad):
        return f"Hola! soy {self.nombre}, tengo {self.edad} y me especializo en {especialidad}"

juan = Persona("Juan", 26)
print(juan.nombre)
print(juan.edad)
print(juan.saludar())

bernardo = Doctor("Bernardo", 40)
print(bernardo.saludar('Cardiología'))

