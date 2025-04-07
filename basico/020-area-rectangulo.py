print("### Calcular área y perímetro de un rectángulo ###")

base = float(input("¿Cuál es la base del rectángulo? "))
altura = float(input("¿Cuál es la altura del rectángulo? "))

area = base * altura
perimetro = 2 * (base + altura)
print(f"El área del rectángulo de base {base} y altura {altura} es {area}.")
print(f"El perímetro del rectángulo de base {base} y altura {altura} es {perimetro}.")