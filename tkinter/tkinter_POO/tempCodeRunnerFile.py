a
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