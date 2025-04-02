print("### programa para ver si está en un rango ###")

VALOR_MINIMO = 0
VALOR_MAXIMO = 5

numero_usuario = int(input("A ver si tu número está entre 0 y 5: "))
esta_dentro = numero_usuario >= VALOR_MINIMO and numero_usuario <= VALOR_MAXIMO
print(f"El valor está dentro: {esta_dentro}")