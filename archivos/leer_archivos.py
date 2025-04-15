""" Leer archivo en Python """

NOMBRE_ARCHIVO = 'archivos/mi_archivo2.txt'

with open(NOMBRE_ARCHIVO, 'r', encoding='UTF-8') as archivo:
    # Leer todas las líneas del archivo
    # print(archivo.readlines())
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())

# Leer todo el contenido del archivo utilizando read
print("Leyendo el contendido con el método read")
with open(NOMBRE_ARCHIVO, 'r', encoding="UTF-8") as archivo:
    print(archivo.read())
