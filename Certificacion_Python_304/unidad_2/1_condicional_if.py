promedio=float(input("Ingresa tu promedio"))
if promedio<=-5:
    print("Tu promedio no es aceptable")
elif promedio<=5 and promedio<=7:
    print("Tu promedio es bajo")
elif promedio<=7 and promedio<=9:
    print("Tu promedio es bueno")
elif promedio>=9 and promedio <=10:
    print("Tu promedio es muy bueno")
else:
    print("Ese promedio no existe")

