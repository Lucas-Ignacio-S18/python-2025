from colorama import Style,Fore
import random
# Nivel básico 

# Calculadora simple
# ➤ Pide dos números y una operación (+, -, *, /).
# ➤ Muestra el resultado.
# Prácticas: input(), if, operadores matemáticos.
# def calculadora():
#     while True:
#         operacion = input("""
# --Elija la operación que desea realizar--
# 1.Suma
# 2.Resta
# 3.Multiplicación
# 4.División
# Elija su operación: """).lower()
#         match operacion:
#             case "1" | "suma" | "sumar":
#                 num1 = int(input("Ingrese el primer número: "))
#                 num2 = int(input("Ingrese el segundo número: "))
#                 resultado = num1 + num2
#                 print(f"El resultado de la suma es: {resultado}")

#             case "2" | "resta" | "restar":
#                 num1 = int(input("Ingrese el primer número: "))
#                 num2 = int(input("Ingrese el segundo número: "))
#                 resultado = num1 - num2
#                 print(f"El resultado de la resta es: {resultado}")

#             case "3" | "multiplicacion" | "*" | "multiplicar":
#                 num1 = int(input("Ingrese el primer número: "))
#                 num2 = int(input("Ingrese el segundo número: "))
#                 resultado = num1 * num2
#                 print(f"El resultado de la multiplicación es: {resultado}")

#             case "4" | "division" | "/" | "dividir":
#                 num1 = int(input("Ingrese el primer número: "))
#                 num2 = int(input("Ingrese el segundo número: "))
#                 if num1 == 0 or num2 == 0:
#                     print(Fore.RED + "No se puede dividir por cero."+ Style.RESET_ALL)
#                     continue

#                 resultado = num1 / num2
#                 print(f"El resultado de la división es: {resultado:.1f}")

#             case _:
#                 print(Fore.RED + f"⚠️ Operacion no detectada ⚠️" + Style.RESET_ALL)
#                 continue

#         salida = input("Quiere terminar de hacer opeaciones? (S/N)").lower()
#         if salida != "s":
#             break

#     print(Fore.GREEN + "Gracias por utilizar al Sr.Calculadora" + Style.RESET_ALL)

# calculadora()


# Adivina el número
# ➤ La computadora elige un número aleatorio entre 1 y 100.
# ➤ El jugador tiene que adivinarlo.
# Prácticas: random, while, condiciones.

def ramdon():
    numero_sel = int(input("Adivina el número: "))
    numero_random = random.randint(1, 10)

    while numero_sel != numero_random:
        print(Fore.RED + f"❌ El número seleccionado no es correcto❌ el correcto era {numero_random}" + Style.RESET_ALL)
        #Reiniciamos el número aleatorio
        numero_random = random.randint(1, 10)
        numero_sel = int(input("Adivina el número: "))
        continue
    print(Fore.GREEN + f"✅ Felicitaciones! El número {numero_sel} era el correcto!✅" + Style.RESET_ALL)
    return numero_random
ramdon()


# Contador de vocales
# ➤ Pedís una frase y contás cuántas vocales tiene.
# Prácticas: cadenas, bucles, condicionales.

# Conversor de temperatura
# ➤ Convierte entre Celsius, Fahrenheit y Kelvin.
# Prácticas: funciones, operadores, input.

# Par o impar
# ➤ Pide un número y dice si es par o impar.
# Prácticas: operadores %, condicionales.