# Registro de personas en un diccionario
personas = [
    {"nombre": "Carlos", "edad": 25, "correo": "carlos@example.com"},
    {"nombre": "Ana", "edad": 17, "correo": "ana@example.com"},
    {"nombre": "Luis", "edad": 19, "correo": "luis@example.com"}
]

# Función que filtra personas mayores de 18 años
def filtrar_mayores_18(personas):
    return [persona for persona in personas if persona["edad"] > 18]

mayores_18 = filtrar_mayores_18(personas)
print("Personas mayores de 18 años:")
for persona in mayores_18:
    print(persona)
