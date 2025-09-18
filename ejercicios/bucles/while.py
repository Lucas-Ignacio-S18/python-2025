# Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
# num = 0
# while num <= 10:
#     print(num)
#     num += 1

# Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
# num = 10
# while num >= 1:
#     print(num)
#     num -= 1

# Mostrar la suma de los números desde el 1 hasta el 10.
# num = 1
# acumulador = 0

# while acumulador <= 9:
#     print(f"El numero es {num}")
#     num += 1
#     acumulador += 1
#     resultado = acumulador + num
#     print(f"{acumulador} + {num} = {resultado}")
    
    

# Mostrar la suma de los números pares desde el 1 hasta el 10.
# num = 0
# while num < 11:
#     num += 1
#     if num % 2 == 0:
#         print(num)

# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.
# num = 0
# acumulador = 0
# contador = 0

# while contador < 5:
#     num = int(input("Ingrese un numero: "))
#     acumulador  += num
#     contador += 1
#     resultado = acumulador / 5
# print(int(resultado))


# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

# num = 0
# acumulador = 0
# contador = 0
# consulta = input("Quiere empezar? si/no: ")
# while consulta == "si":
#     num = int(input("Ingrese un numero: "))
#     acumulador += num
#     contador += 1
#     resultado = int (acumulador / contador)
#     consulta = input("Queres ingresar otro numero? si/no: ")
# print(f"El total es {acumulador}")
# print(f"El pormedio de {acumulador} / {contador} = {resultado}")


# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

# num = 0
# acumulador_pos = 0
# acumulador_neg = -1
# consulta = input("Quiere empezar? si/no: ")
# while consulta == "si":
#     num = int(input("Ingrese un numero: "))
#     consulta = input("Queres ingresar otro numero? si/no: ")
#     if num > 0:
#         acumulador_pos += num
#     elif num < 0:
#         acumulador_neg *= num
# print(f"La suma de los positivos es: {acumulador_pos} y el producto de los negativos es: {acumulador_neg}")

# Ingresar 10 números enteros. Determinar el máximo y el mínimo.

num = int(input("Ingrese un numero: "))
contador = 0

while contador < 10:
    num = int(input("otro numero: "))
    contador += 1
    print(f"{contador}. {num}")
    

# Anexo:
# Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.
# Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

# Integrador While
# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.