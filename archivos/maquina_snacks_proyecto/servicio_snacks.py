""" Clase servicio snacks """

import os.path
from snack import Snack

class ServicioSnacks:
    """ Servicios de la máquina de snacks """
    NOMBRE_ARCHIVO = 'maquina_snacks_proyecto/snacks.txt'

    def __init__(self):
        self.snacks = []
        # Revisar si existe el archivo
        # Si existe obtenemos los snacks
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.snacks = self.obtener_snacks()
        # Si no existe cargamos algunos
        else:
            self.cargar_snacks_iniciales()

    def obtener_snacks(self):
        """ Obtiene snacks del archivo """
        lista_snacks = []
        try:
            with open(ServicioSnacks.NOMBRE_ARCHIVO, 'r', encoding = 'UTF-8') as archivo:
                for linea in archivo:
                    print(linea.strip().split(','))
                    id_snack, nombre, precio = linea.strip().split(',')
                    snack = Snack(nombre, float(precio))
                    lista_snacks.append(snack)
        except Exception as e:
            print(f"Ha habido un error al abrir del archivo: {e}")
        return lista_snacks

    def cargar_snacks_iniciales(self):
        """ Crea archivo snacks.txt y añade snacks """
        snacks_iniciales = [
            Snack('Patatas', 1.50),
            Snack('Refresco', 2.20),
            Snack('Sandwich', 4.15)
        ]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)

    def guardar_snacks_archivo(self, lista):
        """ Guardamos los snacks en la lista """
        try:
            with open(ServicioSnacks.NOMBRE_ARCHIVO, 'a', encoding = "utf-8") as archivo:
                for elemento_snack in lista:
                    archivo.write(f"{elemento_snack.escribir_snack()}\n")
        except Exception as e:
            print(f"Error al guardar snacks en el archivo: {e}")

    def agregar_snack(self, snack):
        """" Añadir un snack """
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])

    def mostrar_snacks(self):
        """ Mostrar los snacks del inventario """
        print("-- Inventario de snacks --")
        for snack in self.snacks:
            print(snack)

    def get_snacks(self):
        """ Obtener los snacks """
        return self.snacks

if __name__ == "__main__":
    servicio = ServicioSnacks()
    for snack in servicio.snacks:
        print(snack)
