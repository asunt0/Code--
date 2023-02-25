
#CREAR UNA LISTA CON LIST
new_list = list(["Hola", "como", "estas"])

#USANDO LEN PARA VER LA CANTIDAD DE ELEMENTOS DE UNA LISTA
resultado = len(new_list)

#agregando un elemento a una lista
new_list.append("tu")

#agregando elementos a una lista en un indice especificado
new_list.insert(1, "Sebastian")

#agregando varios elementos a una lista
new_list.extend(["que", "onda", 1])

#eliminando un elemento de una lista por su indice
new_list.pop(4) # (-1) para eliminar el ultimo (-2) para eliminar el penultimo y asi sucesivamente

#eliminando un elemento de una lista por su valor
new_list.remove("Sebastian")

#eliminando todos los elementos de la lista con clear
#new_list.clear()

#ordenando una lista de forma ascendente
new_list2 = list([10, 1, 3, 20, True])
new_list2.sort()

#inviertiendo una lista con reverse
new_list2.reverse()
print(new_list2)





#elimina todos los elementos de una lista
#new_list.clear()
