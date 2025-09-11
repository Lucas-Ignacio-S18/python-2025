# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

#entrada
altura = int(input("Ingrese la altura del jugador: "))

if altura >= 200:
    print(f"El jugador mide {altura}cm y juega de PIVOT")
elif altura <= 199 and altura >= 180: 
    print(f"El jugador mide {altura}cm y juega de ALERO")
elif altura <= 179 and altura >= 160: 
    print(f"El jugador mide {altura}cm y juega de ESCOLTA")
else:
    print(f"El jugador mide {altura}cm y juega de BASE")