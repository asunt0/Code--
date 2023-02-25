


#creando diccionarios con dict
diccionario = dict(gusto_musical = "deftones", gatos_o_perros = "both")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario2 = {frozenset(["hola", "XD"]), "jajas"}

#creando diccionarios con fromkeys
diccionario3 = dict.fromkeys(["nombre", "apellido", "edad"])
print(diccionario3)
print(type(diccionario3))
