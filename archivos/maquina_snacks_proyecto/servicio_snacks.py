""" Clase servicio snacks """

import os.path
from snack import Snack

class ServicioSnacks:
    """ Servicios de la máquina de snacks """
    NOMBRE_ARCHIVO = 'archivos/maquina_snacks_proyecto/snacks.txt'

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
        return ""

    def cargar_snacks_iniciales(self):
        """ Crea archivo snacks.txt y añade snacks """
        snacks_iniciales = [
            Snack('Patatas', 1.50),
            Snack('Refresco', 2.20),
            Snack('Sandwich', 4.15)
        ]
        self.snacks.extend(snacks_iniciales)

if __name__ == "__main__":
    servicio = ServicioSnacks()
    for snack in servicio.snacks:
        print(snack)
