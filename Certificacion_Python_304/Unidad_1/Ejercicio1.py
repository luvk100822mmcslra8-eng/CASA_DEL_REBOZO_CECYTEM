#realizar un programa que calcule
#compra total de 4 productos, si la compra total  
#es mayor a 2000 pesoa me haga un descuento
#del 20% 
#DATOS DE ENTRADA TENGO
precio1=float(input("Introduce el precio del producto1"))
precio2=float(input("Introduce el precio del producto2"))
precio3=float(input("Introduce el precio del producto3"))
precio4=float(input("Introduce el precio del producto4"))
#proceso
total=precio1+precio2+precio3+precio4.10
if total<2000:
    total=(total-(total*.10))
#total
   print(total)
else:print("no tienes descuento")
