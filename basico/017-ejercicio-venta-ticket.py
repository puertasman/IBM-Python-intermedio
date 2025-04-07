# precio ticket

print("### Generación ticket ###")
precio_leche = float(input("Precio de la leche: "))
precio_pan = float(input("Precio de la pan: "))
precio_lechuga = float(input("Precio de la lechuga: "))
precio_platanos = float(input("Precio de la plátanos: "))

# calcular el subtotal, antes de impuestos
subtotal = precio_pan + precio_leche + precio_lechuga + precio_platanos

# calcular impuestos suponiendo que es un 12 %
impuestos = 16/100 * subtotal

# total
total = subtotal + impuestos

# tíquet venta
print(f'''Ticket de compra
1. precio leche {precio_leche}€
2. precio pan {precio_pan}€
3. precio lechuga {precio_lechuga}€
4. precio plátanos {precio_platanos}€
subtotal {subtotal:.2f}€
impuestos {impuestos:.2f}€
precio total {total:.2f}€''')