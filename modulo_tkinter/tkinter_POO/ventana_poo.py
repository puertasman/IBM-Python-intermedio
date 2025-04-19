""" Empezamos con POO en tkinter """

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk): # hereda de tkinter
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        # configurar grid
        self.configurar_grid()
        self.mostrar_tabla()

    def configurar_ventana(self):
        self.geometry('600x400')
        self.configure(background = '#1d2d44')
        self.title("Manejo de ventanas con POO")

    def configurar_grid(self):
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 0)

    def mostrar_tabla(self):
        estilo = ttk.Style()
        estilo.theme_use('clam') # prepara el manejo del tema
        estilo.configure('Treeview', background = '#000',
                        foreground = '#fff', fieldbackground = '#000',
                        rowheight = 30)
        estilo.map('Treeview', background = [('selected', '#3a86ff')])

        # Creamos la tabla
        columnas = ('Id', 'Nombre', 'Edad')
        self.tabla = ttk.Treeview(self, columns = columnas, show = 'headings')

        self.tabla.grid(row = 0, column = 0, sticky = tk.NSEW)

        # Cabeceras
        self.tabla.heading(columnas[0], text = columnas[0], anchor = tk.CENTER)
        self.tabla.heading(columnas[1], text = columnas[1], anchor = tk.W)
        self.tabla.heading(columnas[2], text = columnas[2], anchor = tk.W)

        # Formato a las columnas
        self.tabla.column(columnas[0], width = 80)
        self.tabla.column(columnas[1], width = 120)
        self.tabla.column(columnas[2], width = 120)

        # Cargar datos a la tabla
        datos = ((1,'Alejandra',25),(2,'Matías',32))

        for persona in datos:
            self.tabla.insert(parent = '', index = tk.END, values = persona)

        scrollbar = ttk.Scrollbar(self, orient = tk.VERTICAL, command = self.tabla.yview)
        self.tabla.configure(yscroll = scrollbar.set)

        scrollbar.grid(row = 0,column = 1, sticky = tk.NS)
        self.tabla.bind('<<TreeviewSelect>>', self.mostrar_registro_seleccionado)


    def mostrar_registro_seleccionado(self, event):
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado) # cogemos el elemento entero
        persona = elemento['values'] # tupla de los valores
        showinfo(title = f"Persona seleccionada {persona[0]}", message = f"Nombre: {persona[1]}, Edad: {persona[2]}")

if __name__ == "__main__":
    ventana = App()

    ventana.mainloop()
