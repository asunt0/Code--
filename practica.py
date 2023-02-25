def greet(lang):
    if lang == 'es':
        print("hola")
    elif lang == 'fr':
        print('bonjour')
    else:
        print('hello')
        
#greet()

def saludo(lenguaje):
    if lenguaje == 'en':
        return 'Hello'
    elif lenguaje == 'fr':
        return 'Bonjour'
    else:
        return 'Hola XD'
    
print(saludo('fr'), 'Sebastian')

 
    
friends = ["nobody","myvoices","myself"]
for friend in friends:
    print(f'Hello {friend}')
print('Done!')


# #mas grande loop
# largerst = -1

# for number in [9, 2, 12, 5]:
#     if number > largerst:
#         largerst = number
#     print(largerst, number)

#mas pequeño
smallest = None
for number in [ 41, 9, 15, 12]:
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
        
        print(smallest, number)
print(smallest)

    


#sumar y contador in loop
contador = 0
suma = 0
for thing in [92, 12, 3, 6, 69]:
    contador = contador + 1
    suma = suma + thing
    print(contador, suma, thing)
print('total', suma)

pregunta = 0 is 0.0
pregunta2 = 0 == 0.0
print(pregunta)



name = input('Enter Name: ')
apple = input('Enter : ')
x = int(apple) - 10
print(x)

fruit = 'banana'
count = 0
for n in fruit:
    if n == 'a':
        count = count + 1
    print(count)