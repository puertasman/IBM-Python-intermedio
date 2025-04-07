# ejercicio máquina de snacks

snacks = [
    {'Id': 1, 'nombre': 'Patatas', 'precio': 1.99},
    {'Id': 2, 'nombre': 'Agua', 'precio': 1.49},
    {'Id': 3, 'nombre': 'Galletas', 'precio': 2.99},
    {'Id': 4, 'nombre': 'Refrescos', 'precio': 2.49}
]

def producto_por_Id(id):
    for producto in snacks:
        if

def mostrar_snacks():
    print("\nSnacks disponibles")
    for snack in snacks:
        print(f"Id: {snack.get('Id')} -> {snack.get('nombre')} {snack.get('precio')}€")


def comprar_snacks():
    print("\nComprar snacks")
    mostrar_snacks()
    producto_id = int(input("¿Qué producto quieres comprar? "))
    cantidad_producto = int(input("¿Cuántos quieres? "))
    producto_por_id = producto_por_Id(producto_id)
    print("Añadidos {cantidad_productos} de {prodc}")

def mostrar_ticket():
    print("\nMosrtar ticket")

while True:
    if __name__ == "__main__":
        print("\nMenú máquina de snaks")
        print("\t1. Mostrar snacks")
        print("\t2. Comprar snacks")
        print("\t3. Mostrar ticket")
        print("\t4. Salir")
        eleccion = input("Elige una opción: ")
        if eleccion == "1":
            mostrar_snacks()
        elif eleccion == "2":
            comprar_snacks()
        elif eleccion == "3":
            mostrar_ticket()
        elif eleccion == "4":
            print("Gracias por usar nuestra máquina de vending.")
            break
        else:
            print("Opción no válida.")