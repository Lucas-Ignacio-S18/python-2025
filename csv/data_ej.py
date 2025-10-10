import csv

lista_equipos = [
    {"id",2,""}
]

with open("equipos.csv", "w", newline = "")as archivo: 
    writer = csv.DictWriter(archivo, fieldnames=["id","nombre","categoria","estado","valor"])

    writer.writeheader()
    writer.writerow()


