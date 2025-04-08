# clase persona

class Persona:
    # nombre y apellido
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrar_persona(self):
        print(f"Nombre: {self.nombre}\nApellidos: {self.apellido}")

p1 = Persona('Enrique', 'Puertas')

p1.mostrar_persona()