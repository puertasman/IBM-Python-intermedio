""" Una base de datos es un sitio dónde almacenar información de manera estructurada,
organizados y almacenados electrónicamente en un sistema informático"""

import mysql.connector

personas_db = mysql.connector.connect(
    host = 'localhost', # 127.0.0.1
    user = 'root',
    password = 'admin',
    database = 'personas_db'    
)

# vamos a hacer el select


    
cursor = personas_db.cursor()

cursor.execute('SELECT * FROM personas')

resultado = cursor.fetchall()

for linea in resultado:
    print(linea)

cursor.close()
personas_db.close()
