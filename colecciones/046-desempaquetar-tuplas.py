# desenpaquetar, es asignar el valor de una tupla a varias variables

objeto = ('Juan', 25, 'Ingeniero')

nombre, edad, profesion = objeto

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Profesión: {profesion}")

# modifico la edad y vuelvo a empaquetar
edad += 30

objeto = (nombre, edad, profesion)

print(objeto)