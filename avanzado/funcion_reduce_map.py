""" Función reduce y map """

from functools import reduce

numeros = [1, 2, 3, 4, 5]

suma_acumulada = reduce(lambda x, y: x + y, numeros)

print(suma_acumulada)
