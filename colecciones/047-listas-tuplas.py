# mezcla de diferentes tipos de datos

print("### Listas y tuplas de productos ###")

productos = [
    ("P001", "Camiseta", 20.00),
    ("P002", "Pantalón", 35.50),
    ("P003", "Sudadera", 42.75)
]

# Imprimir información de productos y precio total
for i, producto in enumerate (productos):
    print(f" - Producto {i+1}. Código: {producto[0]}, producto: {producto[1]}, precio: {producto[2]:.2f}€")

precioTotal = sum(producto[2] for producto in productos)
print(f"El precio total de los productos es: {precioTotal:.2f}€.")