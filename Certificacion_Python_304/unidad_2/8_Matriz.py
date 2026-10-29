#Creando una matriz
numero=[
    [1,2,3],#fila 0
    [2,3,4],#fila 1
    [5,6,7]#fila 2
]
#Obteniendo el numero de filas
filas=len(numero[0])#filas 3
#Obteniendo el numero de columnas
columnas=len(numero[0])
#Ciclo externo para los indices de las filas(i)
for i in range(filas):
    #Ciclo interno para los indices internos de las columnas(j)
    for j in range(columnas):
        print(f"[{i}] [{j}] = {numero[i][j]}")

