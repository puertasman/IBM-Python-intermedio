print("### Boletín informativo ###")

suscriptores = {"luisa@mail.com", "juan@mail.com", "marcos@mail.com", "elena@mail.com"}
print(f"Lista de suscriptores:{", ".join(s for s in suscriptores)}")

# nuevo suscriptor
nuevo_suscriptor = "marcos@mail.com"


if nuevo_suscriptor in suscriptores:
    print(f"El suscriptor {nuevo_suscriptor} ya está registrado.")
else:
    suscriptores.add(nuevo_suscriptor)

# eliminar a elena
suscriptor_eliminar = "elena@mail.com"
suscriptores.remove(suscriptor_eliminar)
print(f"El suscriptor {suscriptor_eliminar} ha sido eliminado.")
print(f"Lista de suscriptores: {", ".join(s for s in suscriptores)}")

print("En la lista ahora hay {len(suscriptores)} suscriptores.")

print("### Lista de suscriptores ###")
for s in suscriptores:
    print(f" - {s}")
