"""Trabajar con cadenas"""

# Dividir cadenas

cadena = "Yo soy una cadena"
palabras = cadena.split()

print(palabras)

#cambiar palabras

cambiado = cadena.replace("cadena", "frase")
print(cambiado)


# buscar devuelve posición

buscar = cadena.find("soy") # posición 3
print("Posición de la cadena buscar {buscar}")

