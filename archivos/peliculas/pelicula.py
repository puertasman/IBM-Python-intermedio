""" Clase película """

class Pelicula:
    """ Clase película, sólo guarda el nombre """

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"

if __name__ == "__main__":
    pelicula = Pelicula("Lo que el viento se llevó")
    print(pelicula)
