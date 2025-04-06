# ejercicio agenda

print("### Agenda ###")
agenda = {
    "Juan" : {
        "telefono" : "123456789",
        "email" : "juan@mail.com",
        "direccion" : "Calle Falsa 123"
    },
    "María" : {
        "telefono" : "987654321",
        "email" : "maria@mail.com",
        "direccion" : "Avenida Siempre Viva 742"
    },
    "Pedro" : {
        "telefono" : "456789123",
        "email" : "pedro@mail.com",
        "direccion" : "Plaza Mayor 1"
    }
}

# los contactos tienen teléfono, email y dirección
for persona in agenda:
    print("### Contacto ###")
    print(f"- Nombre: {persona}")
    print(f"\tTeléfono: {agenda[persona]['telefono']}")
    print(f"\tEmail: {agenda[persona]['email']}")
    print(f"\tDirección: {agenda[persona]['direccion']}")

agenda['Ana'] = {"telefono" : "321654987", "email" : "ana@mail.com", "direccion" : "Calle Nueva 456"}
print(agenda)

# eliminar un contacto
del agenda['Pedro']
print(agenda)

eliminado = 'María'
datos_eliminado = agenda.pop(eliminado)
print(f"El contacto {eliminado} ha sido eliminado.")

# print todos

print("### Agenda actualizada ###")
for persona in agenda:
    print("### Contacto ###")
    print(f"- Nombre: {persona}")
    print(f"\tTeléfono: {agenda[persona]['telefono']}")
    print(f"\tEmail: {agenda[persona]['email']}")
    print(f"\tDirección: {agenda[persona]['direccion']}")