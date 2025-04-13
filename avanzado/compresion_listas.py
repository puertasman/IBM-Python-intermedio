""" comprensión de listas """

# Filtrar sólo los números pares hasta el 100 en una lista

numeros_pares = []

for numero in range (101):
    if numero % 2 == 0:
        numeros_pares.append(numero)

print(numeros_pares)

# compresión de lista: sintaxis variable = [expresion for elemento in iterable condición]

pares = [n for n in range (101) if n % 2 == 0]
print(pares)
