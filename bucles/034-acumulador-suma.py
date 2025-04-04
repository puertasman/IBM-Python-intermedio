print("### Acumulador suma ###")
VALOR_MAXIMO = 5
acumulador_suma = 0
contador = 1

while contador <= 5:
    print(f"Suma actual es: {acumulador_suma} + {contador}")
    acumulador_suma += contador
    print(f"La suma acumulada es: {acumulador_suma}")
    contador +=1

print(f"El resultado final es: {acumulador_suma}")