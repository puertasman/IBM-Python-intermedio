# Colección ordenada y mutable de elementos

print("### Manejo de listas ###")

mi_lista = [1, 2, 3, 4, 5]
print(type(mi_lista))
print(mi_lista)

print(f"Valor de la posición 4: {mi_lista[3]}")
print("Cambio de valor de la posición 2, ahora 10.")
mi_lista[1] = 10
print(mi_lista)

print("Agregar elementos a la lista, en la posición final.")
mi_lista.append(6)

print(mi_lista)

# Eliminar elementos de la lista
print("Elminar elemento de la posición 3.")
del mi_lista[2]

print(mi_lista)


# Tamaño de la lista
print(f"Tamaño de la lista: {len(mi_lista)}")
