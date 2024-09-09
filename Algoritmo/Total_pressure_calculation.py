def calcular_presion(m1, M1, m2, M2, V, T):
    # Constante de gas en las unidades dadas (dm^3 · atm · K^(-1) · mol^(-1))
    R = 0.082

    # Convertimos la temperatura de Celsius a Kelvin
    T_kelvin = T + 273.15

    # Calculamos el número de moles de cada gas
    n1 = m1 / M1  # n1 = moles del gas 1
    n2 = m2 / M2  # n2 = moles del gas 2

    # Usamos la fórmula para calcular la presión total
    P_total = ((n1 + n2) * R * T_kelvin) / V

    # Devolvemos la presión total en atm
    return P_total


# Ejemplo de uso con valores dados (puedes cambiar los valores para probar otros casos):
M1 = 32.0  # masa molar del gas 1 (g/mol)
M2 = 28.0  # masa molar del gas 2 (g/mol)
m1 = 16.0  # masa presente del gas 1 (g)
m2 = 14.0  # masa presente del gas 2 (g)
V = 10.0  # volumen del recipiente en dm^3
T = 25  # temperatura en grados Celsius

# Llamamos a la función para calcular la presión total
P_total = calcular_presion(m1, M1, m2, M2, V, T)

# Mostramos el resultado
print(f"La presión total es: {P_total} atm")
