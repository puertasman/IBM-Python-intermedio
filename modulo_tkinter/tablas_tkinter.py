""" Tablas en Tkinter """

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

ventana = tk.Tk()
ventana.geometry("600x480")
ventana.configure(background="#1d2d44")
ventana.title("Manejo de tablas")

# configuramos el grid
ventana.columnconfigure(0, weight = 1)
ventana.columnconfigure(1, weight = 0)

# definir estilo
estilo = ttk.Style()
estilo.theme_use('clam') # prepara el manejo del tema
estilo.configure('Treeview', background = '#000',
                 foreground = '#fff', fieldbackground = '#000',
                 rowheight = 30)
estilo.map('Treeview', background = [('selected', '#3a86ff')])

# Creamos la tabla
columnas = ('Id', 'Nombre', 'Edad')
tabla = ttk.Treeview(ventana, columns = columnas, show = 'headings')

tabla.grid(row = 0, column = 0, sticky = tk.NSEW)

# Cabeceras
tabla.heading(columnas[0], text = columnas[0], anchor = tk.CENTER)
tabla.heading(columnas[1], text = columnas[1], anchor = tk.W)
tabla.heading(columnas[2], text = columnas[2], anchor = tk.W)

# Formato a las columnas
tabla.column(columnas[0], width = 80)
tabla.column(columnas[1], width = 120)
tabla.column(columnas[2], width = 120)

# Cargar datos a la tabla
datos = ((1,'Alejandra',25),(2,'Matías',32))

# para probar la barra de desplazamiento
# datos = ((1,'Alejandra',25),(2,'Matías',32),(1,'Alejandra',25),(2,'Matías',32),
#          (1,'Alejandra',25),(2,'Matías',32),(1,'Alejandra',25),(2,'Matías',32),
#          (1,'Alejandra',25),(2,'Matías',32),(1,'Alejandra',25),(2,'Matías',32),
#          (1,'Alejandra',25),(2,'Matías',32),(1,'Alejandra',25),(2,'Matías',32),
#          (1,'Alejandra',25),(2,'Matías',32),(1,'Alejandra',25),(2,'Matías',32),
#          (1,'Alejandra',25),(2,'Matías',32),(1,'Alejandra',25),(2,'Matías',32),
#          (1,'Alejandra',25),(2,'Matías',32),(1,'Alejandra',25),(2,'Matías',32))
for persona in datos:
    tabla.insert(parent = '', index = tk.END, values = persona)

# Asociar el elemento select
def mostrar_registro_seleccionado(event):
    elemento_seleccionado = tabla.selection()[0]
    elemento = tabla.item(elemento_seleccionado) # cogemos el elemento entero
    persona = elemento['values'] # tupla de los valores
    showinfo(title = f"Persona seleccionada {persona[0]}", message = f"Nombre: {persona[1]}, Edad: {persona[2]}")

tabla.bind('<<TreeviewSelect>>', mostrar_registro_seleccionado)

# componente scrolbar
scrollbar = ttk.Scrollbar(ventana, orient = tk.VERTICAL, command = tabla.yview)
tabla.configure(yscroll = scrollbar.set)

scrollbar.grid(row = 0,column = 1, sticky = tk.NS)

# ejecutar el programa
ventana.mainloop()
