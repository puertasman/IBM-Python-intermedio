class Persona:
    
    _contador = 0
    
    def __init__(self, nombre, apellido):
        Persona._contador += 1
        self.id = Persona._contador
        self.nombre = nombre
        self.apellido = apellido
        
    def __str__(self):
        return f"Persona[{self.id}]: {self.nombre} {self.apellido}"
    
    @staticmethod
    def get_contador_persona_estatico():
        print("Método estático")
        return Persona._contador
    
    @classmethod
    def get_contador_persona_clase(cls): # indica que es clase
        print(f"Método de clase")
        return cls._contador
        
persona1 = Persona("Gerardo", "Perez")
persona2 = Persona("Daniel", "Sanchez")

print(persona1)
print(persona2)

print(f"Contador de objetos Persona: {Persona._contador}")
print(f"Contador de objetos Persona (static): {Persona.get_contador_persona_estatico()}")
print(f"Contador de objetos Persona (método de clase): {Persona.get_contador_persona_clase()}")