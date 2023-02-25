



diccionario = {
    "nombre" : 'Sebastian',
    "apellido" : 'Figueroa',
    "edad" : 15
}
#mostrando solo las keys con keys
claves = diccionario.keys()

#obteniendo un valor en concreto con get (No lanza excepcion y si no encuentra nada el programa continua)
obtener = diccionario.get("edad")

#eliminando todos los elementos de un diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop('edad')

#obteniendo un elemento dict_items iterable
dict_iterable = diccionario.items()
#print(dict_iterable)

