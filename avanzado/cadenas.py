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

# multiplicar cadenas
print("Repite la cadena"*5)

# strip
cadena_sucia = ".. . .Cadena sucia... ."

cadena_limpia = cadena_sucia.rstrip('. ').replace("sucia","limpia")
print(cadena_limpia)
#rstrip sólo derecha
#lstrip sólo izquierda
