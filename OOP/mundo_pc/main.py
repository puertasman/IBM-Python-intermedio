""" Ejercicio ordenadores """

from _clase_ordenador import Ordenador
from _dispositivo_entrada import Teclado, Raton, Monitor

class Orden:
    """definición clase orden"""
    contador_ordenes = 0

    def __init__(self, ordenadores):
        """inicialización del objeto"""
        Orden.contador_ordenes += 1
        self.id = Orden.contador_ordenes
        # Lista de ordenadores
        self.ordenadores = ordenadores
        # se puede pasar la lista vacía y luego añadir los ordenadores o pasarla entera
        # también puede tener alguno y después poner más

    def agregar_ordenador(self, ordenador):
        """método para añadir ordenadores al encargo"""
        self.ordenadores.append(ordenador)

    def __str__(self):
        """muestra el encargo"""
        if len(self.ordenadores) > 0:
            ordenadores_str = 'Listado de ordenadores del encargo:'
            for ordenador in self.ordenadores:
                ordenadores_str += "\n" + ordenador.__str__()

        else:
            ordenadores_str = "El encargo está vacía."
        return ordenadores_str

teclado1 = Teclado('HP','USB')
raton1 = Raton('HP','USB')
monitor1 = Monitor('HP',17)
ordenador1 = Ordenador('HP',monitor1, teclado1, raton1)

teclado2 = Teclado('Gamer','Bluetooth')
raton2 = Raton('Gamer','Bluetooth')
monitor2 = Monitor('Gamer','34')
ordenador2 = Ordenador('Gamer',monitor2, teclado2, raton2)

ordenador3 = Ordenador('Automontado',monitor1, teclado2, raton1)

ordenadores1 = [ordenador1, ordenador2,ordenador3]

orden1 = Orden(ordenadores1)

print(orden1)


teclado3 = Teclado('Dell', 'Bluetooth')
raton3 = Raton('Dell', 'Bluetooth')
monitor3 = Monitor('Dell', 24)
ordenador4 = Ordenador('Dell',monitor3, teclado3, raton3)

orden1.ordenadores.append(ordenador4)
print(orden1)
