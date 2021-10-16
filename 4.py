# Ejercicio funciones 2
import random
def generarNotas():
    lista = []
    for i in range(5):
        n = random.randint(0, 20)
        lista.append(n)
    return lista

def promedio(x): #x es el argumento para pasar la lista de notas
    p = sum(x) / len(x)
    return p

def condicion(p): #p es el argumento para pasar el promedio
    if p >= 12.5:
        c = 'Aprobado'
    else:
        c = 'Desaprobado'

    return c

# Programa principal
notas = generarNotas()
prom = promedio(notas)
cond = condicion(prom)
print('Notas: ', notas)
print('Promedio: ', prom)
print('Condicion: ', cond)