# Ejemplo 1 manejo de excepciones
numero1=5
numero2=4
try:
    numero1 = float(input("Ingresa el primer numero: "))
    numero2 = float(input("Ingresa el segundo numero: "))
    resultado = numero1 / numero2
    print("Resultado")
except ValueError:
    print("Error: No se puede dividir una letra")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
