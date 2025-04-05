print("Manejo de lsitas")

nombres = ['Carla', 'Juan', 'Laura']

for nombre in nombres:
    print(nombre)
    
lista_heterogenea = [100, True, "Iván"]

for elemento in lista_heterogenea:
    print(f"Elemento: {elemento} - tipo: {type(elemento)}")