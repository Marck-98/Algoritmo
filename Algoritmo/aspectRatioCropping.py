import math  # Importamos la librería math para redondear al siguiente número entero.


def convertir_a_16_9(x_original, y_original):
    # Calcula el nuevo ancho (X) manteniendo la altura (Y) constante
    # 16 / 9 es la relación de aspecto deseada, entonces multiplicamos la altura por 16/9.
    nuevo_x = math.ceil(y_original * (16 / 9))

    # Devolvemos el nuevo ancho (X) junto con la altura original (Y)
    return nuevo_x, y_original


# Ejemplo de uso con una resolución de 374x280 (relación 4:3)
x_original = 374
y_original = 280

# Llamamos a la función para obtener la nueva resolución con aspecto 16:9
nuevo_x, nuevo_y = convertir_a_16_9(x_original, y_original)

# Mostramos los resultados
print(f"Resolución original: {x_original}x{y_original}")
print(f"Nueva resolución con aspecto 16:9: {nuevo_x}x{nuevo_y}")
