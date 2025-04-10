# clase persona para sobreescribir métodos

class Persona(object): # no hace falta poner object porque es por defecto
    """Clase para sobreescribir""" 
    def __init__(self, nombre, apellido): #sobreescribe init de object
        """Crea un objeto de la clase Persona"""
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        """Sobreescribe el print que se hace del objeto
        si no se sobreescribe devuelve la dirección en memoria"""
        return f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Dirección de memoria: {super.__str__(self)}'''

p1 = Persona('Ana','Martínez')
print(p1)  # print(p1.__str__())
