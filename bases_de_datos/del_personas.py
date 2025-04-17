""" Eliminar personas """

import mysql.connector

personas_db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'personas_db'
)

# sentencia delete
cursor = personas_db.cursor()

sentencia_sql = "DELETE FROM personas WHERE id = %s"
persona = (18,)

cursor.execute(sentencia_sql, persona)
print("Persona eliminada correctamente")

personas_db.commit()

cursor.close()
personas_db.close()
