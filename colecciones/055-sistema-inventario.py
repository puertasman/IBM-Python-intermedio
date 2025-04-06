# gestión de inventarios

print("### gestión de inventarios ###")
inventario = []

numero_productos = int(input("¿Cuántos productos tiene el producto? "))
for i in range (numero_productos):
    nombre = input("¿Cómo se llama el producto? ")
    precio = float(input("¿Cuánto cuesta el producto? "))
    cantidad = int(input("¿Cuántos hay en el almacen? "))
    inventario.append({'id' : i,'nombre' : nombre, 'precio' : precio, 'cantidad': cantidad})

print(inventario)

id_buscar = int(input("¿Qué elemento quieres encontrar? "))
producto_encontrado = None

for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado:
    print("Información del producto:")
    print(f'''id: {producto_encontrado.get('id')}
        nombre: {producto_encontrado.get('nombre')}
        precio: {producto_encontrado.get('precio')}
        cantidad: {producto_encontrado.get('cantidad')}
''') 