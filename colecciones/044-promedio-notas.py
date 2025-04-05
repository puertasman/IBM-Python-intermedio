# programa promedio notas

print("### Programa calculo promedio de notas ###")

notas = []
numero_notas = int(input("¿Cuántas notas necesitas añadir? "))

for i in range (numero_notas):
    nota = float(input(f"Introduce la {i + 1}a nota: "))
    while nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10")
        nota = float(input(f"Introduce la {i + 1}a nota: "))
    notas.append(nota)

print(f"Notas introducidas: {notas}")
suma = sum(notas)
print(f"La suma total de las notas es {suma:.2f}")
promedio = suma / len(notas)

print(f"El promedio de las notas es {promedio:.2f}")