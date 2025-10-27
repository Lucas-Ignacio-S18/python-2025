import csv
import os
from colorama import Style,Fore

#? ---------- FUNCIONES AUXILIARES ----------

def validar_nota():  #pide una nota valida entre 0 y 10

    while True:
        try:
            nota = int(input("Ingrese la nota del estudiante (0-10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("❌ La nota debe estar entre 0 y 10.")
        except ValueError:
            print("❌ Debe ingresar un número entero válido.")

def cargar_desde_archivo(nombre_archivo): #carga los datos desde un archivo CSV si existe

    estudiantes = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, newline='', encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                estudiantes.append({
                    "nombre": fila["nombre"],
                    "nota": int(fila["nota"])
                })
    return estudiantes


def guardar_en_archivo(nombre_archivo, estudiantes): #guarda los datos en CSV
    with open(nombre_archivo, "w", newline='', encoding="utf-8") as archivo:
        campos = ["nombre", "nota"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for e in estudiantes:
            escritor.writerow(e)

#? ---------- FUNCIONES PRINCIPALES ----------

def cargar_estudiantes(nombre_archivo="alumnos.csv"):
    #! carga o agrega estudiantes segun el archivo existente

    estudiantes = []
    if os.path.exists(nombre_archivo):
        print("📂 Se detectó un archivo con información de alumnos.")
        opcion = input("¿Desea Reemplazar (R) o Agregar (A) nuevos registros?: ").strip().lower()
        if opcion == "a":
            estudiantes = cargar_desde_archivo(nombre_archivo)
        elif opcion != "r":
            print("Opción no válida. Se asumirá 'Reemplazar'.")

    cant_estudiantes = 0
    while True:
        try:
            cant_estudiantes = int(input("Ingrese la cantidad de estudiantes a cargar: "))
            if cant_estudiantes > 0:
                break
            else:
                print("Debe ingresar un número mayor a 0.")
        except ValueError:
            print("Ingrese un número válido.")

    for i in range(cant_estudiantes):
        print(f"\nEstudiante #{i+1}")
        nombre = input("Ingrese el nombre: ").strip()
        nota = validar_nota()
        estudiantes.append({"nombre": nombre, "nota": nota})

    guardar_en_archivo(nombre_archivo, estudiantes)
    print(f"\n✅ Se guardaron {len(estudiantes)} estudiantes en '{nombre_archivo}'.")
    return estudiantes

def mostrar_estudiantes(estudiantes):
    #!estudiantes y sus notas
    print("\n---- LISTADO DE ESTUDIANTES ----")
    for i in estudiantes:
        print(f"Nombre: {i['nombre']:} | Nota: {i['nota']}")
    print("-" * 32)


def buscar_estudiante(estudiantes):
    #! Busca un estudiante por nombre (sin importar mayúsculas). 
    nombre = input("Ingrese el nombre a buscar: ").strip().lower()
    encontrado = False
    for i in estudiantes:
        if i["nombre"].lower() == nombre:
            print(f"✅ {i['nombre']} tiene una nota de {i['nota']}.")
            encontrado = True
            break
    if not encontrado:
        print("❌ Estudiante no encontrado.")


def calcular_estadisticas(estudiantes):
    #!calcula promedio, aprobado, desaprobado, nota máx/mín.
    notas = [i["nota"] for i in estudiantes]
    promedio = sum(notas) / len(notas)
    aprobados = sum(1 for n in notas if n >= 6)
    desaprobados = len(notas) - aprobados
    max_nota = max(notas)
    min_nota = min(notas)

    print(Style.BRIGHT + "\n--- ESTADÍSTICAS DEL CURSO ---" + Style.RESET_ALL)
    print(f"Promedio general: {promedio:.2f}")
    print(Fore.LIGHTGREEN_EX + f"Aprobados: {aprobados}" + Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + f"Desaprobados: {desaprobados}" + Style.RESET_ALL)
    print(f"Nota más alta: {max_nota}")
    print(f"Nota más baja: {min_nota}")
    print("-" * 20)


def ordenar_estudiantes(estudiantes):
    #! ordena la lista de estudiantees

    while True:
        orden = input("¿Desea ordenar ASC o DESC?: ").strip().lower()
        if orden in ("asc", "desc"):
            break
        print("Ingrese 'ASC' o 'DESC'.")
    copia = estudiantes.copy()
    copia.sort(key=lambda e: e["nota"], reverse=(orden == "desc"))
    mostrar_estudiantes(copia)


def generar_informe(estudiantes):
    #! genera informe final en pantalla y archivo
    notas = [e["nota"] for e in estudiantes]
    promedio = sum(notas) / len(notas)
    aprobados = sum(1 for n in notas if n >= 6)
    desaprobados = len(notas) - aprobados
    mejor = max(estudiantes, key=lambda e: e["nota"])
    peor = min(estudiantes, key=lambda e: e["nota"])

    info = (
        "INFORME FINAL DEL CURSO\n"
        "-------------------------\n"
        f"Cantidad total de estudiantes: {len(estudiantes)}\n"
        f"Promedio general: {promedio:.2f}\n"
        f"Aprobados: {aprobados}\n"
        f"Desaprobados: {desaprobados}\n"
        f"Mejor nota: {mejor['nota']} (Alumno: {mejor['nombre']})\n"
        f"Peor nota: {peor['nota']} (Alumno: {peor['nombre']})\n"
        "-------------------------\n"
    )
    print("\n" + info)
    with open("informe.txt", "w", encoding="utf-8") as f:
        f.write(info)
    print("📄Informe guardado como 'informe.txt'.")


#! ---Función principal------

def menu():
    estudiantes = []
    archivo = "alumnos.csv"

    #carga automatica si existe el archivo
    if os.path.exists(archivo):
        estudiantes = cargar_desde_archivo(archivo)
        print(f"📁 Datos cargados automáticamente desde '{archivo}'.")

    while True:
        #Este es el menú, quedo feo... pero despues se imprime con colores :D
        print(Fore.CYAN + Style.BRIGHT + "\n========= MENÚ PRINCIPAL ========= " + Style.RESET_ALL + "\n1) Cargar datos de estudiantes\n2) Mostrar listado de estudiantes\n3) Buscar estudiante\n4) Calcular estadísticas\n5) Ordenar y mostrar\n6) Generar informe resumen\n7) Salir"+ Fore.CYAN + Style.BRIGHT +"\n==================================" + Style.RESET_ALL)
        
        opcion = input("Seleccione una opción: ").strip()
        match opcion:
            case "1":
                estudiantes = cargar_estudiantes(archivo)
            case "2" | "3" | "4" | "5" | "6":
                if not estudiantes:
                    print("⚠️ Primero debe cargar los datos de los estudiantes (opción 1).")
                    input("Presione ENTER para continuar...")
                    continue
                match opcion:
                    case "2":
                        mostrar_estudiantes(estudiantes)
                    case "3":
                        buscar_estudiante(estudiantes)
                    case "4":
                        calcular_estadisticas(estudiantes)
                    case "5":
                        ordenar_estudiantes(estudiantes)
                    case "6":
                        generar_informe(estudiantes)
            case "7":
                print("👋¡Gracias por usar el sistema de inscripción!👋")
                break
            case _:
                print("❌ Opción inválida. Reintente.")

# ------Salida-------
if __name__ == "__main__":
    menu()
