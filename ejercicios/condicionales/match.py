# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche.

estacion = input("Ingrese en que estacion quiere viajar: ")

match estacion:
    
    case "invierno":
        print("solo se viaja a Bariloche")
    case "verano":
        print("se viaja a Mar del plata y Cataratas")
    case "otoño":
        print("se viaja a todos los lugares")
    case "primavera":
        print("se viaja a todos los lugares menos Bariloche.")
    case _:
        print("Respuesta incorrecta")