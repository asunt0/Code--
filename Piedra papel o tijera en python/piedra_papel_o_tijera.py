
#user data
nombre = input("Introduzca su nombre: ")
apellido = input(["Hola!: ", nombre, ' Introduce tu apellido: '] )

#pregunta
pregunta = input(["Quieres jugar un juego?", nombre + " " + apellido, "Coloca si o no: "])

#juego
piedra = "piedra"
papel = "papel"
tijera = "tijera"

if pregunta.find("si") >= 0 :
    print("Vale! juguemos a piedra papel o tijera a ver si le ganas a esta maquina jajas")
    contador = input([piedra + " " + papel + " " + tijera + " 1.. 2.. 3.. YA!" ])
    if contador.find("piedra") >= 0 :
        print("Papel")
    elif contador.find("papel") >= 0 :
        print("tijera")
    elif contador.find("tijera") >= 0 :
        print("piedra")
    else :
        print("porfavor introduce un valor valido.")

else:
    print("Vale hasta luego!")
