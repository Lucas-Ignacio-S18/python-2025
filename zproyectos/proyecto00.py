from colorama import Fore,Style,Back
import random
# mensaje_list = ["Hola","Chau", "Lista","juancito",1,True]
# print(f"\nLista: {mensaje_list}")
# print(len(mensaje_list))
# print(len(mensaje_list[2]))

# mensaje_diccionario = {"clave01":"Esta es la clave 01",
#                         "clave02":"Esta es la clave 02"}
# print(f"\nDiccionario: {mensaje_diccionario}")
# print(f"key: clave02 | Date: {mensaje_diccionario["clave02"]}")


# mensaje_tupla = ("Tupla","Ordenamiento","Nose",1,2,3,4)
# print(f"\nTupla: {mensaje_tupla}")



# print("\nDatos")
# print(f"mensaje_list = {type(mensaje_list)}")
# print(f"mensaje_diccionario = {type(mensaje_diccionario)}")
# print(f"mensaje_tupla = {type(mensaje_tupla)}")


#? NIVEL 1 — Básico (crear y acceder)
# Crea una lista con 5 nombres y muestra el primer y el último nombre.
# Crea una lista con 5 números y muestra el segundo elemento.
# Usa len() para mostrar cuántos elementos tiene una lista.
# Cambia el valor del tercer elemento de una lista por otro diferente.
# Agrega un nuevo elemento al final de una lista con append().

# lista_nombres = ["Lucas","Juan","Mateo","Draco","Nahi"]
# print(lista_nombres[0::4])

# lista_num = [18,22,10,15,8]
# print(lista_num[1])

# print(len(lista_nombres))

# lista_nombres[3] = "Martin"
# print(lista_nombres)
# lista_nombres.append("Lautaro")
# print(lista_nombres)


#? NIVEL 2 — Recorrer listas

# Crea una lista con 10 números y muestra cada número con un for.
# Suma todos los números de una lista usando un bucle.
# Muestra solo los números pares de una lista.
#! Crea una lista de nombres y muestra los que empiezan con la letra “A”.
# Cuenta cuántas veces aparece un número dentro de una lista (count()).

# lista_num = [1,2,3,4,5,6,7,8,9,10]
# for i in lista_num:
#     print(i)

# print("")
# print(sum(lista_num))

# print("")
# for i in lista_num:
#     if i % 2 == 0:
#         print(i)

# print("")
# lista_nombres = ["Abel","Coscu","Madax","Antonio","Alexis","Mariano","Alejo"]
# print(lista_nombres.index("Antonio")) #muestra posición| "Antonio" -> 3

# print("")
# lista_nume = [2,10,22,40,22,34,255,98,74,9,22,7,22,256,134,22]
# print(lista_nume.count(22))

#?NIVEL 3 — Modificar listas
# Crea una lista vacía y permite que el usuario agregue elementos hasta que escriba "fin".
# Elimina el último elemento de una lista con pop().
# Ordena una lista de números de menor a mayor (sort()).
# Invierte el orden de una lista (reverse()).
# Une dos listas con el operador +.

#1.
lista_new = []

elemnts = input("Quiere agregar un nuevo elemento? s/n: ").lower()

while True:
    match elemnts:
        case "si" | "s":
            new_elmt = input("Ingrese el elemento nuevo a la lista: ").lower()
            lista_new.append(new_elmt)
            print(lista_new)
            elemnts = input("Quiere agregar un nuevo elemento? s/n: ").lower()
        case "no" | "fin" | "n":
            print("Fin de la lista✅")
            break
        case _:
            print("❌Opcion invalida❌")
            elemnts = input("Quiere agregar un nuevo elemento? s/n: ").lower()
            continue
if lista_new == []:
    print("La lista esta vacia 🗑️")
else:
    print(f"La lista final: {lista_new}")

#2.

lista_new.pop(-1)
print(lista_new)

#3.
lista_num = [random.randint(10)]
print(lista_num)


