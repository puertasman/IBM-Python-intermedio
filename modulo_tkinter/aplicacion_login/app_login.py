""" Uso de frames"""

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

ventana = tk.Tk()

ventana.geometry('600x400')
ventana.title("Log in")
ventana.configure(background = "#1d2d64")

# configuración
ventana.columnconfigure(0, weight = 1)
ventana.rowconfigure(0, weight = 1)

# estilas
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure(ventana, background = '#1d2d64', foreground = '#fff',
                  fieldbackground = '#444')
estilos.configure('TButton', background = '#005f73')
estilos.map('TButton', background=[('active','#0a9396')])

# agregamos el frame
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight = 1)
frame.rowconfigure(0, weight = 3)

# title
etiqueta = ttk.Label(frame, text = "Login", font = ('Arial', 20))
etiqueta.grid(row = 0, column = 0, columnspan = 2)

# usuario
usuario = ttk.Label(frame, text = "Usuario:", )
usuario.grid(row = 1, column = 0, sticky = tk.W, padx = 5, pady = 5)
# entrada de texto
usuario_caja_texto = ttk.Entry(frame)
usuario_caja_texto.grid(row = 1, column = 1, sticky = tk.E, padx = 5, pady = 5)

# password
password = ttk.Label(frame, text = "Password:")
password.grid(row = 2, column = 0, sticky = tk.W, padx = 5, pady = 5)
# entrada de texto
password_caja_texto = ttk.Entry(frame, show = "*")
password_caja_texto.grid(row = 2, column = 1, sticky = tk.E, padx = 5, pady = 5)

# boton
login_boton = ttk.Button(frame, text = "Enviar")
login_boton.grid(row = 3, column = 0, columnspan= 2, padx = 5, pady = 5)

def validar():
    """ Al intentor loguear"""
    usuario_val = usuario_caja_texto.get()
    password_val = password_caja_texto.get()
    if usuario_val == 'root' and password_val == 'admin':
        showinfo(title = "Login", message= "Datos correctos")
    else:
        showerror(title = "Login", message= "Datos incorrectos")

# asociar eventos
login_boton.bind('<Return>', validar) # al presionar enter
login_boton.bind('<Button-1>', validar) # clic izquierdo

# Colocamos el frame
frame.grid(row = 0, column = 0)

# programa
ventana.mainloop()
