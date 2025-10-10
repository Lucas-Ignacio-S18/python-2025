# # Práctica
# #  1
# #  para
# #  el

# # parcial

# # Misión

# # Van a desarrollar un sistema en Python que 
# # gestione un inventario de equipos 
# # tecnológicos (notebooks, routers, 
# # impresoras, etc.) para un pequeño 
# # laboratorio de redes. 
# # El sistema trabajará con un archivo 
# # equipos.csv que se genera o actualiza según 
# # las acciones del usuario. 
# # Condiciones

# # • Usar funciones para cada opción del 
# # menú. 
# # • Validar todas las entradas. 
# # • No permitir usar las opciones 2–7 sin 
# # haber cargado o leído el archivo primero. 
# # • Usar estructuras adecuadas (listas y 
# # diccionarios). 
# # • Guardar y leer CSV con csv.DictReader / 
# # csv.DictWriter. 
# # Pasos
# #  iniciales

# # Crear archivos para funciones y 
# # validaciones → Hacer la función menú → 
# # Hacer la opción 1 del menú → ... 
# # Menú
# #  del
# #  programa

# # ¿Cómo lo harías? 
# # def menu(): 
# # vlOpcionUno = False 
# # print(""" 
# # ========= MENÚ INVENTARIO ========= 
# # 1. Cargar equipos 
# # 2. Mostrar inventario 
# # 3. Buscar equipo 
# # 4. Estadísticas 
# # 5. Filtrar por categoría 
# # 6. Ordenar por valor 
# # 7. Generar informe 
# # 8. Salir 
# # """) 
# # libreria =  
# # opcion = input(“Elija una opción ”) 
# # if opcion == "1": 
# # #libreria = cargar_equipos() 
# # if opcion == “2”: 
# # vl_OpcionUno(libreria) 
# # # mostrar inventario() 
# # # def vl_OpcionUno(libreria): 
# # # Asi? y que como parametro tenga si hay algo en la libreria 
# # if len(libreria) == 0: 
# # print(“No hay equipos cargados”) 
# # else: 
# # continue 
# # #con un if?, haces que si hay algo en la libreria avance el 
# # programa, y que si no hay nada que devuelve un print que diga “No 
# # hay equipos cargados” (soy joako), claro, exactamente eso 
# # Opción
# #  1.
# #  Cargar
# #  equipos

# # Permitir ingresar N equipos (cantidad 
# # pedida al usuario). 
# # Cada equipo se representa con un 
# # diccionario con las claves: 
# # ○ "id" (entero autoincremental), 
# # ○ "nombre", 
# # ○ "categoría" (router, pc, notebook, 
# # impresora), 
# # ○ "estado" (funcional o fuera de 
# # servicio), 
# # ○ "valor" (float, validado como número 
# # positivo). 
# # Los datos se guardan en una lista y 
# # también en el archivo equipos.csv
# #  . 
# # Si el archivo ya existe, preguntar: 
# # ○ “¿Desea reemplazar los datos 
# # existentes o agregar nuevos equipos?” 
# # def cargar_equipos(): 
# # n_equipos = int(input("Cantidad de equipos a ingresar: ")) 
# # for i in range(n_equipos): 
# # # ni idea 
# # Opción
# #  2.
# #  Mostrar
# #  inventario

# # Mostrar todos los equipos cargados con 
# # formato: 
# # ID: 1 | Nombre: Router A | Estado: funcional | Valor: 350.50 
# # Separar visualmente con líneas. 
# # def mostrar_inventario(): 
# # # acá el código 
# # Opción
# #  3.
# #  Buscar
# #  equipo

# # Buscar un equipo por nombre (ignorando 
# # mayúsculas/minúsculas). 
# # Mostrar si existe, y si existe, mostrar 
# # todos sus datos. 
# # def buscar_equipo(): 
# # # acá el código 
# # Opción
# #  4.
# #  Estadísticas

# # ● Calcular y mostrar: 
# # Cantidad total de equipos. 
# # Promedio general de valores. 
# # Cantidad de equipos “fuera de 
# # servicio”. 
# # Equipo más caro y más barato (nombre 
# # y valor). 
# # def mostrar_estadisticas(): 
# # # posibles funciones ↓ 
# # calcular_total() 
# # calcular_promedio_valores() 
# # calcular_cantidad_fds() 
# # calcular_mayor_menor() 
# # Opción
# #  5.
# #  Filtrar
# #  por
# #  categoría

# # Solicitar una categoría (ej: “router”) y 
# # mostrar solo los equipos de ese tipo. 
# # Si no hay coincidencias, informar. 
# # def filtrar_categorias(): 
# # # acá el código 

# # Opción
# #  6.
# #  Ordenar
# #  por
# #  valor

# #  Pedir criterio de ordenamiento (ASC o 
# # DESC) y mostrar la lista ordenada
# #  por

# # valor
# #  sin alterar la original. 
# def ordenar_lista_valores(): 
#     criterio = input("Ordenar por valor (ASC/DESC): ") 
#     lista = equipos 
#     n = len(lista) 
#     if criterio == "ASC": 
#         for i in range(n): 
#                     for j in range(n - i): 
#                         if lista[j]["valor"] > lista[j + 1]["valor"]:   
#                             aux = lista[j] 
#                             lista[j] = lista[j + 1] 
#                             lista[j + 1] = aux 
#     print("\nInventario ordenado ascendente:\n") 

#     elif criterio == "DES": 
#     for i in range(n - 1): 
#         for j in range(n - i - 1): 
#             if lista[j]["valor"] < lista[j + 1]["valor"]: 
#                         lista[j], lista[j + 1] = lista[j + 1], lista[j] 
#             print("\nInventario ordenado descendente:\n") 

#     else: 
#     print("Entrada inválida. Debe escribir ASC o DESC.") 

#     for equipo in lista: 
#         print(f"{equipo['id']} | {equipo['nombre']} | Valor: 
#         #${equipo['valor']}") 



# # Opción
# #  7.
# #  Generar
# #  informe

# # Crear un archivo informe_inventario.txt. 
# # Mostrarlo por pantalla. 
# # Formato del informe: 
# # INFORME GENERAL DE INVENTARIO ----------------------------- 
# # Equipos totales: XX 
# # Promedio de valor: XX.XX 
# # Fuera de servicio: XX 
# # Más caro: X (Nombre: XXX) 
# # Más barato: X (Nombre: XXX) ----------------------------- 
# # def generar_informe(): 
# # # acá el código 
# # Opción
# #  8.
# #  Salir

# # Mostrar mensaje de despedida. 
# # Guardar automáticamente los cambios 
# # antes de salir. 
# # def salir(): 
# # print(“Gracias por usar el mejor sistema del mundo ;)”) 
# # acá el código