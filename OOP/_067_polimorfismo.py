"""Ejemplo de polimorfismo"""

class Animal:
    """Clase con sonido"""
    def hacer_sonido(self):
        """suena"""
        print("Hago un pitido...")

class Perro(Animal):
    """Clase Perro subclase de Animal"""
    def hacer_sonido(self):
        """Sobreescribe el método"""
        print("Puedo ladrar")

class Gato(Animal):
    """Clase Gato subclase de Animal"""
    def hacer_sonido(self):
        """Sobreescribe el método"""
        print("Puedo maullar")

print("Ejemplo de polimorfismo")
print("Clase padre: Animal")
animal1 = Animal()
animal1.hacer_sonido()

print("Clase hija: Perro")
animal2 = Perro()
animal2.hacer_sonido()

print("Clase hija: Gato")
animal3 = Gato()
animal3.hacer_sonido()
