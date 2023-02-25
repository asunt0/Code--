


#creando una funcion que nos muestre una funcion finoganzi entre 0 y el numero dado

# def fibonacci (num):
#     a, b = 0, 1
#     fibonacci_lista = [0]
#     for i in range(num):
#         if  b > num: 
#             return fibonacci_lista
#         else:
#             fibonacci_lista.append(b)
#             a, b = b, a + b
            
# resultado = fibonacci(20)
# print(resultado)

# lista = ['sebas', 15]
# nombre, edad = lista
# print(edad)

# s = 'python'
# print(s[0:2])

# fruit = 'banana'
# if 'n' in fruit:
#     print('Found it!')

def division(num,num2):
    num / num2 
    c = num / num2
    print(f'Su division incluyendo dicimales es: {c}')
    num % num2
    d = num % num2
    print(f'El resto de la division fue: {d}')
    num // num2
    e = num // num2
    print(f'Su division sin decimales es: {e}')
    
division(5, 2)