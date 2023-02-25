


diccionario = {
    'nombre' : "sebas",
    'apellido' : "figueroa",
    'ciudad' : "barquisimeto"
}

#recorriendo un diccionario con items para obtener la clave
for key in diccionario:
    key 
    print(f"la clave es: {key}")

#recorriendo un diccionario con items para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"los datos son: {key} y el valor: {value}")