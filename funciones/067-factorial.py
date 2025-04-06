# función factorial

print("### Función factorial con recursividad ###")

def factorial(numero):
    if numero == 0:
        return 1
    else:
        factorial_parcial = numero * factorial(numero-1)
        print(f"El resultado parcial del {numero} es {factorial_parcial}")
        return  factorial_parcial

if __name__ == "__main__":
    numero = int(input("¿De qué número quieres calcular el factorial? "))
    if numero < 0:
        print("No hay factorial de números negativos")
    else:
        print(f"El factorial de {numero} es {factorial(numero)}")