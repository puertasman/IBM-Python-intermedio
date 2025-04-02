###########
print("Creador de usuarios de correo")
nombre = input("¿Cómo te llamas? ").strip().lower()
apellido = input("Cuál es tu apellido? ").strip().lower()
correo = f"{nombre}.{apellido}@tuempresa.com"
print(f'''Hola {nombre},
      tu nuevo correo de empresa es {correo}
haz un buen uso de él.''')