# EJERCICIO LISTAS 1

#ingreso de datos
lista = []
for i in range(5):
    n = int(input('Ingrese la nota '+str(i+1)+': '))
    lista.append(n)
#operación
suma = 0
for nota in lista:
    suma += nota
minimo = 100
for nota in lista:
    if nota < minimo:
        minimo = nota
maximo = -1
for nota in lista:
    if nota > maximo:
        maximo = nota        
suma = suma - minimo - maximo
maximo += 2
if maximo > 20:
    maximo = 20
suma += maximo
p = suma / 4
#resultados
print('Notas:', lista)
print('Menor nota:', minimo)
print('Mayor nota:', maximo)
print('Promedio:', p)


#suma: la función sum(lista)
#máximo: la función max(lista)
#Mínimo: la función min(lista)