# 2 listas - indices impares con try y except
try:
    alumnos = ["Carlos", "Darina", "Jesus", "Mariel", "Jorge"]
    calificaciones = [8, 10, 9, 9, 5]
    print("--- ALUMNOS EN INDICES IMPARES ---")
    # Mostrar solo indices impares (1, 3)
    for i in range(5):
        if i % 2 != 0:
            print(f"Indice {i} - Alumno: {alumnos[i]} - Calificacion: {calificaciones[i]}")
    # Prueba para el except - si pones un indice que no existe
    print(alumnos[2])
except IndexError:
    print("El indice no existe")