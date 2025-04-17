""" Actualizar persona """

import mysql.connector

personas_db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'personas_db'
)

# sentencia update

cursor = personas_db.cursor()
sentencia_sql = 'UPDATE personas SET nombre = %s, apellido = %s, edad = %s WHERE id = %s'

valores = ('Josefa', 'Flores', 30, 18)

cursor.execute(sentencia_sql, valores)
personas_db.commit()
print(f"Se ha modificado la información, ahora consta {valores[:3]}")

cursor.close()
personas_db.close()
