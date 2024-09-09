def convertir_usd_a_cny(usd):
    # Definimos la tasa de conversión de 1 USD a CNY
    tasa_conversion = 6.75

    # Calculamos el valor en CNY multiplicando la cantidad de USD por la tasa de conversión
    cny = usd * tasa_conversion

    # Formateamos el valor en CNY como string con 2 decimales y añadimos la cadena 'Chinese Yuan'
    resultado = f"{cny:.2f} Chinese Yuan"

    # Devolvemos el resultado final como cadena
    return resultado


# Ejemplo de uso
usd1 = 15
usd2 = 465

# Llamamos a la función para convertir los valores de USD a CNY
print(convertir_usd_a_cny(usd1))  # '101.25 Chinese Yuan'
print(convertir_usd_a_cny(usd2))  # '3138.75 Chinese Yuan'
