producto = {
    'nombre' : 'Bolígrafo',
    'precio' : 1.75,
    'cantidad' : 20
}

print("###############Datos producto###############")
for dato in producto:
    print(f"{dato}: {producto[dato]}")

producto['nombre'] = "Lápiz"
producto['precio'] = 2.25
print()
print("###############Datos producto###############")
for dato in producto:
    print(f"{dato}: {producto[dato]}")