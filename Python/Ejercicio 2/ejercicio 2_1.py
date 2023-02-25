


#falto el profe y los pibes van a armar la clase

#pedir el nombre y la edad de lso compañeros que vinieron a clase
def obtener_compañeros(cantidad_de_compañeros):
    #creando la lista con los compañeros
    compañeros = []
   
    #ejecutando un for para pedir la informacion
    for i in range(cantidad_de_compañeros): #se va a repetir 7 veces un bucle para eso es range amigo
      nombre = input('Tu nombre aqui: ')
      edad = int(input('Tu edad aqui: ')) #para que las respuesta que nos den sea un numero
      compañero = (nombre, edad)
     
      #añadiendo la informacion a la lista
      compañeros.append(compañero) #agregamos los datos del compañero a la lista
    
    #ordenandolos de mayor a menor por su edad
    compañeros.sort(key=lambda x: x[1])
    
    asistente = compañeros[0][0] #pq como ya la ordenamos sreia el primero el primer parametro es el nombre y el otro es su edad
    profesor = compañeros[-1][0]
    return asistente, profesor

asistente, profesor = obtener_compañeros(5)

print(f'El profesor es: {profesor} y su asistente es {asistente}')
#