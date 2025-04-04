# Programa calculadora

while True:
    print()
    print("### Calculadora ###")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = input("Selecciona una opción (1-5): ")
    if opcion == '1':
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 + num2
        print(f"El resultado de la suma de {num1} y {num2} es: {resultado}")
    elif opcion == '2':
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 - num2
        print(f"El resultado de la resta de {num1} y {num2} es: {resultado}")
    elif opcion == '3':
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 * num2
        print(f"El resultado de la multiplicación de {num1} y {num2} es: {resultado}")
    elif opcion == '4':
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 / num2
        print(f"El resultado de la división de {num1} y {num2} es: {resultado}")
    elif opcion == '5':
        print("Gracias por utilizar la calculadora.")
        break
    else:
        print("Opción no válida.")