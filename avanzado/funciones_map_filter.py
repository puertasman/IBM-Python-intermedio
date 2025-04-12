""" Funciones map y filter """

numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda x: x ** 2, numeros))

print(cuadrados)

# filter y lambda
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)
