print("### Triángulo ###")

ancho = int(input("Cuántas filas debe tener el triángulo: "))
for i in range (1,ancho+1):
    espacios_en_blanco = ancho - i
    print(" " * espacios_en_blanco + "* " * i)
