

#creando un conjunto con la funcion set
conjunto = set({"dato1", "dato2"})


#metiendo un conjunto dentro de un conjunto
#conjunto1 = frozenset(["dato1", "dato2"])
#conjunto2 = {conjunto1, "dato3"}


#teoria de conjuntos
conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

resultado = conjunto2.issubset(conjunto1)

#diciendo si es un subconjunto con <=
resultado2 = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado3 = conjunto2.issuperset(conjunto1)
resultado4 = conjunto2 >= conjunto1

#verificando si tienen un numero en comun
resultado5 = conjunto2.isdisjoint(conjunto1)

print(resultado5)