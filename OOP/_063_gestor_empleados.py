# gestor de empleados

class Empleado:
    contador_empleados = 0

    def __init__(self, nombre, departamento):
        Empleado.contador_empleados += 1
        self.nombre = nombre
        self.departamento = departamento

    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador_empleados

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar_empleado(self, nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self.empleados.append(empleado)
        print(f"Empleado {nombre} contratado")

    def obtener_numero_empleados_por_departamento(self, departamento):
        numero_empleados_departamento = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento:
                numero_empleados_departamento += 1
        return numero_empleados_departamento
    
    def listar_todos_empleados_por_departamento(self):
        departamentos = set(e.departamento for e in self.empleados)
        for departamento in departamentos:
            print(f"\nTrabajadores del departamento {departamento}:")
            for e in self.empleados:
                if e.departamento == departamento:
                    print(f"\t{e.nombre}")

