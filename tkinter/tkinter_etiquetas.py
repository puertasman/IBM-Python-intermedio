""" Primer uso de tkinter """

import tkinter as tk
from tkinter import ttk # Mejora de tkinter

# Creación de ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title("Primer TKinter")
ventana.configure(background='#1d2d44')

# Componente etiqueta
etiqueta = ttk.Label(ventana, text="Saludos a todos")

# Cambiar el texto con configure
etiqueta.configure(text="Nos vemos...")

# Cambiar el texto con la llame text
etiqueta['text'] = "Adiós"

# Publicarlo en la ventana
# parametro padx pady, margen respecto al padre
etiqueta.pack(pady=20)

ventana.mainloop()
