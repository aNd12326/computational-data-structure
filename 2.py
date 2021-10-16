# EJERCICIO LISTAS 2

#INGRESO DE DATOS
clientes = ['Juan','Pedro','Anaximandro','Eustaquiano','Ana']
nombre = input('Ingrese su nombre: ').capitalize()
precio = float(input('Ingrese el precio: '))
cantidad = int(input('Ingrese la cantidad: '))

#OPERACION
if nombre in clientes:
    porcD = 0.15
else:
    porcD = 0

impC = precio * cantidad
impD = porcD * impC
impP = impC - impD

#RESULTADOS
print('Cliente: ', nombre)
print('Importe de la compra: ', impC)
print('Importe del descuento: ', impD)
print('Importe a pagar: ', impP)

#methods string
# capitalize(): poone la primera letra en mayuscula y las demas en minuscula
# upper(): pone todas las letras en mayusculas
# lower(): pone todas las letras en minusculas