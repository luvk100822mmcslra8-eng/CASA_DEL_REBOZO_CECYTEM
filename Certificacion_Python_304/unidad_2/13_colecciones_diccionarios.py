#creando diccionario
persona={
    "nombre":"valeria",
    "edad":16,
    "profesion":"ptogramador",
    "estudiante":False
}
print(persona)
#Accediendo a un valor en  especifico
print(persona["nombre"])
#se usa en el metodo get
#es util porque no marca error si el valor no existe
print(persona.get("profesion"))
persona["edad"]=23
print(persona["edad"])
#agrega un par(clave:cvalor)
persona["ciudad"]="cecy ranch"
print(persona)
#recorrer un diccionariocon un buqle
