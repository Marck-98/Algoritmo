def nba_extrap(ppg, mpg):
    # Si los minutos por juego son 0, el jugador no ha jugado, por lo que devolvemos 0
    if mpg == 0:
        return 0

    # Extrapolamos los puntos por juego a 48 minutos
    # La fórmula es (ppg / mpg) * 48 para ajustar los puntos a un juego completo de 48 minutos
    extrapolacion = (ppg / mpg) * 48

    # Redondeamos el resultado a un decimal
    return round(extrapolacion, 1)


# Ejemplo de uso
print(nba_extrap(12, 20))  # Debería devolver 28.8
print(nba_extrap(10, 10))  # Debería devolver 48
print(nba_extrap(5, 17))  # Debería devolver 14.1
print(nba_extrap(0, 0))  # Debería devolver 0
