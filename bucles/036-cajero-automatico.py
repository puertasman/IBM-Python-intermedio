# Cajero automático
# depostiar, retirar y consultar saldo

saldo = 1000

while True:
    print()
    print("### Cajero automático ###")
    print("1 - Ingresar dinero")
    print("2 - Retirar dinero")
    print("3 - Consultar saldo")
    print("4 - Salir")
    opcion = input("Selecciona una opción:")
    if opcion == '1':
        print("Ingresar dinero")
        ingreso = float(input("¿Qué cantidad quieres ingresar?"))
        saldo += ingreso
        print(f"Acabas de ingresar {ingreso} €.")
    elif opcion == '2':
        print("Retirar dinero")
        retiro = float(input("¿Qué cantidad quieres retirar?"))
        if saldo >= retiro:
            saldo -= retiro
            print(f"Acabas de retirar  {retiro} €.")
        else:
            print(f"No puedes retirar {retiro} € saldo insuficiente.")
    elif opcion == '3':
        print("Consultar saldo")
        print(f"El saldo actual de la cuenta es {saldo} €.")
    elif opcion == '4':
        print("Gracias por utilizar el cajero.")
        print("Hasta pronto.")
        break
    else:
        print("Opción no válida")