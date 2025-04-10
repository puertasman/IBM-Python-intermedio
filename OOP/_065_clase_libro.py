# clase libro

class Libro:
    
    contador_libros = 0
    
    def __init__(self, titulo, autor, genero):
        Libro.contador_libros += 1
        self._Id = Libro.contador_libros
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        print(f"Adquirido el libro {self.titulo}.")
    
    
    @property    
    def Id(self):
        return self._Id
    @property    
    def titulo(self):
        return self._titulo
    
    @property    
    def autor(self):
        return self._autor
    
    @property    
    def genero(self):
        return self._genero
    