
cadena1 = "hola soy marina"
cadena3 = ["XD", 7 ]

#todo en mayuscula
mayus = cadena1.upper()

#todo en minuscula
cadena2 = "Y TENGO UN HIJO".lower()

#primera letra en mayuscula
primeramayus = cadena1.capitalize()

#buscamos una cadena en otra cadena si n hay coincidencias devuelve -1
cadena1 = "hola soy marina"
buscar = cadena1.find("9")

#buscamos una cadena en otra cadena si n hay coincidencia nos tirara un error
# #buscar_index: cadena1.index("9")

#isnumeric si es numerico devolvera true si n false
cadena1 = "hola soy marina"
es_numerico = cadena1.isnumeric()

#isalphanumeric si es alpha devolera true y si n false
cadena4 = "holaXD"
es_alpha = cadena4.isalpha()
#count contara los valores q encuentre
cadena5 = "hey what's up bro everything allright?"
contar = cadena5.count("e")

#len CONTARA TODOS LOS CARACTERES Q TENGA UNA CADENA
#LEN ES UNA FUNCION NO UN METODO
contar_todo = len(cadena5)

#verifica si una cadena empieza con una cadena dada si es asi devuelve true
cadena1 = "hola soy marina"
comienza_con = cadena1.startswith("H")

#verifica si una cadena termina con una cadena dada si es asi devuelve true
cadena1 = "hola soy marina"
termina_con = cadena1.endswith("a")

#reemplaza un pedazo de la cadena dada por otra dada
cadena6 = "hola"
cadena_reemplazo = cadena6.replace("la", "lu")
cadena7 = "Hola.cuanto.mides?"
cadena_reemplazo2 = cadena7.replace(".", " ")

#separar cadenas con la cadenas q le pasamos
cadena7 = "Hola.cuanto.mides?"
cadena_separada = cadena7.split(".")
print(cadena_separada)
print(type(cadena_separada))
print(cadena_separada[1])
