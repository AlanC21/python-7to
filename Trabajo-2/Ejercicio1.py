# 1. Crear un archivo llamado "mi archivo.txt" en modo escritura.
with open("mi archivo.txt", "w") as archivo:
    # 2. Escribir la frase.
    archivo.write("Hola, estoy aprendiendo Python")
    # El archivo se cierra automáticamente con 'with'.

# 4. Volver a abrir el archivo en modo lectura.
with open("mi archivo.txt", "r") as archivo:
    # 5. Leer el contenido y mostrarlo en pantalla.
    contenido = archivo.read()
    print(contenido)
