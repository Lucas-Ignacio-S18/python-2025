from colorama import init, Fore, Back, Style
import random
#! ESTO ES PARA PROBAR COSAS NOMAS

init()

def main():
#Fore.Color = Color de la letra
    print(Fore.GREEN + "Bienvenido al tutorial interactivo de colorama \n" + Style.RESET_ALL)

    colores = [Fore.CYAN,Fore.WHITE, Fore.YELLOW, Fore.MAGENTA, Fore.RED]
    for color in colores:
        print(color + f"Nuevo colores" + Style.RESET_ALL)

    print("\nFondo de color")
#Back.Color = Color del fondo
    background = [Back.GREEN, Back.BLUE, Back.LIGHTBLUE_EX, Back.LIGHTBLACK_EX]
    for fondo in background:
        print(fondo + f"Los colores de fondo" + Style.RESET_ALL)

    print("\nStyle: estilos de tipografia")
    print(Style.NORMAL + "Style.NORMAL: Texto normal")
    print(Style.DIM + "Style.DIM: Texto Dim, trasparente")
    print(Style.BRIGHT + "Style.BRIGHT: Texto Bright, mas negro")
    print(Style.RESET_ALL + "Style.RESET_ALL: Reinicia los estilos")

    print("\nMensaje:\n" + Fore.LIGHTWHITE_EX + Back.LIGHTBLUE_EX + Style.BRIGHT +"Racing Club de Avellaneda" + Style.RESET_ALL)

main()


print("Diccionario")
diccionario = {"saludo": "Hola", "despedida":"Chau"}
diccionario[2] = "dos"
#diccionario["nombre_pj"] = input("Ingrese su nombre: ")
#print(Fore.LIGHTGREEN_EX + Style.BRIGHT + diccionario["nombre_pj"] + Style.RESET_ALL)
#print(diccionario)
#?------
# print("\nDiccionario2")
# diccionario2 = {"nombre":Fore.LIGHTCYAN_EX + input("Ingrese su nombre: " + Style.RESET_ALL),
#                 "apellido":Fore.GREEN + input("Ingrese su apellido: ") + Style.RESET_ALL}

# print(diccionario2["nombre"])
# print(diccionario2["apellido"])
#?------
# personaje = {
#     "pj1":{"nombre":input("Ingrese su nombre: "),"color":Fore.LIGHTGREEN_EX,"ataque":int(input("Ingrese su daño de ataque: "))},
#     "pj2":{"nombre":input("Ingrese su nombre: "),"color":Fore.LIGHTGREEN_EX,"ataque":int(input("Ingrese su daño de ataque: "))}
# }
# for clave, pj in personaje.items():
#     print(pj["color"] + pj["nombre"] + Style.RESET_ALL + f" tiene {pj['ataque']} de ataque")
#     #print(pj["nombre"] + f" tiene {pj["ataque"]} de ataque")

# colores = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW]
# personaje = {}
#?------
# for i in range(3):
#     nombre = input(f"Ingrese el nombre {i+1}: ")
#     color = random.choice(colores)
#     personaje[nombre] = {"nombre":nombre, "color":color, "ataque":random.randint(5,500)}

# print("\n=== Lista de personajes ===")
# for pj in personaje.values():
#     print(pj["color"] + f"{pj["nombre"]} - Ataque: {pj["ataque"]}" + Style.RESET_ALL)

#!Colores por tipo:
colores_por_tipo ={
    "guerrero":Fore.RED,
    "mago":Fore.MAGENTA,
    "arquero":Fore.GREEN,
    "vanguardia":Fore.LIGHTRED_EX,
    "sanador":Fore.CYAN
}

#? Si el pj es lvl +50 y tiene mas de 250 de daño, que se lo catalogue como "clase superior"
#? En caso que sea +50 pero no supere los 250 de daño entonces que sea "clase mayor"
#? sino que sea "clase comun"

personaje = {}
for i in range(3):
    nombre = input(f"Ingrese su nombre: ") + Style.BRIGHT
    tipo = input(f"Ingrese su clase(vanguardia/guerrero/mago/arquero/sanador): ").lower()
    color = colores_por_tipo.get(tipo, Fore.WHITE)
    ataque = random.randint(5,500)
    nivel_num = random.randint(1,100)

    if nivel_num > 50 and ataque > 250:
        clase = Fore.RED + "Superior" + Style.RESET_ALL
    elif nivel_num > 50 and ataque < 250:
        clase = Fore.LIGHTYELLOW_EX + "Mayor" + Style.RESET_ALL
    elif nivel_num < 50 and ataque > 250:
        clase = Fore.LIGHTMAGENTA_EX + "Prodigio" + Style.RESET_ALL
    else:
        clase = Fore.WHITE + Style.DIM + "Comun" + Style.RESET_ALL

# -- Cargar personajes dentro del bucle for()
    personaje[nombre] = {
                            "nombre":nombre, 
                            "tipo":tipo,
                            "color":color,
                            "ataque":ataque, 
                            "nivel":nivel_num,
                            "clase":clase
                            }

print("\n===== Lista de personajes =====")
for pj in personaje.values():
    #print(pj["color"] + f"{pj["nombre"]} - Clase({pj["tipo"]}) {Style.RESET_ALL} - Ataque: {pj["ataque"]}")
    print(f"{Style.BRIGHT} {pj["nombre"]}{Style.RESET_ALL} - lvl.({pj["nivel"]}) - {Style.RESET_ALL}{pj["color"]}({pj["tipo"]}){Style.RESET_ALL} - Ataque: {pj["ataque"]} - Rango: {pj["clase"]}")
    