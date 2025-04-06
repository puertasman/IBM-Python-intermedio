# keywords arguments, diccionarios

print("Argumentos variables con llame\n")

def superheroes_superpoderes(nombre, *args, **kwargs):
    print(f"{nombre} - {args}. Más info: {kwargs}")

superheroes_superpoderes("Spiderman", "instinto aracnido", edad = 17, empresa = "Marvel")
superheroes_superpoderes("Ironman", "armadura", "playboy", edad = 45)
superheroes_superpoderes("Mi vecino", personalidad = "buenas vibras")