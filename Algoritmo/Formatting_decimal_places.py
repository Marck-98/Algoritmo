# Definimos una función que recibe un número como entrada
def redondear_a_dos_decimales(numero):
    # Utilizamos la función round para redondear el número a dos decimales
    numero_redondeado = round(numero, 2)
    # Retornamos el número redondeado
    return numero_redondeado

# Ejemplo de uso de la función
# Definimos un número de ejemplo
numero_ejemplo = 5.5589
# Llamamos a la función para redondear el número
numero_redondeado = redondear_a_dos_decimales(numero_ejemplo)
# Imprimimos el resultado
print(f"Número redondeado: {numero_redondeado}")

# Otro ejemplo
numero_ejemplo = 3.3424
numero_redondeado = redondear_a_dos_decimales(numero_ejemplo)
print(f"Número redondeado: {numero_redondeado}")
