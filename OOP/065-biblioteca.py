# Mi biblioteca

from _065_clase_biblioteca import Biblioteca

mi_biblioteca = Biblioteca("Biblioteca Pública de Cabrils")

mi_biblioteca.agregar_libro('El alquimista','Paulo Coelho','Ficción')
mi_biblioteca.agregar_libro('1984','George Orwell','Ficción')
mi_biblioteca.agregar_libro('El Código Da Vinci','Dan Brown','Misterio')
mi_biblioteca.agregar_libro('Rayuela', 'Julio Cortázar', 'Novela')
mi_biblioteca.agregar_libro('Verónica decide morir','Paulo Coelho','Ficción')

mi_biblioteca.mostar_todos_los_libros()

mi_biblioteca.buscar_libros_por_autor("Paulo Coelho")

mi_biblioteca.buscar_libros_por_genero("Ficción")
