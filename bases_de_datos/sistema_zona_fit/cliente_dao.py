""" Administrar usuarios, utilizamos patrón de diseño típico, plantilla DATA ACCESS OBJECT """

from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
    """ Para poder modificar usuarios y listarlos """
    SELECCIONAR = 'SELECT * FROM clientes ORDER BY id'
    INSERTAR = 'INSERT INTO clientes(nombre, apellido, miembro) VALUES (%s, %s, %s)'
    ACTUALIZAR = 'UPDATE clientes SET nombre = %s, apellido = %s, miembro = %s WHERE ID = %s'
    ELIMINAR = 'DELETE FROM clientes WHERE ID = %s'

    @classmethod
    def seleccionar(cls):
        """ Elige la información de los usuarios de la base de datos y los convierte en usuarios """
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # mapeo clase-tabla cliente
            clientes = []
            for registro in registros:
                nuevo_cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(nuevo_cliente)
            return clientes
        except Exception as e:
            print(f"Ocurrió un error al seleccionar clientes: {e}")
        finally: # se ejecuta siempre
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == "__main__":
    # seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    print(clientes)
    for cliente in clientes:
        print(cliente)
