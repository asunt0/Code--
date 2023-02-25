


frutas = ["banana", "pera", "manzana", "granada", "naranja", "durazno", "mandarina"]
numeros = [4, 5, 6, 7]

#evitando que se coma una banana con la sentencia continue
for fruta in frutas:
    if fruta == "banana":
        continue
    print(f'Me voy a comer una {fruta}')
    
#evitar que el bucle se siga ejecutando
for fruta in frutas:
    if fruta == "granada":
        break
    print(f'Me voy a comer una {fruta}')

else:
    print("bucle terminado")  #el else no se ejecuta por el break
    
    
#iterar una cadena
saludo = "Hola Sebastian"
for letra in saludo:
    print(letra)
    
#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros ]
print(numeros_duplicados)