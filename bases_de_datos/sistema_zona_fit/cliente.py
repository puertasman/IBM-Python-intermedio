""" La calse de clientes """

class Cliente:
    """ Clase para crear y consultar la información del cliente """
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        """ constructor de la clase, no necesita información, lo pone vacío"""
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self):
        """ información del cliente """
        return f"""ID: {self.id}
Nombre: {self.nombre}
Apellido: {self.apellido}
Membresia: {self.membresia}"""
