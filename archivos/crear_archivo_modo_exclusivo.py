""" Abrir un archivo en modo exclusivo"""

NOMBRE_ARCHIVO = "archivos/mi_archivo2.txt"

try:
    with open(NOMBRE_ARCHIVO, 'x', encoding="utf-8") as archivo:
        archivo.write("Escritura en modo exclusivo\n")
        archivo.write("ESpero sea útil\n")
    print(f"Se ha escrito el archvio {NOMBRE_ARCHIVO}")
except FileExistsError as e:
    print(f"El archivo {NOMBRE_ARCHIVO} ya existe.")
    print(f"Detalla del error: {e}")
