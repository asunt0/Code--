#Creating a list can be modified (lista)
list = ["Sebastian Figueroa","Asunt",True, 1.72]

#Creating a tuple can't be modified (tupla)
tuple = ("Sebastian Figueroa","Asunt",True, 1.72)

#This is valid

list[3] = "JAJA"

#This is not

#tuple[3] ="JAJA"

#Creating a set (conjunto) (NO SE PUEDE LLAMAR A ELEMENTOS POR SU INDICES, NO SE PUEDEN ALMACENAR DATOS DUPLICADOS, Y SON DATOS DESORDENADOS) 

set = {"Sebastian Figueroa","Asunt",True, 1.72}

#This is valid

#set = {"hola"}

#this is not

#set[2] = "hola"

#NO PUEDE ACCEDER AL ELEMENTO

#print(set[3])

#Creating a dict (diccionario) (LA ESTRUCTURA ES key: value) (se ponen comas, para separar los elementos. si hay solo uno no se coloca)

dict = {
    'nombre' : "Sebastian Figueroa",
    'id' : "Asunt",
    'esta_emocionado' : True,
    'estatura' : 1.72
}


print(list[0])

print(tuple[2])

print(set)

print(dict['estatura'] + 0.1) 

