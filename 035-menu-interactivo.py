# menú interactivo

print("### Menú interactivo ###")

while True:
    print()
    print("Menú interactivo")
    print("1. Crear cuenta")
    print("2. Eliminar cuenta")
    print("3. Salir del sistema")
    opcion = input("Seleccion una opción: ")
    if opcion == "1":
        print("Creando cuenta...")
    elif opcion == "2":
        print("Eliminando cuenta...")
    elif opcion == "3":
        print("Salinedo del sistema")
        break
    else:
        print("Opción no válida")