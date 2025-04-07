# receta de cocina

print("###Recetario###")
nombre_receta = input("¿Nombre de la receta? ")
ingredientes_receta = input("Ingredientes:  ")
tiempo_preparacion = int(input("Tiempo de preparación: "))
dificultad_receta = input("Nivel de dificultad (Alta, media, baja): ")

print(f'''La receta {nombre_receta} es de una dificultad {dificultad_receta},
      se tarda {tiempo_preparacion} minutos en hacerla y necesita
      {ingredientes_receta}.''')