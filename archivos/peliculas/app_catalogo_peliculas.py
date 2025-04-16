""" App catálogo películas """

from servicio_pelicula import Servicio

class Catalogo:
    """ Catálogo de películas por aplicación, se puede modificar """
    def __init__(self, nombre):
        self.servicio_pelicula = Servicio(nombre)
        self.nombre = nombre

    def catalogo(self):
        """ Función que controla el programa """
        salir = False
        print("\n*** Catálogo de películas ***")
        while not salir:
            opcion = self.mostrar_menu()
            salir = self.ejecutar_opcion(opcion)

    def mostrar_menu(self):
        """ Sólo lista las opciones para poder elegir"""
        print("""
      1. Agregar película
      2. Eliminar catálogo película
      3. Listar películas
      4. Salir""")
        try:
            return int(input("Elige una opción (1-4): "))
        except ValueError:
            print("Introduce un número del 1 al 4.")
            return 0

    def ejecutar_opcion(self, opcion):
        """ Menú """
        if opcion == 1:
            self.agregar_pelicula()
        elif opcion == 2:
            self.del_pelicula()
        elif opcion == 3:
            self.listar_peliculas()
        elif opcion == 4:
            print("Hasta pronto.")
            return True
        else:
            print("Opción no válida.")
            return False

    def agregar_pelicula(self):
        """ Añade una película a la lista de películas """
        nombre = input("Título de la película: ")
        self.servicio_pelicula.add_pelicula(nombre)
        print(f"Película {nombre} agregada correctamente.")

    def del_pelicula(self):
        """ Eliminar archivo película por ID """
        self.servicio_pelicula.del_pelicula()

    def listar_peliculas(self):
        """ Listar las películas directamente de servicio """
        print("Tocaría listar las películas")
        self.servicio_pelicula.listar_peliculas()

if __name__ == "__main__":
    catalogo = Catalogo('Catalogo 1')
    catalogo.catalogo()
