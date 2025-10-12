from colorama import init, Fore, Back, Style
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