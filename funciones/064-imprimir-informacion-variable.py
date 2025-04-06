print("### Uso de kwargs para imprimir información ***")

def imprimir_informacion(**kwargs):
    print("Valores recibidos:")
    for i, (llave, valor) in enumerate(kwargs.items(), start=1):
        print(f"  {i} - {llave}: {valor}")

imprimir_informacion(nombre = "Carla", edad = 30)

imprimir_informacion(nombre = "carlos", edad = 28, ciudad = "Guadalajara", cargo = "Gerente")
