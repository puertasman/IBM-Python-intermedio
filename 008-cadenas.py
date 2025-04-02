# cadenas en python

cadena1 = "Hola mundo"
cadena2 = "Python es genial"
cadena3 = '''Múltiples
líneas en una cadena,
son 3 líneas'''

print(cadena1)
print(cadena2)
print(cadena3)

print(cadena1 + cadena2)

print(" ".join([cadena1,cadena2]))


# Más formato de cadenas
nombre = 'Juan'
edad = 30

mensaje = "Hola me llamo {}, y tengo {} años".format(nombre,edad)
print(mensaje)

mensaje = f"Hola me llamo {nombre}, y tengo {edad} años."
print(mensaje)

print(f"La cadena \"{mensaje}\" tiene {len(mensaje)} caracteres.")

print(mensaje.upper())
print(mensaje.lower())
print(mensaje.capitalize())

subcadena =  mensaje[3:30]
print(subcadena)

for i in range(len(mensaje)):
    print(mensaje[:i])