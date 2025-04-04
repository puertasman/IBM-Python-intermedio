
TARIFA_NACIONAL = 0.5
TARIFA_INTERNACIONAL = 1

destino = input("¿El destino del paquete es nacional o internacional? ")
peso = float(input("¿Cuál es el peso del paquete? "))
precio = None

if destino.lower() == "nacional":
    precio = peso * TARIFA_NACIONAL  
elif destino.lower() == "internacional":
    precio = peso * TARIFA_INTERNACIONAL
else:
    print("No se puede aplicar ninguna tarifa, destino no válido")

if precio is not None:
    print(f"El precio por enviar tu paquete a un destino {destino} es {precio} €")