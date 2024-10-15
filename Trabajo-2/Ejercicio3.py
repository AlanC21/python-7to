import sqlite3

# 1. Crear una base de datos llamada "escuela.db".
conexion = sqlite3.connect("escuela.db")

# 2. Crear una tabla llamada "alumnos" con las columnas id, nombre y curso.
with conexion:
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            curso TEXT NOT NULL
        )
    """)

# 3. Insertar 3 alumnos con nombres y cursos diferentes.
with conexion:
    conexion.execute("INSERT INTO alumnos (nombre, curso) VALUES ('Juan Pérez', 'Matemáticas')")
    conexion.execute("INSERT INTO alumnos (nombre, curso) VALUES ('Ana Gómez', 'Física')")
    conexion.execute("INSERT INTO alumnos (nombre, curso) VALUES ('Carlos López', 'Programación')")

# 4. Guardar los cambios y cerrar la conexión.
conexion.commit()
conexion.close()