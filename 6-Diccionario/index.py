# Diccionario de productos y precios
productos = {
    "manzana": 0.5,
    "banana": 0.3,
    "pan": 1.2
}

# Función que calcula el total a pagar
def calcular_total_a_pagar(productos_seleccionados):
    total = sum(productos[producto] * cantidad for producto, cantidad in productos_seleccionados.items())
    return total

# Ejemplo de productos seleccionados
productos_comprados = {
    "manzana": 4,
    "banana": 5
}

total = calcular_total_a_pagar(productos_comprados)
print(f"Total a pagar: {total:.2f}")
