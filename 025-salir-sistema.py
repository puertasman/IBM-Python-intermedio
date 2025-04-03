print("### Sistema bancario ###")

while __name__ == "__main__":
    print("#################################")
    print("Estás dentro del sistema bancario")
    respuesta = input("¿Quieres salir en el sistema (s/n): ")
    if not respuesta.lower() == "s":
        print("Permaneces en el sistema...")
    else:
        print("Saliendo del sistema...")
        break

