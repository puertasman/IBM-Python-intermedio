# Validación de contraseñas

print("### Validación de contraseñas ###")
password = input("Introduce una contraseña (mínimo 6 caracteres): ")
while len(password) < 6:
    print("La contraseña no es válida. Debe tener al menos 6 caracteres.")
    password = input("Introduce una contraseña (mínimo 6 caracteres): ")
print("Contraseña creada.")