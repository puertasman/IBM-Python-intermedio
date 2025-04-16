""" clase servicio película, añade, borra y lista """

from pathlib import Path
from os import remove

class Servicio:
    """ La clase que almacena las películas según el servicio correspondiente """

    def __init__(self, nombre):
        """ Servicio de películas """
        self.nombre_archivo = Path(__file__).parent / 'peliculas.txt'
        self.nombre = nombre

    def listar_peliculas(self):
        """ Muestra las películas del servicio """
        peliculas = []
        try:
            with open (self.nombre_archivo, 'r', encoding = 'UTF-8') as archivo:
                for line in archivo:
                    peliculas.append(line.strip())
            print(f"--- Películas en {self.nombre} ---")
            print("=" * 30)
            if len(peliculas) == 0:
                print("No hay películas")
            else:
                print(f"Hay {len(peliculas)} películas en el catálogo.")
                for pelicula in peliculas:
                    print(pelicula)
        except FileNotFoundError:
            print("No hay archivo de listado de películas")

    def add_pelicula(self, nombre):
        """ Añadir una película solo con el título """
        with open (self.nombre_archivo, 'a', encoding = 'UTF-8') as archivo:
            archivo.write(f'{nombre}\n')

    def del_pelicula(self):
        """ Eliminar la lista de películas"""
        try:
            remove(self.nombre_archivo)
        except FileNotFoundError:
            print("No hay archivo de listado de películas que poder borrar.")

if __name__ == '__main__':

    servicio = Servicio('Netflix')
    servicio.listar_peliculas()

    servicio.del_pelicula()

    servicio.add_pelicula('la última vuelta')
    servicio.listar_peliculas()
