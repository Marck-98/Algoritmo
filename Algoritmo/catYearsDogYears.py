# Calcula la edad del perro y el gato en años humanos
def calculate_pet_ages(humanYears):
    # Inicializar las variables para las edades de los gatos y perros
    catYears = 0  # Edad del gato en años de gato, inicializada en 0
    dogYears = 0  # Edad del perro en años de perro, inicializada en 0

    # Calcular los años de los gatos
    if humanYears >= 1:  # Si la edad humana es 1 o más
        catYears += 15  # El primer año equivale a 15 años de gato
    if humanYears >= 2:  # Si la edad humana es 2 o más
        catYears += 9  # El segundo año suma 9 años más de gato
    if humanYears > 2:  # Si la edad humana es mayor a 2 años
        catYears += (humanYears - 2) * 4  # Cada año adicional después del segundo suma 4 años de gato

    # Calcular los años de los perros
    if humanYears >= 1:  # Si la edad humana es 1 o más
        dogYears += 15  # El primer año equivale a 15 años de perro
    if humanYears >= 2:  # Si la edad humana es 2 o más
        dogYears += 9  # El segundo año suma 9 años más de perro
    if humanYears > 2:  # Si la edad humana es mayor a 2 años
        dogYears += (humanYears - 2) * 5  # Cada año adicional después del segundo suma 5 años de perro

    # Retornar las edades en una lista
    return [humanYears, catYears, dogYears]  # Devuelve una lista con la edad humana, la edad del gato y la edad del perro

# Solicitar al usuario que ingrese los años humanos
human_years_input = int(input("Ingresa la edad en años humanos: "))
# Usa input() para pedir al usuario que ingrese un valor desde el teclado
# Se convierte este valor en un número entero usando int()

# Calcular y mostrar los resultados
result = calculate_pet_ages(human_years_input)  # Llama a la función para calcular las edades y guarda el resultado en 'result'
print(f"Edad en años humanos: {result[0]}")  # Imprime la edad humana ingresada por el usuario
print(f"Edad del gato en años de gato: {result[1]}")  # Imprime la edad del gato calculada en años de gato
print(f"Edad del perro en años de perro: {result[2]}")  # Imprime la edad del perro calculada en años de perro
