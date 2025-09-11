import math

# #1.Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
# def numero_entero(num_entero = int(input("Ingrese un numero entero: "))):
#     return num_entero
# #num_entero = int(input("Ingrese un numero entero: "))
# print(numero_entero())

# print("------------------------------")

# # 2.Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
# def numero_flotante(num_float = float(input("Ingresse un numero flotante: "))):
#     return num_float    
# print(numero_flotante())

# print("------------------------------")

# # 3.Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 
# def string(cadena = input("Ingresse un string: ")):
#     return cadena    
# print(string())

# print("------------------------------")

# # 4.Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 
# def rectangulo(base = int(input("Ingrese la base: ")),altura = int(input("Ingrese la altura: "))):
#     area = base * altura
#     return area
# # base = int(input("Ingrese la base: "))
# # altura = int(input("Ingrese la altura: "))
# print(rectangulo())

# print("------------------------------")

# # 5.Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
# def circulo(radio = int(input("Ingrese el area: "))):
#     return math.pi * (radio ** 2)

# print(circulo())

# # print("------------------------------")

# # 6.Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
# def verif_par_impar(num = int(input("Ingrese un numero: "))):
#     if num % 2 == 0:
#         return f"El numero {num} es par"
#     else:
#         return f"El numero {num} es impar"

# print(verif_par_impar())

# # 7.Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

# def verif_true_false(num = int(input("Ingrese un numero: "))):
#     if num % 2 == 0:
#         num = True
#         return num
#     else:
#         num = False
#         return num
# print(verif_true_false())


# 8.Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

# def numero_mas_grande(a = int((input("Ingres el primer numero: "))), b = int(input("Ingrese el segundo numero: ")), c = int(input(" Ingrese el tercer numero: "))):
#     if a >= b and a >= c:
#         return f"El numero mas grande es el primero {a}"
#     elif b >= a and b >= c:
#         return f"El numero mas grande es el segundo {b}"
#     else:
#         return f"El numero mas grande es el tercero {c}"
# print(numero_mas_grande())
    


## 9.Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
#def potenciador(base = int(input("Base: ")) ,exponente = int(input("Exponente: "))):
# def potenciador(base,exponente):
#         print(f"la base es: {base}")
#         print(f"el exponente es: {exponente}")
#         potencia = base ** exponente
#         return f"({base})^{exponente} = {potencia}"
# base = int(input("Base: "))#
# exponente = int(input("Exponente: "))#
# print(potenciador(base, exponente))

# 10.Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
def numeros_primos(numeros_primos = int(input("Ingrese un numero: "))):
    for i in range(2, int(numeros_primos ** 0.5) + 1):
        if numeros_primos % i == 0:
            return False
    return True
print(numeros_primos())

# 11.Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.
def a():
    pass


# 12.Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.
def tabla(base):
    pass


# 13.Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
def a():
    pass

