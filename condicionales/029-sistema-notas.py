nota = float(input("Introduce la nota obtenida: "))
calificacion = ''

if 9 <= nota <= 10:
    calificacion = 'A'
elif 8 <= nota < 9:
    calificacion = 'B'
elif 7 <= nota < 8:
    calificacion = 'C'
elif 6 <= nota < 7:
    calificacion = 'D'
elif 5 <= nota < 6:
    calificacion = 'E'
elif 0 <= nota < 5:
    calificacion = 'F'
else:
    calificacion = "Valor desconocido"

print(f"La calificación obtenida con un {nota} es {calificacion}")