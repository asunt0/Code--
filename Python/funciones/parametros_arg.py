
# # #forma no optima
# # def suma(lista):
# #     numeros_sumados = 0
# #     for numero in lista:
# #         numeros_sumados = numeros_sumados + numero
# #     return numeros_sumados
    
# resultado2 = suma([3, 13, 543, 12])
# print(resultado2)

#utilizando el parametro args
def suma(*numeros):
    return sum(numeros)

resultado = suma(13,2,6,5,13)
print(resultado)
