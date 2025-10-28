
mensaje_list = ["Hola","Chau", "Lista","juancito",1,True]
print(f"\nLista: {mensaje_list}")
print(len(mensaje_list))
print(len(mensaje_list[2]))

mensaje_diccionario = {"clave01":"Esta es la clave 01",
                        "clave02":"Esta es la clave 02"}
print(f"\nDiccionario: {mensaje_diccionario}")
print(f"key: clave02 | Date: {mensaje_diccionario["clave02"]}")


mensaje_tupla = ("Tupla","Ordenamiento","Nose",1,2,3,4)
print(f"\nTupla: {mensaje_tupla}")



print("\nDatos")
print(f"mensaje_list = {type(mensaje_list)}")
print(f"mensaje_diccionario = {type(mensaje_diccionario)}")
print(f"mensaje_tupla = {type(mensaje_tupla)}")

