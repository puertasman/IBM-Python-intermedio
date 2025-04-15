""" Programa de la máquina de snacks """

from servicio_snacks import ServicioSnacks
from snack import Snack

class MaquinaSnacks:
    """ Clase de la máquina de Snacks  """
    def __init__(self):
        self.servicio_snacks = ServicioSnacks()
        self.productos = []

    def maquina_snacks(self):
        """ Función que controla el programa """
        salir = False
        print("*** Máquina de Snacks ***")
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f"Ocurrió un error: {e}")

    def mostrar_menu(self):
        """ Muestra las opciones del menú """
        print("""\n---Menú máquina snacks---
            1. Comprar snacks
            2. Mostrar ticket
            3. Agregar nuevo producto
            4. Mostrar inventario de Snacks
            5. Salir""")
        return int(input("Elige una opción: "))
    
    def ejecutar_opcion(self, opcion):
        """ Menú """
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket() 
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print("Hasta pronto.")
            return True
        else:
            print("Opción no válida.")
            return False

    def comprar_snack(self):
        """ método comprar snack """
        id_snack = int(input("¿Qué snack quieres comprar?" ))
        snacks = self.servicio_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
        if snack:
            self.productos.append(snack)
            print(f"Snack encontrado: {snack}")
        else:
            print(f"Id snack no encontrado: {id_snack}")

    def mostrar_ticket(self):
        if not self.productos:
            print("No hay snacks en el ticket")
            return
        total = sum(snack.precio for snack in self.productos)
        print("----Ticket de venta----")
        for producto in self.productos:
            print(f"\t - {producto.nombre} - {producto.precio:.2f} €")
            print(f"\tTotal: {total:.2f}")

    def agregar_snack(self):
        nombre = input("Nombre del snack: ")
        precio = float(input("Precio: "))
        nuevo_snack = Snack(nombre, precio)
        self.servicio_snacks.agregar_snack(nuevo_snack)
        print(f"Snack agregado correctamente.")

# Programa principal
if __name__ == "__main__":
    maquina_snacks = MaquinaSnacks()
    maquina_snacks.maquina_snacks()
