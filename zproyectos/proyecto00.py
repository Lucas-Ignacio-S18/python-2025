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
#1.Crea una lista vacía y permite que el usuario agregue elementos hasta que escriba "fin".
def list_neu():
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

#2.Elimina el último elemento de una lista con pop().
    lista_new.pop(-1)
    print(lista_new)
#list_neu()

#3.Ordena una lista de números de menor a mayor (sort()).
def list_nums():
    lista_num = [23,12,56,40,8,-3]
    print(lista_num)

    lista_num.sort()
    print(lista_num)

    #4.Invierte el orden de una lista (reverse()).
    lista_num.reverse()
    print(lista_num)

    #5.Une dos listas con el operador +.
    lista_num02 = ["a","b","c","d"]

    listas_unidas = [lista_num + lista_num02]
    print(listas_unidas)
#list_nums()

#? NIVEL 4 — Sublistas y slicing

#1.Crea una lista de 10 números y muestra solo los 5 primeros.
def sublist():
    lista_diez = [18,40,5,41,6,10,35,50,10,92]
    print(lista_diez[0:5])
    
#2.Muestra los elementos desde el índice 2 hasta el 6.
    print(lista_diez[2:6])

#3.Muestra los últimos 3 elementos de una lista.
    print(lista_diez[-3:])

#4.Crea una copia de una lista usando [:].

#5.Muestra la lista original y la copia para verificar que son listas diferentes.
sublist()




#?NIVEL 5 — Ejercicios con lógica

#1.Pide al usuario 5 números, guárdalos en una lista y muestra el mayor y el menor.

#2.Crea una lista con 10 números y muestra solo los que son múltiplos de 3.

#3.Pide una palabra y guarda cada letra en una lista.

#4.Une una lista de palabras en una sola cadena de texto (join()).

#5.Elimina los elementos repetidos de una lista (pista: set() o bucle).