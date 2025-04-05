# las tuplas no son mutables, no se pueden modificar los elementos
# no se pueden añadir ni quitar elementos
# se añaden con paréntesis

mi_tupla = ()

# esto daría error mi_tupla[0] = 1
# no tiene los mismos métodos que una lista
# la manera de cambiar elementos es cambiar la tupla

mi_tupla = (1, 2, 3, 4, 5)

for elemento in mi_tupla:
    print(elemento)

# uno de sus usos es para las coordenadas ya que no se puede cambiar
# ejemplo:

coordenadas = (3,2)

print(f"Coordenadas: x = {coordenadas[0]}, y = {coordenadas[1]}")
