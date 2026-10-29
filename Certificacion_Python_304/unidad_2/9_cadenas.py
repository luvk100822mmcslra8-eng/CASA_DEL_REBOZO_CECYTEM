cadena1='Hola'
cadena2='Mundo'
multilinea="""Esto es una cadena
de varias lineas"""
print(cadena1+cadena2+multilinea)
eco='ja'*3
print(eco)
#cambiar una cadena de minuscula a mayiscula
tu_nombre='valeria'
print(tu_nombre.upper())
#cambiar una cadena de  mayuscula a minuscula 
print(tu_nombre.lower())
#reamplazar texto en cadena
frase="Me gusta programacion"
print(frase.replace("programacion","matematicas"))
#foremato de cadenas (f-string)
edad=17
nombre='valeria'
mensaje=f"Hola, me llamo {nombre} y tengo {edad} años"
print(mensaje)
#contar los caracteres de una cadena
texto= "¡Felicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#comprobar si un texto contiene una palabra
oracion="Aprender python es divertido"
if"java" in oracion:
    print("Encontrado")
else:
    print("no esta")
#validar contenido en una cadena
nlista='valeria'
print(nlista.isalpha())
print(nlista.isdigit())