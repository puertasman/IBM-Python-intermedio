""" GENERADORES """

def generador(maximo):
    contador = 0
    while contador < maximo:
        yield contador
        contador += 1
        
# Creamos un generador
var_generador = generador(5)

# Iteramos
for valor in var_generador:
    print(valor)

# con expresión, parecido a compresión pero son con () genera tuplas
generador = (x**2 for x in range(20) if x % 2 == 0)

for cuadrados_pares in generador:
    print(cuadrados_pares)
