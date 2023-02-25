

#abriendo  el archivo con with open
with open('C:\\Users\\Asu\\Documents\\Code😎\\Python\\Archivos\\Texto.txt') as archivo:
    
    #leyendo el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)
    
#no es necesario cerrarlo con with open