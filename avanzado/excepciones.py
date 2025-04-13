""" EXCEPCIONES """

def dividir(numerador, denominador):
    try:
        if denominador == 0:
            raise Exception("El denominador es 0")
        resultado = numerador/denominador
        print(f"El Resultado de la división es {resultado}")
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    else:
        print("Todo ha ido sin problemas")
    finally:
        print("Terminamos de procesar la excepción\n")
    #except ZeroDivisionError:
    #    print("No se puede dividir por 0")
    #except TypeError:
    #    print("Los operandos deben ser numéricos")

dividir(10,2)

dividir(6,0)

dividir("a",7)
