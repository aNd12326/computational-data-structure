# 2. Modifica el ejercicio anterior, de tal manera que ahora se solicite el 
# nombre del usuario, y se muestre como parte del saludo.

def saludar():
    nombre = input('Ingrese nombre de usuario: ').capitalize()
    print('Hola ', nombre)

saludar()
