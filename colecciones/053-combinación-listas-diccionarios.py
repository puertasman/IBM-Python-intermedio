# combinación listas diccionarios

personas = [
    {'nombre': 'Juan', 'edad': 25, 'profesión': 'Ingeniero'},
    {'nombre': 'Ana', 'edad': 30, 'profesión': 'Arquitecta'},
    {'nombre': 'Luis', 'edad': 28, 'profesión': 'Médico'},
    {'nombre': 'Sofía', 'edad': 22, 'profesión': 'Diseñadora'},
    {'nombre': 'Pedro', 'edad': 35, 'profesión': 'Abogado'},
    {'nombre': 'María', 'edad': 27, 'profesión': 'Contadora'},
    {'nombre': 'Javier', 'edad': 29, 'profesión': 'Programador'},
    {'nombre': 'Laura', 'edad': 31, 'profesión': 'Psicóloga'}    
]

print(f"Nombre: {personas[0].get('nombre')}")
print(f"Edad: {personas[0].get('edad')}")
print(f"Profesión: {personas[0].get('profesión')}")

for contador, persona in enumerate(personas):
    print(f"Persona {contador + 1}:")
    print(f"Nombre: {persona.get('nombre')}")
    print(f"Edad: {persona.get('edad')}")
    print(f"Profesión: {persona.get('profesión')}")
    print()