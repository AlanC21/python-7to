# Lista de estudiantes con su edad
estudiantes = [
    {"nombre": "Juan", "edad": 18},
    {"nombre": "María", "edad": 22},
    {"nombre": "Pedro", "edad": 16},
    {"nombre": "Lucía", "edad": 19}
]

# Función que devuelve el estudiante con mayor y menor edad
def encontrar_mayor_menor_estudiante(estudiantes):
    mayor = max(estudiantes, key=lambda x: x["edad"])
    menor = min(estudiantes, key=lambda x: x["edad"])
    return mayor, menor

mayor, menor = encontrar_mayor_menor_estudiante(estudiantes)
print(f"Estudiante con mayor edad: {mayor}")
print(f"Estudiante con menor edad: {menor}")
