""" Aplicación clientes """

from cliente_dao import ClienteDAO

opcion = None
while opcion != 5:
    print("""\n*** MENÚ ***
    1. Listar clientes
    2. Agregar cliente
    3. Modificar cliente
    4. Eliminar cliente
    5. Salir""")
    try: 
        opcion = int(input("Escribe tu opción: "))
        if opcion == 1:
            clientes = ClienteDAO.seleccionar()
            for cliente in clientes:
                print(cliente)
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            print("Gracias por utilizar la aplicación del Gimnasio.")
            break
        else:
            print("Debes introducir una opción válida.")
    except Exception as e:
        print('Debes introducir una opción válida.')
