

# #creando una funcion simple
# def saludar():
#     print("Hola maestro como andas")
# #ejecutando al funcion simple
# saludar()


#creando una funcion con parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
        
    elif sexo == "hombre":
        adjetivo = "titan"
    else:
        adjetivo = "gay"
    
    print(f"Hola {nombre} mi {adjetivo} como estas ")
    
saludar("Marimiga", "muJER")

#creando una funcion que nos retorna valores
def crear_contraseña_random(num):
    caracteres = "abdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f'{caracteres[c1]}{caracteres[c2]}{caracteres[c3]}{num * 2}'
    return contraseña
    
password = crear_contraseña_random(8)
frase = f'tu contraseña random es {password}'
print(frase)