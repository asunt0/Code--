



import csv

with open('C:\\Users\\Asu\\Documents\\Code😎\\Python\\Archivos\\datos.csv') as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)