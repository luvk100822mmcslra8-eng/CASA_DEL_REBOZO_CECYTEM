#Declarando una lista 
try:
   materias=["Programacion", "Filosofia", "Matematicas", "Ingles"]
   print(materias[3])
   materias.append("lengua y comunicacion")
   print(materias)
   materias[1]="Biologia"
   print(materias)
   materias.remove("Matematicas")
   print(materias)
except IndexError:
   print("Este indidice no existe")