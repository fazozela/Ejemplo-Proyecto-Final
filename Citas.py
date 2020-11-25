class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola soy {self.nombre}")

class Doctor(Persona):
    def saludoDoctor(self, especialidad):
        print(f"Hola soy {self.nombre}, voy a ser tu doctor de cabecera, y mi especialidad es {especialidad}")

especialidades = "Cardiologia, Pediatria, Ginecolog[ia"

print("BIENVENIDOS AL HOSPITAL TECBA")

print("""
********************************

1. Reservar cita
2. Ver especialidades
3. Salir

********************************
""")

dato_usuario = input("Ingrese su elección: ")

if dato_usuario == "1":
    print("""
    Con quien quiere una cita?
    
    1. Doctor
    2. Enfermería
    3. Administrativo
    4. Salir
    """)
    dato_cita = input("Con quien quiere la cita: ")
    if(dato_cita == "1"):
        diego = Doctor("Diego")
        diego.saludoDoctor("Cardiologo")


elif dato_usuario == "2":
    print(especialidades)

elif dato_usuario == "3":
    print("Gracias por su visita")