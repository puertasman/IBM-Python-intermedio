""" Funciones Lambda """

# función cuadrado sin lambda
def cuadrado(x):
    return x ** 2

print(f"El cuadrado de 5 es {cuadrado(5)}")

# función cuadrado con lambda
cuadrado_lambda = lambda x: x ** 2

print(f"El cuadrado de 5 es {cuadrado_lambda(5)}")
