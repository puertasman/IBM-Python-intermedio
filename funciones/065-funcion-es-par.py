print("### función par ###")

def es_par(numero):
    return True if numero % 2 == 0 else False

if __name__ == '__main__':
    numero = int(input("Introduce un valor: "))
    print(f"¿Número par? {es_par(numero)}")