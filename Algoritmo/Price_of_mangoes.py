def costo_mangos(cantidad, precio_por_mango):
    # Para cada 3 mangos, solo pagas por 2. Así que pagas por (cantidad // 3) * 2 + (cantidad % 3)
    # cantidad // 3 calcula cuántos grupos de 3 mangos tienes
    # (cantidad % 3) calcula cuántos mangos adicionales quedan fuera de los grupos de 3
    mangos_a_pagar = (cantidad // 3) * 2 + (cantidad % 3)

    # Multiplicamos los mangos a pagar por el precio por mango para obtener el costo total
    costo_total = mangos_a_pagar * precio_por_mango

    # Devolvemos el costo total
    return costo_total


# Ejemplo de uso
print(costo_mangos(2, 3))  # 2 mangos a $3 cada uno = $6
print(costo_mangos(3, 3))  # 3 mangos (1 gratis), solo pagas 2 a $3 = $6
print(costo_mangos(5, 3))  # 5 mangos (1 gratis), pagas 4 a $3 = $12
print(costo_mangos(9, 5))  # 9 mangos (3 gratis), pagas 6 a $5 = $30
