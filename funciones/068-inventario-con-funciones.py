# inventario con funciones
inventario = [
     {'id': 1,
      'nombre': 'Champú',
      'precio': 3.50,
      'cantidad': 10},
      {'id': 2,
      'nombre': 'Pantalón',
      'precio': 3.99,
      'cantidad': 28},
      {'id': 3,
      'nombre': 'Zapatos',
      'precio': 23.79,
      'cantidad': 15},
      
]

def mostrar_productos():
    for producto in inventario:
        print()
        for clave, valor in producto.items():
            print(f"\t{clave}: {valor}")

def agregar_producto():
    print("\nAgregar nuevo producto")
    id = int(input("Id del producto: "))
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del nuevo producto: "))
    cantidad = int(input("¿Qué stock tiene? "))
    nuevo_producto = {'id': id, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    inventario.append(nuevo_producto)
    print(f"Producto {nombre} añadido.")

def buscar_producto_id():
    print("Buscar producto por ID")
    id_a_buscar = int(input("¿Qué id tiene el producto buscado? "))
    for producto in inventario:
        if producto.get('id') == id_a_buscar:
            print("Información del producto encontrado:")
            print(f"\tID: {producto.get('id')}\n\tNombre: {producto.get('nombre')}\n\tPrecio: {producto.get('precio')}€\n\tCantidad:{producto.get('cantidad')}")
            return
    print("\nProdcuto {id_a_buscar} no encontrado.")


while True:
    if __name__ == "__main__":
        print("\n Menú inventario")
        print("\t1- Mostrar inventario")
        print("\t2- Agregar nuevo producto")
        print("\t3- Buscar producto por ID")
        print("\t4- Salir")

        eleccion = input("Elige una opcion(1-4): ")
        if eleccion == "1":
            mostrar_productos()
        elif eleccion == "2":
            agregar_producto()
        elif eleccion == "3":
            buscar_producto_id()
        elif eleccion == "4":
            print("Gracias por utilizar nuestro programa de inventarios")
            break
        else:
            print("Opción no válida")