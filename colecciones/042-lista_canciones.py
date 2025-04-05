print("Playlist de canciones")

lista_reproduccion = []

lista_reproduccion.append('Dream On - Aerosmith')
lista_reproduccion.append('Hotel California - Eagles')
lista_reproduccion.append('Staying Alive - Bee Gees')

# ordenar la lista, sort
lista_reproduccion.sort()

print("\nLista de canciones ordenada:")
for cancion in lista_reproduccion:
    print(f" - {cancion}")