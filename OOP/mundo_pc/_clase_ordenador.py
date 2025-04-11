""" Módulo clase ordenadores """
from _dispositivo_entrada import Teclado, Raton, Monitor

class Ordenador:
    """ clase ordenador """
    contador_ordenadores = 0

    def __init__ (self, nombre, monitor, teclado, raton):
        Ordenador.contador_ordenadores += 1
        self.id = Ordenador.contador_ordenadores
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f"""El ordenador {self.nombre} tiene Id {self.id} y los componentes:
    Monitor: {self.monitor}
    Teclado: {self.teclado}
    Ratón: {self.raton}"""

if __name__ == "__main__":
    monitor1 = Monitor("samsung", 27)
    raton1 = Raton("Logitech","ratón")
    teclado1 = Teclado("Logi","teclado")

    ordenador1 = Ordenador('HP 533', monitor1, teclado1, raton1)
    print(ordenador1)

    teclado2 = Teclado("Gamer", 'Bluetooth')
    raton2 = Raton("Gamer","Bluetooth")
    monitor2 = Monitor("Gamer",34)
    ordenador2 = Ordenador("Gamer", monitor2, teclado2, raton2)
    print(ordenador2)
