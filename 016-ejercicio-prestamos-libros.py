# préstamos de libros
print("Sistema de préstamo de libros")
distancia_maxima = 3

es_estudiante = input("¿Tiene carnet de estudiante?(S/N) ").lower()
distancia_persona = int(input("¿A cuánto vives de la biblioteca? "))

if es_estudiante == 's' or distancia_persona <= distancia_maxima:
    print("Puedes llevarte el libro a casa")
else:
    print("No puedes llevarte libros a casa")