print("Estación según meses")
mes = input("Introduce el número del mes (1-12): ")
respuesta = 'desconocido'
if mes == "12" or mes == "1" or mes == "2":
    print("Invierno")
    respuesta = 'invierno'
elif mes == "3" or mes == "4" or mes == "5":
    print("Primavera")
    respuesta = 'primavera'
elif mes == "6" or mes == "7" or mes == "8":
    print("Verano")
    respuesta = 'verano'
elif mes == "9" or mes == "10" or mes == "11":
    print("Otoño")
    respuesta = 'otoño'
else:
    print(f"No existe el mes {mes}")

print(f"El mes {mes} es {respuesta}.")