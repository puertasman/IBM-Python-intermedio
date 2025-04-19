""" Primer uso de tkinter """

import tkinter as tk
from tkinter import ttk # Mejora de tkinter

# Creación de ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title("Primer TKinter")
ventana.configure(background='#1d2d44')

# Manejo de grid
boton1 = ttk.Button(ventana,text="Botón 1")
boton2 = ttk.Button(ventana,text="Botón 2")
boton3 = ttk.Button(ventana,text="Botón 3")

# Configuración del grid
ventana.columnconfigure(0, weight = 1)
ventana.columnconfigure(1, weight = 3)
ventana.columnconfigure(2, weight = 3)
ventana.columnconfigure(3, weight = 3)
ventana.columnconfigure(4, weight = 1)

ventana.rowconfigure(0, weight = 3)
ventana.rowconfigure(1, weight = 3)
ventana.rowconfigure(2, weight = 3)

boton1.grid(row = 0, column = 1, sticky = tk.NSEW, padx = 20, pady = 20) # margin
boton2.grid(row = 0, column = 2, sticky = tk.SE, ipadx = 20, ipady = 20) # padding
boton3.grid(row = 0, column = 3, sticky = tk.NW)

ventana.mainloop()
