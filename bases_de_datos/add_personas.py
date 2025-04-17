""" Una base de datos es un sitio dónde almacenar información de manera estructurada,
organizados y almacenados electrónicamente en un sistema informático"""

import mysql.connector

personas_db = mysql.connector.connect(
    host = 'localhost', # 127.0.0.1
    user = 'root',
    password = 'admin',
    database = 'personas_db'    
)


cursor = personas_db.cursor()

# insertar un registro
CONSULTA = "INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)"
valores = ('Josete', 'Huertas', 33)

cursor.execute(CONSULTA, valores)
personas_db.commit()
print(f"Se ha añaido el nuevo registro a la base de datos: {valores}.")

cursor.close()
personas_db.close()
