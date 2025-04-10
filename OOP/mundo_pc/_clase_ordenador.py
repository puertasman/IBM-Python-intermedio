from _dispositivo_entrada import Teclado, Raton, Monitor

class Ordenador:
    contador_ordenadores = 0

    def __init__ (self, monitor, teclado, raton):
        Ordenador.contador_ordenadores += 1
        self.id = Ordenador.contador_ordenadores
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f"""El ordenador {self.id} tiene los componentes:
    Monitor: {self.monitor}
    Teclado: {self.teclado}
    Ratón: {self.raton}"""

if __name__ == "__main__":
    monitor = Monitor("samsung", 27)
    raton = Raton("Logitech","ratón")
    teclado = Teclado("Logi","teclado")

    ordenador1 = Ordenador(monitor, teclado, raton)
    print(ordenador1)