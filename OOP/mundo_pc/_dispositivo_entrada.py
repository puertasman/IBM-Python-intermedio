# clase de dispositivo de entrada

class Dispositivo_Entrada:
    """Elementos de entrada"""
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo
class Raton(Dispositivo_Entrada):
    """Clase que hered de dispositivo de entrada"""
    contador_raton = 0
    def __init__(self, marca, tipo):
        Raton.contador_raton += 1
        self.id = Raton.contador_raton
        super().__init__(marca, tipo)

    def __str__(self):
        return f"Ratón de entrada tipo {self.tipo} con id {self.id}, de marca {self.marca}"
    
class Teclado(Dispositivo_Entrada):
    """Clase que hereda e dispositivo de entrada"""
    contador_teclado = 0
    def __init__(self, marca, tipo):
        """Inicialización del elemento teclado"""
        Teclado.contador_teclado += 1
        self.id = Teclado.contador_teclado
        super().__init__(marca, tipo)

    def __str__(self):
        return f"Teclado de entrada tipo {self.tipo} con id {self.id}, de marca {self.marca}"

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
    raton = Raton('Logitech', 'USB')
    print(raton)

    raton2 = Raton('HP','bluetooth')
    print(raton2)

    teclado = Teclado('logi', 'USB')
    print(teclado)

    teclado2 = Teclado('Dell','USB')
    print(teclado2)
    
    monitor = Monitor('Samsung', 27)
    print(monitor)