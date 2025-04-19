""" Zona fit App para guardar, actualizar y modificar personas"""

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

from cliente import Cliente
from cliente_dao import ClienteDAO

class App(tk.Tk):
    color_ventana = "#1d2d44"

    def __init__(self):
        super().__init__()
        self.id_cliente = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry('900x600')
        self.title('App Zona Fit')
        self.configure(background=App.color_ventana)
        # configuración estilos
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam') # para poder modificar
        self.estilos.configure(self, background = App.color_ventana,
                               foreground = '#fff', fieldbackground = '#000')

    def configurar_grid(self):
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)

    def mostrar_titulo(self):
        titulo = tk.Label(self, text = "App Zona Fit",
                          font = ('Arial', 25),
                          background = App.color_ventana,
                          foreground = "#fff")
        titulo.grid(row = 0, column = 0, columnspan = 2, pady = 30)

    def mostrar_formulario(self):
        self.frame_formulario = ttk.Frame()
        nombre_l = ttk.Label(self.frame_formulario, text = 'Nombre: ')
        nombre_l.grid(row = 0, column = 0, sticky = tk.W, pady = 30, padx = 5)
        self.nombre_t = ttk.Entry(self.frame_formulario)
        self.nombre_t.grid(row = 0, column = 1)

        apellido_l = ttk.Label(self.frame_formulario, text = 'Apellido: ')
        apellido_l.grid(row = 1, column = 0, sticky = tk.W, pady = 30, padx = 5)
        self.apellido_t = ttk.Entry(self.frame_formulario)
        self.apellido_t.grid(row = 1, column = 1)

        membresia_l = ttk.Label(self.frame_formulario, text = 'Membresía: ')
        membresia_l.grid(row = 2, column = 0, sticky = tk.W, pady = 30, padx = 5)
        self.membresia_t = ttk.Entry(self.frame_formulario)
        self.membresia_t.grid(row = 2, column = 1)
        
        self.frame_formulario.grid(row = 1, column = 0)

    def cargar_tabla(self):
        self.frame_tabla = ttk.Frame(self)
        self.estilos.configure('Treeview', background = '#000',
                               foreground = '#fff', fieldbackground = '#000',
                               rowheight = 20)
        # columnas  
        columnas = ('Id', 'Nombre', 'Apellido', 'Membresia')
        self.tabla = ttk.Treeview(self.frame_tabla, columns = columnas,
                                  show = 'headings')
        # cabeceras tabla
        self.tabla.heading('Id', text = 'Id', anchor = tk.CENTER)
        self.tabla.heading('Nombre', text = 'Nombre', anchor = tk.W)
        self.tabla.heading('Apellido', text = 'Apellido', anchor = tk.W)
        self.tabla.heading('Membresia', text = 'Membresia', anchor = tk.W)

        # Definir las columnas
        self.tabla.column('Id', anchor = tk.CENTER, width = 50)
        self.tabla.column('Nombre', anchor = tk.W, width = 100)
        self.tabla.column('Apellido', anchor = tk.W, width = 100)
        self.tabla.column('Membresia', anchor = tk.W, width = 100)
        # Cargar datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert('', index=tk.END,
                              values = (cliente.id, cliente.nombre,
                                        cliente.apellido, cliente.membresia))
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient = tk.VERTICAL,
                                  command = self.tabla.yview)
        self.tabla.configure(yscroll = scrollbar.set)
        scrollbar.grid(row = 0, column = 1, sticky = tk.NS)
        
        # Asociar evento
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)

        self.tabla.grid(row = 0, column = 0)
        self.frame_tabla.grid(row = 1, column = 1, padx = 20)

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame(self)
        agregar_boton = ttk.Button(self.frame_botones, text= 'Guardar',
                                   command = self.validar_cliente)
        agregar_boton.grid(row = 0, column = 0, padx = 30)
        eliminar_boton = ttk.Button(self.frame_botones, text= 'Eliminar',
                                   command = self.eliminar_cliente)
        eliminar_boton.grid(row = 0, column = 1, padx = 30)
        limpiar_boton = ttk.Button(self.frame_botones, text= 'Limpiar',
                                   command = self.limpiar_datos)
        limpiar_boton.grid(row = 0, column = 2, padx = 30)

        self.frame_botones.grid(row = 2, column = 0, columnspan = 2, pady = 20)

        self.estilos.configure('TButton', background = '#005f73')
        self.estilos.map('TButton', background = [('active','#0a9396')])

    def validar_cliente(self):
        # validar campos
        if self.nombre_t.get() and self.apellido_t.get() and self.membresia_t.get():
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title = 'Atención',
                          message = "El valor de membresía no es numérico")
                self.membresia_t.delete(0, tk.END)
                self.membresia_t.focus_set()
        else:
            showerror(title = "Faltan datos", message = "Todos los campos son requeridos")
            self.nombre_t.focus_set()

    def validar_membresia(self):
        try:
            int(self.membresia_t.get())
            return True
        except:
            return False

    def guardar_cliente(self):
        nombre = self.nombre_t.get()
        apellido = self.apellido_t.get()
        membresia = self.membresia_t.get()
        # comprobamos si hay id cliente
        if self.id_cliente == None:
            cliente = Cliente(nombre = nombre, apellido = apellido, membresia = membresia)
            ClienteDAO.insertar(cliente)
            showinfo(title = 'Agregar', message = 'Cliente agregado')
        else:
            cliente = Cliente(self.id_cliente, nombre, apellido, membresia)
            ClienteDAO.actulizar(cliente)
            showinfo(title = 'Actualizar', message = 'Cliente actualizado')
        # actualizar la visualización de la tabla
        self.recargar_datos()

    def cargar_cliente(self, event):
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        cliente_t = elemento['values']
        self.id_cliente = cliente_t[0]
        nombre = cliente_t[1]
        apellido = cliente_t[2]
        membresia = cliente_t[3] 
        # antes de cargar los datos vaciamos el formulario
        self.limpiar_formulario()
        self.nombre_t.insert(0, nombre)
        self.apellido_t.insert(0, apellido)
        self.membresia_t.insert(0, membresia)

    def eliminar_cliente(self):
        if self.id_cliente is None:
            showerror(title ="Error", message="Primero hay que seleccionar un registro")
        else:
            cliente = Cliente(id = self.id_cliente)
            ClienteDAO.eliminar(cliente)
            showinfo(title="Eliminado", message = "Cliente eliminado")
            self.recargar_datos()

    def recargar_datos(self):
        """ Volver a cargar todos los datos de la tabla """
        self.cargar_tabla()
        self.limpiar_datos()

    def limpiar_datos(self):
        self.limpiar_formulario()
        self.id_cliente = None
    
    def limpiar_formulario(self):
        self.nombre_t.delete(0, tk.END)
        self.apellido_t.delete(0, tk.END)
        self.membresia_t.delete(0, tk.END)

if __name__ == '__main__':
    ventana = App()
    ventana.mainloop()
