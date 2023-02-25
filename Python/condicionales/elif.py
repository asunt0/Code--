ingreso_mensual = 80000
gasto_mensual = 76000
#if anidados y elifs
if ingreso_mensual >= 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("tas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("tas bien pa")
    else:
        print("epa tas gastando un monton hay q ver si alcanzas")

elif ingreso_mensual > 1000:
    print("estas bien economicamente en latinoamerica")

elif ingreso_mensual >= 200:
    print("estas bien economicamente en venezuela")
    
else:
    print("sos pobre")