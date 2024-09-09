import math  # Importamos la librería math para usar la función de redondeo hacia abajo.


def calcular_litros(time):
    # Nathan bebe 0.5 litros de agua por cada hora de ciclismo
    # Multiplicamos el tiempo por 0.5 para obtener la cantidad de litros
    litros = time * 0.5

    # Redondeamos el número de litros hacia abajo usando math.floor()
    litros_redondeados = math.floor(litros)

    # Devolvemos el valor redondeado
    return litros_redondeados


# Ejemplo de uso
time1 = 3
time2 = 6.7
time3 = 11.8

# Llamamos a la función para obtener la cantidad de litros que Nathan beberá
print(f"Para {time1} horas, Nathan beberá {calcular_litros(time1)} litros.")
print(f"Para {time2} horas, Nathan beberá {calcular_litros(time2)} litros.")
print(f"Para {time3} horas, Nathan beberá {calcular_litros(time3)} litros.")
