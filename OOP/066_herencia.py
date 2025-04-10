"""Programa para probar la herencia"""

class Animal:
    """Clase que representa un animal"""

    def comer(self):
        """Habilidad del animal para comer"""
        print("Mucha veces al día.")

    def dormir(self):
        """Habilidad del animal para dormir"""
        print("Duerme muchas horas.")

class Perro(Animal):
    """Perro sublcase de Animal"""
    def hacer_sonido(self):
        """sonido de la clase perro"""
        print("Bup bup")

    def dormir(self): # se llama igual para poder sobreescribir
        print("Este perro duerme como un perro")

class Gato(Animal):
    """Gato sublcase de Animal"""
    def hacer_sonido(self):
        """sonido de la clase gato"""
        print("Miau miau")

animales = []
perro = Perro()
animales.append(perro)
gato = Gato()
animales.append(gato)
animal = Animal()
animales.append(animal)

for animal in animales:
    print(type(animal).__name__)
    animal.comer()
    animal.dormir()
    if type(animal).__name__ != 'Animal':
        animal.hacer_sonido()
