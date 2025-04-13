""" Decoradores """

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Antes de llamar la función")
        resultado = funcion(*args, **kwargs)
        print("Después de llamar a la función")
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Carlos")
