import math  # Importamos la librería para usar la función floor (redondear hacia abajo)


def rango_edad(age):
    # Si la edad es menor o igual a 14, usamos una regla diferente para calcular el rango
    if age <= 14:
        min_age = math.floor(age - 0.10 * age)  # Restamos el 10% de la edad
        max_age = math.floor(age + 0.10 * age)  # Sumamos el 10% de la edad
    else:
        # Para edades mayores de 14, usamos la regla "mitad de la edad más 7"
        min_age = math.floor(age / 2 + 7)  # Edad mínima: mitad de la edad + 7
        max_age = math.floor((age - 7) * 2)  # Edad máxima: (edad - 7) * 2

    # Retornamos el rango de edad en el formato [min]-[max]
    return f"{min_age}-{max_age}"


# Ejemplos de uso
print(rango_edad(27))  # Debería devolver 20-40
print(rango_edad(5))  # Debería devolver 4-5
print(rango_edad(17))  # Debería devolver 15-20
