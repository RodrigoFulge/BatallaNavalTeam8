import random

print("Las siguientes son las calificaciones de los 10 alumnos: ")
Grades = [random.randint(4, 10) for i in range(10)]

print(f"Calificaciones de los estudiantes: {Grades}")
Pasan = [i for i in Grades if i >= 7]
print(f"Las calificaciones aprobatorias son: {Pasan}")