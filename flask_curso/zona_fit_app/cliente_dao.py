""" Administrar usuarios, utilizamos patrón de diseño típico, plantilla DATA ACCESS OBJECT """

from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
    """ Para poder modificar usuarios y listarlos """
    SELECCIONAR = 'SELECT * FROM clientes ORDER BY id'
    SELECCIONAR_ID = 'SELECT * FROM clientes WHERE id = %s'
    INSERTAR = 'INSERT INTO clientes(nombre, apellido, membresia) VALUES (%s, %s, %s)'
    ACTUALIZAR = 'UPDATE clientes SET nombre = %s, apellido = %s, membresia = %s WHERE ID = %s'
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

    @classmethod
    def seleccionar_id(cls, id):
        """ Elige la información de los usuarios de la base de datos y los convierte en usuarios """
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (id,)
            cursor.execute(cls.SELECCIONAR_ID, valores)
            registro = cursor.fetchone()
            # mapeo clase-tabla cliente
            cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
            return cliente
        except Exception as e:
            print(f"Ocurrió un error al seleccionar clientes: {e}")
        finally: # se ejecuta siempre
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrió un error al insertar un cliente: {e}")
        finally: # se ejecuta siempre
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)    

    @classmethod
    def actulizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrió un error al actualizar un cliente: {e}")
        finally: # se ejecuta siempre
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)        
    
    @classmethod
    def eliminar(cls,cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,) # , porque es tupla
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrió un error al actualizar un cliente: {e}")
        finally: # se ejecuta siempre
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == "__main__":
    # insertar cliente
    # cliente1 = Cliente(nombre = 'Roberto',apellido = 'Fernández', membresia = 300)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f"Clientes insertados: {clientes_insertados}")
    # actualizar cliente
    # cliente2 = Cliente(poner el que toque, 'Evaristo', 'Tellez', 400)
    # clientes_actualizados = ClienteDAO.actulizar(cliente2)
    # print(f"Cliente actualizado: {clientes_actualizados}")
    # cliente eliminar
    # cliente_eliminar = Cliente(id=5)
    # ClienteDAO.eliminar(cliente_eliminar)
    # print(f"Cliente actualizado: {cliente_eliminar}")
    # seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)
