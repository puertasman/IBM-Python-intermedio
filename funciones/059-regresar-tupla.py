# devuelve en mayúsuclas

print("Esta función devuelve una tupla")
def persona_en_mayusculas(nombre, apellido, edad):
    print("Devuelve los valores en mayúsculas")
    return(nombre.upper(), apellido.upper(), edad)

datos_mayuculas = persona_en_mayusculas("Antonio", "Fernández", 33)
print(datos_mayuculas, type(datos_mayuculas))