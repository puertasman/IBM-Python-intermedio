print("Vamos a comprar dos números")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"El {num1} es mayor que el {num2}")
elif num2 > num1:
    print(f"El {num2} es mayor que el {num1}")
else:
    print(f"{num1} y {num2} son iguales")

resultado = "Número 1" if num1>num2  else "Número 2"
print(f"Es mayor el {resultado}") 

