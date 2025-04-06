# args - argumentos - tupla
print("### argumens variables ###")

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f"{superheroe} - {nombre}: {"no tiene" if len(args) == 0 else ", ".join(map(str, sorted(args)))}")

superheroe_superpoderes("Superman", "Clark Kent","Volar")
superheroe_superpoderes("Batman", "Bruce Wayne")
superheroe_superpoderes("Spiderman", "Peter Parker", "Instinto arácnido", "Telarañas")