#Ciclo externo
for i in range(1,4):
    print(f"---Tabla del {i}---")
    #Ciclo imterno ultiplica la base por el numero j
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print(f"AQUI TERMINA LA TABLA DEL{i}")