print("Playlist de canciones")

lista_reproduccion = []

numero_canciones = int(input("¿Cuántas canciones quieres añadir a la lista de reproducción? "))

for i in range(numero_canciones):
    print(f"Datos de la canción {i + 1}")
    cancion = input("Introduce el nombre de la canción: ")
    artista = input("Introduce el nombre del artista: ")
    lista_reproduccion.append(f"{cancion} - {artista}")

# ordenar la lista, sort
lista_reproduccion.sort() # revese=True para que hacer el orden descendente

print("\nLista de canciones ordenada:")
for cancion in lista_reproduccion:
    print(f" - {cancion}")