import csv

lista_equipos = [
    {"id":1, "nombre":"Super Compu","categoria":"notebook", "estado": "funcional", "valor": 500},
    {"id":2, "nombre":"Mega Compu","categoria":"notebook", "estado": "funcional", "valor": 700},
    {"id":3, "nombre":"Ultra Compu","categoria":"notebook", "estado": "funcional", "valor": 1000}
]

with open("equipos.csv", "w", newline = "")as archivo: 
    writer = csv.DictWriter(archivo, fieldnames=["id","nombre","categoria","estado","valor"])

    writer.writeheader()
    for equipo in lista_equipos:
        writer.writerow(equipo)

with open("equipos.csv", "r") as archivo:
    reader = csv.DictReader(archivo)
    for linea in reader:
        print(linea)


