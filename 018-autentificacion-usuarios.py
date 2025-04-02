# programa de autentificación de usuario
usuarios = {'admin' : '123', 'enrique' : '456', 'juan' : '789'}

usuario = input("¿Cuál es tu usuario? ")

if usuario in usuarios.keys():
    password = input("¿Cuál es tu contraseña? ")
    if usuarios[usuario] == password:
        print(f"Datos correctos, bienvenido {usuario}")
    else:
        print(f"Contraseña no válida")
else:
    print(f"Usuario {usuario} no encontrado")


