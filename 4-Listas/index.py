# Función para ordenar una lista de números
def ordenar_numeros(lista_numeros):
    lista_ordenada = []
    
    # Añadir cada número a una nueva lista
    for numero in lista_numeros:
        lista_ordenada.append(numero)
    
    # Ordenar la lista
    lista_ordenada.sort()
    
    # Mostrar la lista ordenada
    print(f"Números ordenados: {lista_ordenada}")
    print(f"Cantidad de números: {len(lista_ordenada)}")
    
    # Encontrar y mostrar el número máximo y mínimo
    print(f"Máximo: {max(lista_ordenada)}")
    print(f"Mínimo: {min(lista_ordenada)}")
    print(f"")

# Función para ordenar una lista de letras
def ordenar_letras(lista_letras):
    lista_ordenada = []
    
    # Añadir cada letra a una nueva lista
    for letra in lista_letras:
        lista_ordenada.append(letra)
    
    # Ordenar la lista
    lista_ordenada.sort()
    
    # Mostrar la lista ordenada
    print(f"Letras ordenadas: {lista_ordenada}")
    print(f"Cantidad de letras: {len(lista_ordenada)}")
    
    # Encontrar y mostrar la letra máxima y mínima (en términos de orden alfabético)
    print(f"Máxima (alfabéticamente): {max(lista_ordenada)}")
    print(f"Mínima (alfabéticamente): {min(lista_ordenada)}")
    print(f"")

# Ejemplo de uso
numeros = [5, 2, 9, 1, 5, 6]
letras = ['z', 'b', 'a', 'm', 'q']

ordenar_numeros(numeros)
ordenar_letras(letras)
