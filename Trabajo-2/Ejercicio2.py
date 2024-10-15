# 1. Crear un archivo nuevo llamado "notas.txt".
with open("notas.txt", "w") as archivo:
    # 2. Escribir tres líneas con información de materias favoritas.
    archivo.write("Matemáticas\n")
    archivo.write("Programación\n")
    archivo.write("Física\n")

# 4. Volver a abrir el archivo y mostrar las tres líneas, una por una.
with open("notas.txt", "r") as archivo:
    # Leer y mostrar cada línea por separado.
    for linea in archivo:
        print(linea.strip())  # 'strip()' elimina los saltos de línea adicionales.
