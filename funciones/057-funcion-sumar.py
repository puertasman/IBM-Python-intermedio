# sumar en función

def sumar(a, b):
    resultado = a + b
    return resultado

# arg1, arg2= 5, 7
arg1 = float(input("¿Cuál es el primer valor de la suma? "))
arg2 = float(input("¿Cuál es el segundo valor de la suma? "))
resultado_suma = sumar(arg1, arg2)

print(f"El resultado de la suma es {resultado_suma}")