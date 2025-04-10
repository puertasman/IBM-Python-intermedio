#clase bibliteca

from _065_clase_libro import Libro

def mostrar_lista_libros(lista):
    for libro in lista:
        print(f'''Libro {libro.Id}
    Título: {libro.titulo}
    Autor: {libro.autor}
    Género: {libro.genero}''')
        

class Biblioteca:
    
    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []
        
    def agregar_libro(self, titulo, autor, genero):
        libro = Libro(titulo, autor, genero)
        self.libros.append(libro)
        
    def buscar_libros_por_autor(self, autor):
        libros_por_autor = []
        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                libros_por_autor.append(libro)
        if len(libros_por_autor) == 0:
            print(f"No hay libros de {autor}.")
        else:
            print(f"\nEstos son los libros de {autor}")
            mostrar_lista_libros(libros_por_autor)
    
    def buscar_libros_por_genero(self, genero):
        libros_por_autor = []
        for libro in self.libros:
            if libro.genero.lower() == genero.lower():
                libros_por_autor.append(libro)
        if len(libros_por_autor) == 0:
            print(f"No hay libros de {genero}.")
        else:
            print(f"\nEstos son los libros de {genero}")
            mostrar_lista_libros(libros_por_autor)
            
    def mostar_todos_los_libros(self):
        print("\nEstos son los libros de la biblioteca")
        mostrar_lista_libros(self.libros)
        
    @property
    def nombre(self):
        return self._nombre

    @property
    def libros(self):
        return self._libros