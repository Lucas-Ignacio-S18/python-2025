#Ejemplos sencillos para practicar
#Crea una lista con numeros del 1 al 5, agrega el 6 y luego elimina el 2.
lista_num = [1,2,3,4,5]
print("Lista original: ", lista_num)
lista_num.append(6)
print("Append 6: ", lista_num)
lista_num.remove(2)
print("Remove 2: ", lista_num)
print("--"*20)

#Crea una lista con nombres de tus amigos y ordenla alfabeticamente
lista_amigos = ["Marco","Nicolas","Agustin","Juan","Diego"]
print("Lista de amigos: ", lista_amigos)
lista_amigos.sort()
print("Lista de amigos ordenada: ", lista_amigos)
print("--"*20)

# contar cuantas veces aparece el numero 3 en una lista
lista_alterada = [4,3,2,3,8,5,1,6,3,6,3,1,9,10,3,7,5,3]
print(f"el numero 3 aparece: {lista_alterada.count(3)} veces" )
print("--"*20)

# invertir una lista de frutas.
lista_frutas = ["manzanas","duraznos","naranjas","kiwis","bananas","cocos"]
print(lista_frutas)
lista_frutas.reverse()
print(lista_frutas)
print("--"*20)

#Hacer la suma de todos los numeros de una lista
lista_suma = [2,5,2,10,20,5]
print(lista_suma)
print(sum(lista_suma))
print("--"*20)


mi_lista = [1, 3, 5, 7, 9, 11, 13, 40, 39, 73, 115]
buscar = 40
#  1 -Búsqueda lineal (el más simple)

#  2 -Buscar el índice de un valor

#  3 -Búsqueda binaria (requiere lista ordenada)
