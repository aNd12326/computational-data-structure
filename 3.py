# Ejercicio funciones 1
import random

def saludo():
    nombre = input('Ingrese su nombre: ').capitalize()
    print('Hola', nombre)

def lanzarDado():
    n = random.randint(1, 6)
    print('Numero generado: ', n)
    return n

#Porgrama principal
saludo()
r = input('Deseas lanzar un dado?: ').upper()
if r == 'SI':
    num = lanzarDado()
    print('Dado: ',num)
    if num == 6:
        print('Felicidades, Usted ha ganadoS/. 5.00')
    else:
        print('No ha ganado ningun premio')

else:
    print('Para la proxima sera')