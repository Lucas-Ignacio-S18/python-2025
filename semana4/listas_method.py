#----------------------------------LISTAS----------------------------------#
print("\n")

mi_lista = ["a","b","c","d","e"]
print("Lista original: ", mi_lista)

print("\n")
##----------------------------------APPEND----------------------------------#
print("-"*25, "APPEND","-"*25 )

mi_lista.append("nuevo")
print("append: ", mi_lista)

print("\n")
##----------------------------------INSER----------------------------------#
print("-"*25, "INSERT","-"*25 )

mi_lista.insert(2,[1,2,3,["a","b"],5])
print("insert: ", mi_lista)

print("\n")
##----------------------------------EXTEND----------------------------------#
print("-"*25, "EXTEND","-"*25 )

mi_lista.extend([1,2,3,['a','b'],5])
print("extend: ", mi_lista)

print("\n")
##----------------------------------REMOVE----------------------------------#
print("-"*25, "REMOVE","-"*25 )
mi_lista.remove('a')
print("remove: ", mi_lista)

print("\n")
#----------------------------------POP----------------------------------#
print("-"*25, "POP","-"*25 )
mi_lista.pop(4)
print("pop: ", mi_lista)

print("\n")
#----------------------------------CLEAR----------------------------------#
print("-"*25, "CLEAR","-"*25 )
mi_lista.clear()
print("clear: ", mi_lista)


print("\n")
##----------------------------------ORDENAR Y REVERTIR----------------------------------#
print("-"*25, "Ordenar y revertir","-"*25 )
#! Ordenar y revertir
#sort() -> Ordena la lista de menor a mayor
#sort(reverse = True) -> Ordena de mayor a menor
#rever() -> Invierte el orden de los elementos
lista_numeros = [2,5,1,6,9,7]
print("lista numeros: ", lista_numeros)
lista_strings = ['d','a','v','k','e']
print("lista strings: ", lista_strings)
lista_numeros.sort()
lista_strings.sort()

#print("sorted list: ",sorted(['z','a','x','b']))
print("listas ordenadas")
print("sort numeros: ", lista_numeros)
print("sort strings: ", lista_strings)

print("\n")
##----------------------------------COPY----------------------------------#
print("-"*25, "COPY(Copiar lista)","-"*25 )
#! Copiar lista
#copy() -> devuelve una copia de la lista
copiado_list = []
print("copialo_list original: ", copiado_list)
copiado_list = lista_strings.copy

print("\n")
##----------------------------------SLICING----------------------------------#
print("-"*25, "SLICING(Rebanar)","-"*25 )
# [ INICIO : FINAL : PASO ]
#Slicing (rebanado) rapido
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros[2:6]) # [3,4,5,6] -> Desde el indice 2 hasta el 6
print(numeros[:5]) # [3,4,5,6] -> Desde el inicio hasta 5
print(numeros[::3]) # [3,4,5,6] -> de 3 en 3 [1,4,7]
print(numeros[::-2]) # [9,7,5,3,1] -> Invertida, va restando 2 en 2


# print("-"*50)
# palabras = ['javascript', 'java', 'c', 'go', 'python']
# ordenado_por_longitud = sorted(palabras, key=len)
# print(ordenado_por_longitud)  # ['c', 'go', 'java', 'python', 'javascript']