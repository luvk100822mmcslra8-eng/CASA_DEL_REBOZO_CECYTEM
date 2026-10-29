numero=int(input("Ingresa un numero del 1 al 10:"))

while numero < 1 or numero > 10:
    print("Error: tu numero no es corecto")
    numero=int(input("Ingresa un numero del 1 al 10:"))

i=1
while i <=10:
    resultado=numero*1
    print(numero, "x",i, "=", resultado)
    i=i+1
