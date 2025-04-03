print("Estación según meses")
mes = input("Introduce el número del mes (1-12): ")

if mes == "12" or mes == "1" or mes == "2":
    print("Invierno")
elif mes == "3" or mes == "4" or mes == "5":
    print("Primavera")
elif mes == "6" or mes == "7" or mes == "8":
    print("Verano")
elif mes == "9" or mes == "10" or mes == "11":
    print("Otoño")
else:
    print(f"No existe el mes {mes}")