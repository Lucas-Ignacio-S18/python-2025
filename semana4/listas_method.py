#----------------------------------LISTAS----------------------------------#
mi_lista = ["a","b","c","d","e"]
print("Lista original: ", mi_lista)
print("-"*50)
##----------------------------------APPEND----------------------------------#
mi_lista.append("nuevo")
print("append: ", mi_lista)
print("-"*50)
##----------------------------------INSER----------------------------------#
mi_lista.insert(2,[1,2,3,["a","b"],5])
print("insert: ", mi_lista)
print("-"*50)
##----------------------------------EXTEND----------------------------------#
mi_lista.extend([1,2,3,['a','b'],5])
print("extend: ", mi_lista)
print("-"*50)
##----------------------------------REMOVE----------------------------------#
mi_lista.remove('a')
print("remove: ", mi_lista)
print("-"*50)
#----------------------------------POP----------------------------------#
mi_lista.pop(4)
print("pop: ", mi_lista)
print("-"*50)
#----------------------------------CLEAR----------------------------------#
mi_lista.clear()
print("clear: ", mi_lista)
print("-"*50)

#! Ordenar y revertir
#sort() -> Ordena la lista de menor a mayor
#sort(reverse = True) -> Ordena de mayor a menor
#rever() -> Invierte el orden de los elementos
lista_numeros = [2,5,1,6,9,7]
lista_strings = ['d','a','v','k','e']
lista_numeros.sort()
lista_strings.sort()

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