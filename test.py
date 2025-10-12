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

# print("\nDiccionario2")
# diccionario2 = {"nombre":Fore.LIGHTCYAN_EX + input("Ingrese su nombre: " + Style.RESET_ALL),
#                 "apellido":Fore.GREEN + input("Ingrese su apellido: ") + Style.RESET_ALL}

# print(diccionario2["nombre"])
# print(diccionario2["apellido"])

personaje = {
    "pj1":{"nombre":input("Ingrese su nombre: "),"color":Fore.LIGHTGREEN_EX,"ataque":int(input("Ingrese su daño de ataque: "))},
    "pj2":{"nombre":input("Ingrese su nombre: "),"color":Fore.LIGHTGREEN_EX,"ataque":int(input("Ingrese su daño de ataque: "))}
}
for clave, pj in personaje.items():
    print(pj["color"] + pj["nombre"] + Style.RESET_ALL + f" tiene {pj['ataque']} de ataque")
    #print(pj["nombre"] + f" tiene {pj["ataque"]} de ataque")