""" Primer uso de tkinter """

import tkinter as tk
from tkinter import ttk # Mejora de tkinter

# Creación de ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title("Primer TKinter")
ventana.configure(background='#1d2d44')

etiqueta = ttk.Label(ventana, text="Saludos a todos")

def saludar(parametro):
    texto = f"Le has dado al botón con {parametro}"
    etiqueta.configure(text=texto)

#Botones
boton1 = ttk.Button(ventana, text="Enviar", command=saludar)

# Si tienen parámetros tiene que ser lambda
boton1 = ttk.Button(ventana, text="Enviar", command=lambda:saludar('Parámetro'))

# También hay que colocarlo en la ventana
etiqueta.pack(pady=20)
boton1.pack()

ventana.mainloop()
