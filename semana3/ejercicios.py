"""
Nivel Básico
1. Función que saluda a una persona

Enunciado:
Escribí una función que reciba un nombre y muestre un saludo personalizado.
""" 

# def saludo(nombre):
#     print("Hola " + nombre)

# nombre = str(input("tu nombre: "))
# saludo(nombre)

"""
Enunciado:
Escribí una función que reciba base y altura, y devuelva el área.
Datos por consola un argumento por defecto =10
"""

# def area(base = 10 , altura = 10):
#     area = base * altura
#     return area

# base = float(input("Ingrese la base: "))
# altura = float(input("Ingrese la altura: "))

# print(f"El area es: {area(base, altura)}")

"""Nivel Intermedio
Función que devuelva suma, resta y multiplicación

Enunciado:
Escribí una función que reciba dos números y devuelva los tres resultados: suma, resta y multiplicación."""

# def cuentas(num1, num2):
#     suma = num1 + num2
#     print(f"La suma es {suma}")

#     resta = num1 - num2
#     print(f"La resta es {resta}")

#     multiplicacion = num1 * num2
#     print(f"La multiplicacion es {multiplicacion}")

# num1 = int(input("Ingrese el primer numero: "))
# num2 = int(input("ingrese el segundo numero: "))

# cuentas(num1, num2)
"""
    Enunciado:
Escribí una función que reciba cualquier cantidad de números y los multiplique los parametros por consola.

Ayuda: pedir al usuario cuantos numeros cargar, luego usar ese valor para iterar
"""

def cantidad_de_numeros():
    acumulador = 1
    contador = int(input("Ingrese la cantidad de numeros que quiera ingresar: "))

    for x in range(contador):
        numero = int(input(f"Ingrese un numero: "))
        acumulador *= numero
    
    return acumulador

print(cantidad_de_numeros())
