
#?🔹Nivel 1 (básicos)
# For - contar números pares
# Escribe un programa que muestre los números pares del 1 al 20.

# for i in range(21):
#     if i % 2 == 0:
#         print(i)

# While - pedir contraseña
# Pide al usuario una contraseña hasta que la escriba correctamente ("python123").

# contraseña = input("Ingrese la contraseña: ")
# while contraseña != "python123":
#     print("Error, reintentar")
#     contraseña = input("Ingrese la contraseña: ")    
# print("La contraseña se ingreso correctamente")


# If - positivo o negativo
# Pide un número al usuario e imprime si es positivo, negativo o cero.

# numero = int(input("Ingrese un numero: "))
# if numero > 0:
#     print(f"El numero {numero} es positvo")
# elif numero < 0:
#     print(f"El numero {numero} es negativo")
# else:
#     print("El numero es CERO")

#?🔹Nivel 2 (intermedios)

# For - suma de una lista
# Dada la lista [3, 7, 2, 9, 5], calcula la suma de todos sus elementos.
# mi_lista = [3, 7, 2, 9, 5]
# print(mi_lista)
# print(f"Esta es la suma de los indices de la lista: {sum(mi_lista)}")

# While - cuenta regresiva
# Pide un número al usuario y haz una cuenta regresiva hasta 0.

# numero = int(input("Ingrese un numero: "))
# print(f"El numero que elejiste fue {numero}")
# while numero != 0:
#     numero -= 1
#     print(f"El numero actual es: {numero}")
# print("Llegaste a CERO (0)")


# If con bucle - múltiplos de 3 y 5
# Recorre los números del 1 al 30.
numero = 0
while numero < 30:
    numero += 1
    if numero % 3 == 0 and numero % 5 == 0:
        print(f"{numero} - Fizz Buzz")
    elif numero % 3 == 0:
        print(f"{numero} - FIZZ")
    elif numero % 5 == 0:
        print(f"{numero} - BUZZ")
    else:
        print(f"{numero}")

# Si es múltiplo de 3 → imprime "Fizz".

# Si es múltiplo de 5 → imprime "Buzz".

# Si es múltiplo de ambos → imprime "FizzBuzz".

# Si no, imprime el número.


#? 🔹Nivel 3 (desafío)


# For y If - números primos
# Pide un número al usuario y muestra si es primo o no.

# While - menú interactivo
# Haz un programa que muestre este menú hasta que el usuario elija salir:
# For + If - tabla de multiplicar
# Pide un número y muestra su tabla de multiplicar del 1 al 10.