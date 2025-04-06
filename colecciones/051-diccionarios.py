# Ejercicios diccionarios

print("### Ejercicio diccionario ###")

persona = { 'nombre' : 'Sergio', 'edad' : 20, 'profesión' : 'Ingeniero'}

print(persona, type(persona))

print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")
print(f"Profesión: {persona['profesión']}")

# modificar el valor de la clave
persona['edad'] = 35

print(persona)


# Agregar una nueva clave
persona['email'] = 'sergio@mail.com'
print(persona)

# Eliminar una clave
del persona['profesión']
print(persona)

# items devuelve la clave y el valor key:value
for clave, valor in persona.items():
    print(f"{clave}: {valor}")