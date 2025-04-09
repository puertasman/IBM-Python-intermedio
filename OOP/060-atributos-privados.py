# atributos privados

class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca # atributo público
        self._modelo = modelo # atributo protegido
        self._color = color # atributo privado
    
    def conducir(self):
        print(f"Conduciendo el coche {self._marca} {self._modelo} de color {self._color}")

    def get_marca(self):
        return self.marca
    
    def set_marca(self, marca):
        self.marca = marca

if __name__ == "__main__":

    coche1 = Coche("Chevrolet", "Corvete", "Rojo")
    coche1.marca = 'Toyota'
    coche1._modelo = 'Yaris' # no es buena práctica
    coche1.__color = "verde" # mala práctica
    coche1.conducir()
    coche1.get_marca()
    coche1.set_marca('BMW')
    coche1.conducir()