from _063_gestor_empleados import Empleado, Empresa

print("***Sistema empleados***")

# creamos la empresa
empresa1 = Empresa("Mi empresa")

# creamos los empleados
empresa1.contratar_empleado("Juan", 'Ventas')
empresa1.contratar_empleado("María", 'Marketing')
empresa1.contratar_empleado("Pedro", 'Ventas')
empresa1.contratar_empleado("Ana", "Recursos humanos")

# total empleados
print(f"El número total de empleados en la empresa {empresa1.nombre} es {Empleado.obtener_total_empleados()}.")

# empleados ventas.

print(f"El número total de empleados en el departamento ventas es {empresa1.obtener_numero_empleados_por_departamento('Ventas')}.")

empresa1.listar_todos_empleados_por_departamento()

empresa1.mostrar_todos_los_empleados()