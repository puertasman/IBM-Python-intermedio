"""Ejercicio zip"""
nombre = ["Juan", "María", "Pedro"]
edad = 30, 25, 35
ciudad = ["Madrid", "Barcelona", "Sevilla"]

# crea un tipo zip
personas = zip(nombre,edad,ciudad)
print(type(personas))
for persona in personas:
    print(f"""**** PERSONA ***
    Nombre: {persona[0]}
    Edad: {persona[1]}
    Ciudad: {persona[2]}""")
# si no tiene suficientes valores para todos los miembros no crea
