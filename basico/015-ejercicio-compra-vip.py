print("###Sistema de descuentos###")

No_productos_descuento = 10

productos = int(input("¿Cuántos productos compraste hoy? "))
tiene_vip = input("¿Eres miembro de la tienda?(S/N) ")

if productos >= No_productos_descuento and tiene_vip.lower() == 's':
    print("Tiene derecho a descuento")
else:
    print("No tiene derecho a descuento")


