# ejercicio máquina de snacks

snacks = [
    {'Id': 1, 'nombre': 'Patatas', 'precio': 1.99},
    {'Id': 2, 'nombre': 'Agua', 'precio': 1.49},
    {'Id': 3, 'nombre': 'Galletas', 'precio': 2.99},
    {'Id': 4, 'nombre': 'Refrescos', 'precio': 2.49}
]

ticket = []

def producto_por_Id(id):
    for producto in snacks:
        if producto.get('Id') == id:
            return producto
    return None

def mostrar_snacks():
    print("\nSnacks disponibles")
    for snack in snacks:
        print(f"Id: {snack.get('Id')} -> {snack.get('nombre')} {snack.get('precio')}€")


def comprar_snacks():
    print("\nComprar snacks")
    while True:
        mostrar_snacks()
        producto_id = int(input("¿Qué producto quieres comprar? "))
        producto = producto_por_Id(producto_id)
        if producto:
            cantidad_producto = int(input("¿Cuántos quieres? "))
            total = cantidad_producto * producto.get('precio')
            print(f"Añadidos {cantidad_producto} de {producto.get('nombre')}, total {total}€.")
            compra = [producto.get('Id'), producto.get('nombre'), producto.get('precio'),cantidad_producto, total]
            ticket.append(compra)
        salir = input("¿Quieres seguir comprando? (S/N)").lower()
        if salir in ['n', 'no']:
            break
        else:
            print("Continuemos con la compra")

def mostrar_ticket():
    print("\nMosrtar ticket")
    if len(ticket)>0:
        print("-----Ticket de compra-----")
        total = 0
        for i, compra in enumerate(ticket, start = 1):
            print(f"{i} - {compra[1]} - precio: {compra[2]} - cantidad: {compra[3]} - total: {compra[4]}€")
            total += compra[4]
        print(f"\n\tPrecio total {total}€")
    else:
        print("No hay nada en la cesta")

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