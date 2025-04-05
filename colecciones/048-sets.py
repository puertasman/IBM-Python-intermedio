# Los sets son colecciones no ordenadas, mutables y sin duplicados
# no se pueden ubicar por posición, sólo si están o no
# se añaden con llaves

mi_set = {1, 2, 3}
print(mi_set)

mi_set.add(3) # no se añade porque ya existe
mi_set.add(4)
mi_set.add(5)
mi_set.add(7)
print(mi_set)

mi_set.remove(2) # elimina el 2 si está, sino da error
print(mi_set)


for elemento in mi_set:
    print(elemento)

lista = [3, 2,3, 5, 2, 4, 7, 9]
print(f"En la lista hay los elementos {", ".join(map(str, sorted(set(lista))))}")