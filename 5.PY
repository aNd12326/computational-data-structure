# Desarrolle una aplicacion que permita calcular el importe de la compra, 
# el importe del descuento, el importe a pagar. 
# El porcD sera del 20% si la cantidad adquirida es mayor a 100 si no, no hay descuento.

def impC(p, c):
    return p * c

def impD(p, c):
    if c > 100:
        porcD = 0.20
    else:
        porcD = 0
    d = porcD * impC(p, c)
    return d

def impP(p, c):
    p = impC(p, c) - impD(p, c)
    return p

#programa principal
precio = float(input('Ingrese el precio: '))
cantidad = int(input('Ingrese la cantidad: '))
print('Importe de la compra: ' , impC(precio, cantidad) )
print('Importe del descuento: ' , impD(precio, cantidad) )
print('Importe a pagar: ' , impP(precio, cantidad) )