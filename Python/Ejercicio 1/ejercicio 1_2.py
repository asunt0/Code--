


frase = input('Dime una frase y te calculo cuanto tardarias diciendo algo: ')

palabras_separadas = frase.split(" ") #porque espacio porque los espacios nos dicen cuando termina una palabra.

cantidad_de_palabras = len(palabras_separadas)

print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras / 2} segundos en decirlo")

print(f"Dalto tardaria {cantidad_de_palabras /  1.3} en decirlo jaja")

if cantidad_de_palabras > 20:
    print("para flaco tampoco te pedi un testamento")
else:
    print("bien flaco recuerda q no mas de 20 palabras :D")
    

