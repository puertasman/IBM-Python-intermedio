print("### Repetición de datos ###")

mensaje = input("Introduce el mensaje a repetir: ")
repeticiones = int(input("¿Cuántas veces quieres repetir el mensaje?"))

for i in range (repeticiones):
    print(f"{i+1} - {mensaje}")

