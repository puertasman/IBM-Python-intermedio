edad = int(input("¿Qué edad tienes? "))

respuesta = ''
if edad >= 18:
    respuesta = "mayor"
else:
    respuesta = "menor"

print(f"Una persona con edad {edad} es {respuesta} de edad.")