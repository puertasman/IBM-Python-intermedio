# Programa calculadora
# suma, resta, multiplica y divide

##### funciones

def mostrar_menu():
        print("\nCalculadora Puertas")
        print("1- Suma")
        print("2- Resta")
        print("3- Multiplicación")
        print("4- División")
        print("5- Salir")
        opcion = input("Elige una opción: ")
        return opcion

def pedir_valores():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    return (num1, num2)

def ejecutar_operacion(opcion, salir):
    if 1 <= int(opcion) <= 4:
        print(opcion, type(opcion))
        num1, num2 = pedir_valores()
        if opcion == "1":
            print(f"Resultado: {num1 + num2}")
        elif opcion == "2":
            print(f"Resultado: {num1 - num2}")
        elif opcion == "3":
            print(f"Resultado: {num1 * num2}")
        elif opcion == "4":
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Error: División por cero.")
    elif opcion == "5":
        print("Gracias por utilizar la calculadora.")
        salir = True
    else:
        print("Opción no válida.")
    return salir
        
    


##### programa
if __name__ == "__main__":
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)