""" Aplicación clientes """

from cliente_dao import ClienteDAO
from cliente import Cliente

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
        elif opcion == 2: # añadir un cliente
            nombre_var = input("Nombre del nuevo usuario: ")
            apellido_var = input("Apellido del nuevo usuario: ")
            membresia_var = input("Escribe el número de miembro: ")
            cliente = Cliente(nombre = nombre_var, apellido = apellido_var,
                              membresia = membresia_var)
            clientes_insertados = ClienteDAO.insertar(cliente)
            print(f"Clientes insertados: {clientes_insertados}")
        elif opcion == 3:
            id_cliente_var = int(input("Escribe el ID del cliente a modificar: "))
            nombre_var = input("Nombre del nuevo usuario: ")
            apellido_var = input("Apellido del nuevo usuario: ")
            membresia_var = input("Escribe el número de miembro: ")
            cliente = Cliente(id_cliente_var, nombre_var, apellido_var,
                              membresia_var)
            clientes_actualizados = ClienteDAO.actulizar(cliente)
            print(f"Clientes actualizados: {clientes_actualizados}")
        elif opcion == 4:
            id_cliente_var = int(input("Escribe el ID del cliente a modificar: "))
            cliente = Cliente(id=id_cliente_var)
            clientes_borrados = ClienteDAO.eliminar(cliente)
            print(f"Clientes actualizados: {clientes_borrados}")
        elif opcion == 5:
            print("Gracias por utilizar la aplicación del Gimnasio.")
            break
        else:
            print("Debes introducir una opción válida.")
    except Exception as e:
        print('Debes introducir una opción válida.')
