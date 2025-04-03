print("### Descuento para socios ###")
COMPRA_MINIMA = 1000

es_socio = input("¿Eres socio del club?(s/n) ")
valor_compra = int(input("¿Cuánto ha gastado en la compra? "))

if es_socio.lower() == "s":
    if valor_compra < COMPRA_MINIMA:
        print(f"Descuento por socio del 5%. Total a pagar {valor_compra*0.95:.2f} $")
    else:
        print(f"Descuento por compra superior a 1000$ y ser socio del 10%. Total a pagar {valor_compra*0.9:.2f} $")
else:
    print("No hay descuento.")