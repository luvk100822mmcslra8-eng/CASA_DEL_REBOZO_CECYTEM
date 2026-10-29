tabla =[
    ["nombre","edad","Calificacion"],
    ["Luis",17,8.0],
    ["Darina",16,9.0],
    ["Valeria",16,9.0],
    ["Carlos",16,9.0],
    ["Oscar",16,9.0],
    ["Mariel",16,9.0],
    ["Sherlyn",16,9.0],
    ["Jorge",16,9.0],
    ["Jesus",16,9.0],
    ["Melisa",16,9.0],
    ["Ximena",16,9.0]
]
buscar=input("Nombre a buscar:")
filas=len(tabla)
columnas=len(tabla[0])
#Ciclo externo para manejar filas(i)
for i in range(filas):
    #Ciclo eterno para manejar columnas
    for j in range(columnas):
        #Verificamos si encontramos el tesoro
        if tabla[i][j] ==buscar:
            print(f"Nombre encontrado en la posicion {i},{j} ->{tabla[i]}")