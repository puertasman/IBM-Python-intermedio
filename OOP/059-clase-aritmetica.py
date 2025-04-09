# operaciones básicas con clase
class Aritmetica:

    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2
        print(f"Se acaba de crear el objeto con los valores {self.operando1} y {self.operando2}")

    def sumar(self):
        if self.operando1 != None and self.operando2 != None:
            print(f"La suma de {self.operando1} y {self.operando2} es {self.operando1 + self.operando2}")
        else:
            print("No se puede operar.")

    def restar(self):
        if self.operando1 != None and self.operando2 != None:
            print(f"La resta de {self.operando1} y {self.operando2} es {self.operando1 - self.operando2}")
        else:
            print("No se puede operar.")

    def __str__(self):
        return f"Objeto de la clase Aritmetica con valores {self.operando1} y {self.operando2}"

if __name__ == "__main__":
    aritmetica1 = Aritmetica(5,7)
    aritmetica2 = Aritmetica(12,16)
    aritmetica3 = Aritmetica(3)
    aritmetica4 = Aritmetica()

    aritmetica3.operando2 = 4

    aritmetica = [aritmetica1, aritmetica2, aritmetica3, aritmetica4]

    for par in aritmetica:
        print(par)
        par.sumar()
        par.restar()
    