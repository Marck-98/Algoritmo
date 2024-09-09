def tercer_angulo(angulo1, angulo2):
    # La suma de los ángulos interiores de un triángulo siempre es 180 grados
    # Para calcular el tercer ángulo, restamos la suma de los dos primeros ángulos de 180
    angulo3 = 180 - (angulo1 + angulo2)

    # Devolvemos el valor del tercer ángulo
    return angulo3


# Función para pedir un número entero y manejar posibles errores
def pedir_entero(mensaje):
    while True:
        try:
            # Pedimos al usuario que ingrese un valor
            valor = int(input(mensaje))
            return valor  # Si es válido, devolvemos el valor
        except ValueError:
            # Si no es un entero, mostramos un mensaje de error y repetimos
            print("Por favor, ingresa un número entero válido.")


# Pedimos al usuario que ingrese los dos ángulos, asegurándonos de que sean enteros
angulo1 = pedir_entero("Ingresa el primer ángulo (entero): ")
angulo2 = pedir_entero("Ingresa el segundo ángulo (entero): ")

# Llamamos a la función para obtener el tercer ángulo
print(f"El tercer ángulo es: {tercer_angulo(angulo1, angulo2)}")
