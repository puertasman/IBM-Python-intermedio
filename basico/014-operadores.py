## operadores aritméticos

a = 10
b = 4
# también se podría hacer a, b = 10, 4

# suma
c = a + b
print(f"La suma de {a} y {b} es {c}")

# resta
c = a - b
print(f"La resta de {a} y {b} es {c}")

# multiplicación
c = a * b
print(f"La multiplicación de {a} y {b} es {c}")

# potencia
c = a ** b
print(f"La potencia de base {a} y exponente {b} es {c}")

# división
c = a / b
print(f"La división de {a} entre {b} es {c}")

# división entera
c = a // b
print(f"La división entera de {a} entre {b} es {c}")

# módulo
c = a % b
print(f"El módulo de la división entre {a} y {b} es {c}")

# operadores de asignación
a = 5
print(f"el valor de a es {a}")
cadena = "esto es una cadena"
print(f"el valor de a es {b}")
a, b, c, d = "hola", 3, 2.1, True
print(f"los valores de a, b, c y d son {a}, {b}, {c} y {d}")

# operadores de asignación y operación
a, b = 10, 15
a += b # esto es a = a + b
print(f"La variable a ahora vale {a}")

a -= b # esto es a = a - b
print(f"La variable a ahora vale {a}")

a *= b # esto es a = a * b
print(f"La variable a ahora vale {a}")

a /= b # esto es a = a / b
print(f"La variable a ahora vale {a}")

a %= b # esto es a = a % b
print(f"La variable a ahora vale {a}")

a **= b # esto es a = a ** b
print(f"La variable a ahora vale {a}")

## operadores comparación
print("Operadores de comparación")
a, b = 7, 5
print(f"Los valores de a y b son {a} y {b}")

resultado = a == b
print(f"Resultado de a == b es {resultado}")

resultado = a != b
print(f"Resultado de a != b es {resultado}")

resultado = a < b
print(f"Resultado de a < b es {resultado}")

resultado = a > b
print(f"Resultado de a > b es {resultado}")

resultado = a <= b
print(f"Resultado de a <= b es {resultado}")

resultado = a >= b
print(f"Resultado de a >= b es {resultado}")

# operadores lógicos
print("operadores lógicos")

a,b = True, False
print(f"Los valores a y b valen {a} y {b}")

# and
resultado = a and b
print(f"El resultado de a and b es {resultado}")

# or
resultado = a or b
print(f"El resultado de a or b es {resultado}")

# not
resultado = not a
print(f"El resultado de not a b es {resultado}")
