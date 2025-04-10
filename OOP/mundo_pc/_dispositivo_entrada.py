# clase de dispositivo de entrada

class Dispositivo_Entrada:
    """Elementos de entrada"""
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo
class Raton(Dispositivo_Entrada):
    """Clase que hered de dispositivo de entrada"""
    contador_raton = 0
    def __init__(self):
        Raton.contador_raton += 1
        self.id = Raton.contador_raton

    def __str__(self):
        return f"Dispositivo de entrada tipo ratón con id {self.id}"
    
class Teclado(Dispositivo_Entrada):
    """Clase que hereda e dispositivo de entrada"""
    contador_teclado = 0
    def __init__(self):
        """Inicialización del elemento teclado"""
        Teclado.contador_teclado += 1
        self.id = Teclado.contador_teclado

    def __str__(self):
        return f"Dispositivo de entrada tipo teclado con id {self.id}"

class Monitor:
    """Clase que almacena el monitor del ordenador"""
    contador_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.id = Monitor.contador_monitores
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return f"El monitor {self.id}, es de la marca {self.marca} y su tamaño es de {self.tamanio} pulgadas."

if __name__ == "__main__":
    raton = Raton()
    print(raton)

    teclado = Teclado()
    print(teclado)

    monitor = Monitor('Samsung', 27)
    print(monitor)