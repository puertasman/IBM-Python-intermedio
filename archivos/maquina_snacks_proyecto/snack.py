""" clase snack"""

class Snack:
    """ Clase snacks para añadir aperitivos """
    contador_snacks = 0

    def __init__(self, nombre = '', precio = 0.0):
        Snack.contador_snacks += 1
        self.id_snack = Snack.contador_snacks
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Snack ID: {self.id_snack}, nombre: {self.nombre}, precio = {self.precio} €"

    def escribir_snack(self):
        """ función sacar información del snack """
        return f"{self.id_snack},{self.nombre},{self.precio}"

if __name__ == "__main__":
    snack = Snack('caramelo', 2.11)
    print(snack)
    print(snack.escribir_snack())
