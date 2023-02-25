


#promedio de duraciones
otros_cursos_min = 2.5
otros_cursos_max = 7 
otros_cursos_promedio = 4
dalto_curso = 1.5

#recordemos que primero se ejecutan las divisiones luego la multis y luego las restas

#diferencias min
diferencias_con_min =  dalto_curso / otros_cursos_min * 100 #esto es una formula para sacar porcentaje 

print("-----------------------------")

print(f'el curso de dalto dura un {diferencias_con_min}% menos que el mas rapido') 


#diferencias max
diferencias_con_max =  dalto_curso  / otros_cursos_max * 100 # esta formula es para mover la comilla matematica avanzada.

print(f'el curso de dalto dura un {round(diferencias_con_max)}% menos que el mas lento') 

#diferencias otros cursos promedio
diferencias_con_promedio =  dalto_curso / otros_cursos_promedio * 100

print(f'el curso de dalto dura un {diferencias_con_promedio}% menos que el promedio') 
print("-----------------------------")


#diferencias de crudo (video crudo sin editar)
crudo_promedio = 5
crudo_de_dalto = 3.5

diferencias_de_crudos = crudo_de_dalto / crudo_promedio * 100 

print(f'el curso de dalto tiene un {diferencias_de_crudos}% de crudo menos que los cursos promedio')
print("-----------------------------")


#cuanto eliminan los cursos de su videos
tiempo_vacio_promedio = 100 - otros_cursos_promedio / crudo_promedio * 100
tiempo_vacio_dalto = 100 - dalto_curso  / crudo_de_dalto *100

print(f'los cursos promedio eliminan un {tiempo_vacio_promedio}% de tiempo vacio de sus videos')
print(f'el curso de dalto elimina un {round(tiempo_vacio_dalto)}% de tiempo vacio de sus videos')
print("-----------------------------")


#mostrando las diferencias  si los cursos duraran 10 horas
print(f'ver 10 horas de este curso equivale a {otros_cursos_promedio * 100 // dalto_curso / 10}% horas de otros cursos')
print(f'ver 10 horas de otros cursos equivale a {dalto_curso * 100 // otros_cursos_promedio / 10}% horas de de este curso')
print("-----------------------------")








