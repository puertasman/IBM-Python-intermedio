""" Añadir información """

NOMBRE_ARCHIVO = "archivos/mi_archivo2.txt"

with open(NOMBRE_ARCHIVO,'a', encoding='UTF-8') as archivo:
    archivo.write("Una frase al final\n")
    archivo.write("Saliendo de añadir información\n")
    
print(f"Se ha añadido información en {NOMBRE_ARCHIVO}")
