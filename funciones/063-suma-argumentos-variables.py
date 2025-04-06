print("** Suma argumentos variables **")

def sumar(*args):
    suma_total = 0
    for numero in args:
        suma_total += numero
    return suma_total


resultado = sumar(1,2,3,4,5,333,32,1)

print(f"El resultado de la suma es {resultado}") 