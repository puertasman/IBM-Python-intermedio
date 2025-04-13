""" Ordenar los iterables """

# Diferente a sort y devuelve lista ordenada

# Sintaxis: sorted(iterable, key = None, reverse = False)

empleados = ['Juan', 'Pedro', 'María']


empleados_ordenados = sorted(empleados)
print(f"Empleados ordenados: {empleados_ordenados}")

empleados_ordenados = sorted(empleados,reverse = True)
print(f"Empleados ordenados descendentemente: {empleados_ordenados}")

# ordenador diccionario con una llave
empleados_dict = [
    {'nombre' : 'Juan', 'salario': 3000},
    {'nombre' : 'María', 'salario': 2500},
    {'nombre' : 'Pedro', 'salario': 3500},
    {'nombre' : 'Antonio', 'salario': 3100}
]

empleados_ordenados_por_salario = sorted(empleados_dict, key = lambda x: x['salario'] )
print(f"Empleados ordenados por salarios: {empleados_ordenados_por_salario}.")
