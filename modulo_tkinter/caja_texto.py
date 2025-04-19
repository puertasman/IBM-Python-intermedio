""" Primer uso de tkinter """

import tkinter as tk
from tkinter import ttk # Mejora de tkinter

# Creación de ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title("Primer TKinter")
ventana.configure(background='#1d2d44')

def mostrar():
    texto = caja_texto.get() # recupera el valor del texto
    caja_texto.configure(text="")
    print(f"Texto proporcionado: {texto}")
    etiqueta.configure(text=texto)

# Caja texto
caja_texto = ttk.Entry(ventana, font = ('Arial', 15)) # tipo y tamaño
caja_texto.pack(pady = 20)

# Agregar un botón
boton = ttk.Button(ventana, text = "Enviar", command = mostrar)
boton.pack(pady = 20)

# Etiqueta
etiqueta = ttk.Label(ventana, text = "Valor inicial")
etiqueta.pack(pady = 20)

ventana.mainloop()
