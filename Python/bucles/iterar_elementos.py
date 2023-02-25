


animales = ["perro", 'gato', 'loro', 'cocodrilo']
numeros = [10, 4, 6, 7]

#recomiendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a : {animal}')

#recomiendo la lista de numeros y multiplicando cada uno por 2
for numero in numeros:
    resultado = numero * 2
    print(resultado)
    
#iterando 2 listas
for numero, animal in zip(animales, numeros):
    print(f"recorriendo lista 1 {numero}")
    print(f"recorriendo lista 2 {animal}")
    
#range
for num in range(50, 55):
    print(num)

#forma correcta de recorrer una lista por su indice
for num in enumerate(numeros):
    print(num)
    
numero1, numero2, numero3, numero4 = numeros
print(numero3)

#asddja
for num in (numeros):
    print(f"ejecutando el ultimo valor actual : {num}")
else:
    print("el bucle termino")
    
#todo lo anterior funciona exactamente igual para tuplas y conjuntos