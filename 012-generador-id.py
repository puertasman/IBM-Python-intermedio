# generador de ids
import random

nombre = input("¿Cómo te llamas? ")
apellido = input("¿Cuál es tu apellido? ")
ano_nacimiento = input("¿En qué año naciste? ")

id = nombre[:2].upper()+apellido[:2].upper()+ano_nacimiento[-2:]+str(random.randint(1000,9999))
print(f"Tu identificador es {id}.")