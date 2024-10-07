# Diccionario donde se almacenarán los empleados
empleados = {
    "Alan Cordoba": {"edad": 18, "puesto": "Programadro"},
    "Ana Lopez": {"edad": 30, "puesto": "Desarrolladora"},
    "Luis Perez": {"edad": 45, "puesto": "Gerente de proyectos"},
    "Maria Diaz": {"edad": 25, "puesto": "Analista de datos"},
    "Carlos Gomez": {"edad": 38, "puesto": "Ingeniero de software"},
    "Laura Fernandez": {"edad": 28, "puesto": "Diseñadora gráfica"},
    "Jorge Ramos": {"edad": 50, "puesto": "Director de marketing"},
    "Sofia Martinez": {"edad": 32, "puesto": "Reclutadora"},
    "Pablo Castro": {"edad": 27, "puesto": "Consultor"},
    "Lucia Gutierrez": {"edad": 40, "puesto": "Contadora"}
}

# Función para agregar empleados
def agregar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    if nombre in empleados:
        print(f"El empleado {nombre} ya existe en el registro.")
        return
    edad = int(input("Ingrese la edad del empleado: "))
    puesto = input("Ingrese el puesto del empleado: ")
    empleados[nombre] = {"edad": edad, "puesto": puesto}
    print(f"Empleado {nombre} agregado correctamente.")

# Función para listar todos los empleados
def listar_empleados():
    if not empleados:
        print("No hay empleados registrados.")
        return
    print("\nLista de empleados:")
    for i, (nombre, detalles) in enumerate(empleados.items(), start=1):
        print(f"{i}. Nombre: {nombre}, Edad: {detalles['edad']}, Puesto: {detalles['puesto']}")
    print()

# Función para actualizar un empleado
def actualizar_empleado():
    nombre = input("Ingrese el nombre del empleado a actualizar: ")
    if nombre not in empleados:
        print(f"El empleado {nombre} no existe en el registro.")
        return
    print("¿Qué desea actualizar?")
    print("1. Edad")
    print("2. Puesto")
    opcion = input("Ingrese el número de opción: ")
    if opcion == "1":
        nueva_edad = int(input("Ingrese la nueva edad: "))
        empleados[nombre]["edad"] = nueva_edad
        print(f"Edad actualizada correctamente para {nombre}.")
    elif opcion == "2":
        nuevo_puesto = input("Ingrese el nuevo puesto: ")
        empleados[nombre]["puesto"] = nuevo_puesto
        print(f"Puesto actualizado correctamente para {nombre}.")
    else:
        print("Opción no válida.")

# Función para eliminar un empleado
def eliminar_empleado():
    nombre = input("Ingrese el nombre del empleado a eliminar: ")
    if nombre in empleados:
        del empleados[nombre]
        print(f"Empleado {nombre} eliminado del registro.")
    else:
        print(f"El empleado {nombre} no existe en el registro.")

# Función opcional para calcular la edad promedio de los empleados
def calcular_edad_promedio():
    if not empleados:
        print("No hay empleados registrados.")
        return
    total_edad = sum(detalles["edad"] for detalles in empleados.values())
    promedio_edad = total_edad / len(empleados)
    print(f"La edad promedio de los empleados es: {promedio_edad:.2f} años.")

# Menú principal
def menu():
    while True:
        print("\n----- Menú de opciones -----")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Actualizar empleado")
        print("4. Eliminar empleado")
        print("5. Calcular edad promedio (opcional)")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_empleado()
        elif opcion == "2":
            listar_empleados()
        elif opcion == "3":
            actualizar_empleado()
        elif opcion == "4":
            eliminar_empleado()
        elif opcion == "5":
            calcular_edad_promedio()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Iniciar el programa
if __name__ == "__main__":
    menu()