
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#CREANDO una funcion lambda
multiplicar = lambda x: x*2

# #creando una funcion comun q diga si es par o no
# def es_par(num):
#     if (num % 2 == 0) :
#         return True

# #USANDO FILTER CON UNA FUNCION COMUN
# numeros_pares = filter(es_par, numeros)

#creando lo mismo q antes pero en lambda
numeros_pares = filter(lambda numero: numero % 2 == 0, numeros)
#filter lo que hace es iterar cada elemento de la lista osea pasa primero por 1 y asi


print(multiplicar(6))
print(list(numeros_pares))
