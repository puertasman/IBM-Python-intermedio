""" Conexión a la base de datos """
from mysql.connector import pooling


class Conexion:
    """ Clase para las conexiones """
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = '192.168.1.20'
    POOLSIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        """ Un pool para que pueda haber 5 conexiones """
        if cls.pool is None: # creamos el pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOLSIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    user = cls.USERNAME,
                    password = cls.PASSWORD,
                    database = cls.DATABASE
                )
                return cls.pool
            except Exception as e:
                print(f"Ocurrió un error al obtener pool: {e}")
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        """ da pool a quien pide """
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        """ libera la conexión libre """
        conexion.close()

if __name__ == '__main__':
    # creamos el pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print("Se ha liberado la conexión 1")
