""" Crear archivos """

nombre_archivo = "archivos/mi_archivo.txt"

# abrir el archivo
with open(nombre_archivo, 'w', encoding="utf-8") as archivo:
    archivo.write('Hola como estas\n')
    archivo.write('estoy agregando información al arhcivo\n')
# con esto se cierra directamente, es mucho más práctico

# archivo = open(nombre_archivo, 'w')
# archivo.write('Hola como estas\n')
# archivo.write('estoy agregando información al arhcivo\n')

# siempre cerrar
# archivo.close()

print(f"Se creó el archivo {nombre_archivo}")
