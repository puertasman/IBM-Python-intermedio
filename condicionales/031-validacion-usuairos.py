USUARIO_AUTENTIFICADO = 'admin'
PASSWORD_AUTENTIFICADO = '1234'

usuario = input("Introduce tu nombre de usuario: ")
password = input("Introduce tu contraseña: ")
respuesta = ''
if usuario != USUARIO_AUTENTIFICADO:
    respuesta = "Usuario no válido."
    if password != PASSWORD_AUTENTIFICADO:
        respuesta = "Usuario y contraseña no válidas"
else:
    if password != PASSWORD_AUTENTIFICADO:
        respuesta = "Password invalido"
    else:
        respuesta = "Bienvenido al sistema"

print(respuesta)