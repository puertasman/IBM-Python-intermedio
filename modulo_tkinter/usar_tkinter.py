""" Primer uso de tkinter """

import tkinter as tk

# Creación de ventana
ventana = tk.Tk()

# Dimensiones de ventana
ventana.geometry('800x640')

# Título
ventana.title("Primer TKinter")

# Evitar redimensionar la ventana
ventana.resizable(0,0)

# Color de la ventana
ventana.configure(background='#1d2d44')

# La hacemos visible
ventana.mainloop()
