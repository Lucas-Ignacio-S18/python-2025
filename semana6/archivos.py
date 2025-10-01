
#primer archivo y guardar cadenas

# archivo = open ("archivo.txt", "w")
# archivo.write("Primer linea de texto\n")
# archivo.write("Segunda linea de texto\n")
# archivo.write("Tercer linea de texto\n")
# archivo.close()

# archivo = open("archivo.txt", "r+")
# texto = archivo.read()
# print(f"El archivo es: {texto}")
# archivo.close()

# archivo = open("archivo1.txt","r+", encoding='utf-8')
# lista_lineas = archivo.readline()
# for linea in lista_lineas:
#     print(linea)
# archivo.close()

#escribir vsv
# nombre_columnas = ["Nombre", "Edad", "Ciudad"]
# matriz = [["Juan", 28, "Madrid"], ["Ana", 22, "Barcelona"], ["Loan", 8, "Corrientes"]]
# with open("personas.csv", "w", encoding="utf-8-sig") as archivo:
#     archivo.write(",".join(nombre_columnas) + "\n")

#     for fila in matriz:
#         linea = ""
#         for i in range(len(fila)):
#             linea += str(fila[i])
#             if i < len(fila) - 1:
#                 linea += ","
#         archivo.write(linea + "\n")

#JSON
import json

with open("datos.json"):
    pass
