# se crean por encima del __init__

class Persona:
    
    atributo_clase = 0
    
    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia
        
if __name__ == "__main__":
    print("Atributos de clase")
    print(f"Atributo de clase {Persona.atributo_clase}")
    
    Persona.atributo_clase = 10
    print(f"Atributo de clase {Persona.atributo_clase}")
    
    persona1 = Persona(15)
    print(f"Atributo de clase desde persona1 :{persona1.atributo_clase}")
    print(f"Atributo de instancia desde persona1: {persona1.atributo_instancia}")
    
    persona2 = Persona(30)
    print(f"Atributo de clase desde persona2 :{persona2.atributo_clase}")
    print(f"Atributo de instancia desde persona2: {persona2.atributo_instancia}")