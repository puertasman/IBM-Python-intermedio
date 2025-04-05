print("### Boletín informativo ###")

suscriptores = set()

# nuevo suscriptor
numero_suscriptores = int(input("¿Cuántos suscriptores hay? "))

for i in range(numero_suscriptores):
    print("Introducir datos suscriptor")
    nuevo_suscriptor = input(f"Introduce el email del suscriptor {i + 1}: ")
    suscriptores.add(nuevo_suscriptor)
    print(f"Suscriptor {nuevo_suscriptor} añadido.")

print(f"Lista de suscriptores: {', '.join(s for s in suscriptores)}")

nuevo_suscriptor = input("Introduce el email de nuevo suscriptor: ")
if nuevo_suscriptor not in suscriptores:
    suscriptores.add(nuevo_suscriptor)
else:
    print(f"El suscriptor {nuevo_suscriptor} ya está en la lista.")

# eliminar usuario
suscriptor_eliminar = input("Introduce el email del suscriptor a eliminar: ")
suscriptores.remove(suscriptor_eliminar)
print(f"El suscriptor {suscriptor_eliminar} ha sido eliminado.")
print(f"Lista de suscriptores: {", ".join(s for s in suscriptores)}")

print("En la lista ahora hay {len(suscriptores)} suscriptores.")

print("### Lista de suscriptores ###")
for s in suscriptores:
    print(f" - {s}")
