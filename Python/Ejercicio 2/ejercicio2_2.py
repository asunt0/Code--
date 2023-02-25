


#creando una funcion que nos devuelva numeros primos
#entre 0 y el argumento que le pasemos

def es_primo(num):
    for i in range(2,num - 1):
        if (num % i == 0): return False
    return True

def primo_hasta(num):
    primos = []
    for i in range(num):
        resultado = es_primo[i]
        if resultado == True:
            primos.append(i)
    return primos

resultado = primo_hasta(12)
print(resultado) #false no es primo



            