vehiculo = {
    'marca' : 'Subaru',
    'modelo' : 'Forester',
    'ano' : 2012
}

print("####Datos coche####")
for dato in vehiculo:
    print(f"{dato}: {vehiculo[dato]}")

vehiculo['marca'] = 'Jeep'
vehiculo['modelo'] = 'Compass'
vehiculo['ano'] = 2020

print()
print("####Datos coche####")
for dato in vehiculo:
    print(f"{dato}: {vehiculo[dato]}")

vehiculo['marca'] = 'Ford'
vehiculo['modelo'] = 'Mustang'
vehiculo['ano'] = 1957

print()
print("####Datos coche####")
for dato in vehiculo:
    print(f"{dato}: {vehiculo[dato]}")
