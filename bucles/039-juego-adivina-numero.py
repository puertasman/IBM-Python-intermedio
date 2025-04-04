# crear un número con while hasta que adivine el número

import random

numero_secreto = random.randint(1, 50)
intentos = 0
intentos_maximos = 5

print("### Juego: Adivina el Número ###")
print("He pensado un número entre 1 y 50.")
while True:
    if(intentos < intentos_maximos):
        numero = int(input("¿Qué número he pensado? "))
        intentos += 1
        if numero < numero_secreto:
            print("El número es mayor que el que has dicho.")
        elif numero > numero_secreto:
            print("El número es menor que el que has dicho.")
        else:
            print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
            break
    else:
        print(f"Te has quedado sin intentos el número era {numero_secreto}")
        break